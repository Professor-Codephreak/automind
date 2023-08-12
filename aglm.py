#aglm.py
import os
import glob
import ujson
import psutil
from transformers import AutoModelForCausalLM, AutoTokenizer
from automind import format_to_llama_chat_style


class LlamaModel:
    def __init__(self, model_name, models_folder):
        self.model_name = model_name
        self.models_folder = models_folder
        self.model, self.tokenizer = self.initialize_model()

    def initialize_model(self):
        model_path = os.path.join(self.models_folder, self.model_name)
        model = AutoModelForCausalLM.from_pretrained(model_path, device="cuda")
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        return model, tokenizer

    def generate_contextual_output(self, conversation_context):
        formatted_context = format_to_llama_chat_style(conversation_context)
        inputs = self.tokenizer(formatted_context, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(input_ids=inputs.input_ids)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

def determine_batch_size():
    total_memory = psutil.virtual_memory().available
    default_batch_size = 10
    max_memory_usage = 2e9  # Adjust based on your system's available memory
    adjusted_batch_size = int(total_memory / max_memory_usage) * default_batch_size
    return max(default_batch_size, adjusted_batch_size)

def main():
    models_folder = "./models/"
    memory_folder = "./memory/"  # Specify the folder where memory data is stored
    conversation_context = ""

    memory_files = glob.glob(os.path.join(memory_folder, "*.json"))
    batch_size = determine_batch_size()
    for batch_start in range(0, len(memory_files), batch_size):
        batch_files = memory_files[batch_start:batch_start + batch_size]
        for memory_file in batch_files:
            with open(memory_file, "r", encoding="utf-8") as file:
                memory_data = ujson.load(file)
                for dialog in memory_data:
                    conversation_context += f"{dialog['user_input']}\n{dialog['model_response']}\n"

    model_name_path = os.path.join(models_folder, "model_name.txt")
    with open(model_name_path, "r") as file:
        model_name = file.read().strip()

    aglm_parser = LlamaModel(model_name, models_folder)

    response = aglm_parser.generate_contextual_output(conversation_context)
    print(response)

if __name__ == '__main__':
    main()
