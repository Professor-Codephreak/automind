This build will experience a 4096 memory input too large error with pasting of a large prompt into the UI<br /><br />
ongoing development of Professor Codephreak LLM <a href="https://github.com/pythaiml/automindx">here</a>


This Professor Codephreak build is being left intact as the first example of the working aGLM prototype</b>
Work continues at <a href="https://github.com/pythaiml/automindx">automindx</a> as the next evolution of Professor Codephreak's core intention value and success creating <a href="https://automindx.dmg.finance">AUTOMINDx</a><br />


# IAML Intelligent Autonomous Machine Learning<br />
"I Am Machine Learning"<br /><br />
project codename = codephreak<br />
project direction = automind <a href="https://github.com/automindx">automindx</a><br /><br />
"Professor Codephreak is an expert in machine learning, computer science and computer programming ..."<br />
uiux.py provides Gradio output to local server for local language model interaction<br />
Gradio interacts with html javascript and css <a href="https://www.gradio.app/guides/custom-CSS-and-JS">custom Gradio</a><br />
<a href="https://www.gradio.app/guides/getting-started-with-the-js-client">Gradio Javascript Client</a><br />
Documentation: codephreak = uiux.py + memory.py + automind.py + aglm.py<br />

# User Interface and Interaction (uiux.py)<br />

(uiux.py) provides a user interface using the Gradio library to facilitate user interaction.
This chatbot interface takes the user input, processes it, generating response includingc onversation memory handling storing and managing user instructions and model responses. The result is a local language model prompted to run as "Professor Codephreak is an expert in computer programming ....." that refers to itself as "codephreak"
Contextual Conversation Management<br />

(automind.py) provides the mechanism to format and managing conversation history using the format_to_llama_chat_style function.
(automind.py) creates coherent conversation context integrating memory management and with chatbot behavior.
Handling different model types and initialization is based on model name calling the model from the models folder. <br />

(memory.py) handles Conversation Memory Management by  creating a class DialogEntry to represent individual conversation dialog entries.
A function save_conversation_memory is called to save conversation history as JSON files. Memory is created by storing user instructions and model responses in memory files for context management as .json outputs with a timestamp.<br />

# LLAMA Model Interaction<br />
(aglm.py)<br />

Initializes the LLAMA language model and tokenizer based on the specified models_folder models handling processing and tokenization of conversation context using the LLAMA model then generating contextually relevant responses using the LLAMA model. AUTOMIND uses a LLAMA language model to generate responses based on user instructions and conversation history. (uiux.py) encompasses user interface design, memory management, context handling, and interaction with the language model to create a conversational experience for users.<br />

-----------------------------------

## [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)

To install right click "Save link as ..." [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install) chmod +x automind.install && automind.install

details and verbose procedure
1. Right-click the following link: [automind.install](https://raw.githubusercontent.com/Professor-Codephreak/automind/main/automind.install)
2. Choose "Save link as..." or "Download linked file" from the context menu.
3. Select a location on your computer to save the file.
4. from the terminal
5. chmod +x automind.install && ./automind.install


---------------------------------
<br />

# RUN codephreak<br />

```bash
python3 uiux.py --model_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --tokenizer_name="TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGML" --model_type="ggml" --save_history --file_name="llama-2-7b-chat-codeCherryPop.ggmlv3.q4_1.bin"
```
