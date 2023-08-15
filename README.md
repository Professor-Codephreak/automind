# IAML Intelligent Autonomous Machine Learning<br />
"I Am Machine Learning"<br /><br />
project codename = codephreak<br />
project direction = automind automindx<br /><br />
"Professor Codephreak is an expert in machine learning, computer science and computer programming ..."<br />
uiux.py provides Gradio output to local server for local language model interaction<br />
Gradio interacts with html javascript and css <a href="https://www.gradio.app/guides/custom-CSS-and-JS">custom Gradio</a><br />
<a href="https://www.gradio.app/guides/getting-started-with-the-js-client">Gradio Javascript Client</a><br />
Documentation: codephreak = uiux.py + memory.py + automind.py + aglm.py

# User Interface and Interaction (uiux.py)<br />

(uiux.py) provides a user interface using the Gradio library to facilitate user interaction.
This chatbot interface takes the user input, processes it, generating response.
Conversation memory handling to store and manage user instructions and model responses.
Contextual Conversation Management<br />

(automind.py)<br /><br />

(automind.py) provides the mechanism to format and managing conversation history using the format_to_llama_chat_style function.
(automind.py) creates coherent conversation context integrating memory management and with chatbot behavior.
Handling different model types and initialization is based on model name calling the model from the models folder. <br />

(memory.py)<br /><br />

Conversation Memory Management is handled by (memory.py) creating a class DialogEntry to represent individual conversation dialog entries.
A function save_conversation_memory is called to save conversation history as JSON files
Memory is created by storing user instructions and model responses in memory files for context management as .json outputs with a timestamp.<br />

# LLAMA Model Interaction<br />
(aglm.py)<br /><br />

Initializes the LLAMA language model and tokenizer based on the specified models_folder models handling processing and tokenization of conversation context using the LLAMA model then generating contextually relevant responses using the LLAMA model. AUTOMIND uses a LLAMA language model to generate responses based on user instructions and conversation history. (uiux.py) encompasses user interface design, memory management, context handling, and interaction with the language model to create a conversational experience for users.

