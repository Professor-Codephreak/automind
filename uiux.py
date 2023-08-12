# uiux.py
import os
import gradio as gr
import fire
import time
import pathlib
import ujson
from enum import Enum
from threading import Thread
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from auto_gptq import AutoGPTQForCausalLM
from llama_cpp import Llama
from huggingface_hub import hf_hub_download
# codephreak is automind + memory + aglm
from automind import format_to_llama_chat_style
from memory import save_conversation_memory
from aglm import LlamaModel

# class syntax
class Model_Type(Enum):
    gptq = 1
    ggml = 2
    full_precision = 3

def get_model_type(model_name):
    if "gptq" in model_name.lower():
        return Model_Type.gptq
    elif "ggml" in model_name.lower():
        return Model_Type.ggml
    else:
        return Model_Type.full_precision

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def initialize_gpu_model_and_tokenizer(model_name, model_type):
    if model_type == Model_Type.gptq:
        model = AutoGPTQForCausalLM.from_quantized(model_name, device_map="auto", use_safetensors=True, use_triton=False)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", token=True)
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
    return model, tokenizer

def init_auto_model_and_tokenizer(model_name, model_type, file_name=None):
    model_type = get_model_type(model_name)

    if Model_Type.ggml == model_type:
        models_folder = "./models"
        create_folder_if_not_exists(models_folder)
        file_path = hf_hub_download(repo_id=model_name, filename=file_name, local_dir=models_folder)
        model = Llama(file_path, n_ctx=4096)
        tokenizer = None
    else:
        model, tokenizer = initialize_gpu_model_and_tokenizer(model_name, model_type=model_type)
    return model, tokenizer

def run_ui(model, tokenizer, is_chat_model, model_type, save_history=True):
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")

        conversation_memory = []

        def user(user_message, memory):
            nonlocal conversation_memory
            conversation_memory = memory + [[user_message, None]]
            return "", conversation_memory

        def bot(memory):
            nonlocal conversation_memory
            if is_chat_model:
                instruction = format_to_llama_chat_style(memory)
            else:
                instruction = memory[-1][0]

            memory[-1][1] = ""
            kwargs = dict(temperature=0.6, top_p=0.9)
            try:
                if model_type == Model_Type.ggml:
                    kwargs["max_tokens"] = 512
                    for chunk in model(prompt=instruction, stream=True, **kwargs):
                        token = chunk["choices"][0]["text"]
                        memory[-1][1] += token
                        yield memory
                else:
                    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, Timeout=5)
                    inputs = tokenizer(instruction, return_tensors="pt").to(model.device)
                    kwargs["max_new_tokens"] = 512
                    kwargs["input_ids"] = inputs["input_ids"]
                    kwargs["streamer"] = streamer
                    thread = Thread(target=model.generate, kwargs=kwargs)
                    thread.start()

                    for token in streamer:
                        memory[-1][1] += token
                        yield memory

                if save_history:
                    save_conversation_memory(conversation_memory)
            except ValueError as e:
                if "Requested tokens exceed context window of 4096" in str(e):
                    memory[-1][1] = "Error: Instruction too long to process."
                    yield memory
                else:
                    raise e

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
        clear.click(lambda: None, None, chatbot, queue=False)
    demo.queue()
    demo.launch(share=True, debug=True)

def generate_response_from_memory(memory_folder, models_folder):
    conversation_context = ""

    memory_files = glob.glob(os.path.join(memory_folder, "*.json"))
    for memory_file in memory_files:
        with open(memory_file, "r", encoding="utf-8") as file:
            memory_data = ujson.load(file)  # Use ujson.load instead of json.load
            for dialog in memory_data:
                conversation_context += f"{dialog['user_input']}\n{dialog['model_response']}\n"

    with open(os.path.join(models_folder, "model_name.txt"), "r") as file:
        model_name = file.read().strip()

    aglm_parser = LlamaModel(model_name, models_folder)

    response = aglm_parser.generate_contextual_output(conversation_context)
    return response

def main(model_name=None, file_name=None, save_history=True):
    assert model_name is not None, "model_name argument is missing."

    is_chat_model = 'chat' in model_name.lower()
    model_type = get_model_type(model_name)

    if model_type == Model_Type.ggml:
        assert file_name is not None, "When model_name is provided for a GGML quantized model, file_name argument must also be provided."

    model, tokenizer = init_auto_model_and_tokenizer(model_name, model_type, file_name)
    run_ui(model, tokenizer, is_chat_model, model_type, save_history=save_history)

    memory_folder = "./memory/"
    models_folder = "./models/"
    response = generate_response_from_memory(memory_folder, models_folder)
    print(response)

if __name__ == '__main__':
    fire.Fire(main)
