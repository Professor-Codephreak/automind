# IAML Intelligent Autonomous Machine Learning<br />
"I Am Machine Learning"<br /><br />
project codename = codephreak<br />
project direction = automind automindx<br /><br />
"Professor Codephreak is an expert in machine learning, computer science and computer programming ..."<br />
uiux.py provides Gradio output to local server for local language model interaction<br />
Gradio interacts with html javascript and css <a href="https://www.gradio.app/guides/custom-CSS-and-JS">custom Gradio</a><br />
<a href="https://www.gradio.app/guides/getting-started-with-the-js-client">Gradio Javascript Client</a><br />
Documentation: codephreak = uiux.py + memory.py + automind.py + aglm.py

# User Interface and Interaction (uiux.py):

A user interface using the Gradio library to facilitate user interaction.
A chatbot interface that takes user input, processes it, and generates responses.
Conversation memory handling to store and manage user instructions and model responses.
Contextual Conversation Management (automind.py):

A mechanism for formatting and managing conversation history using the format_to_llama_chat_style function.
Integration of memory management and chatbot behavior to maintain a coherent conversation context.
Handling different model types and initialization based on model names.
Conversation Memory Management (memory.py):

A class DialogEntry to represent individual conversation dialog entries.
A function save_conversation_memory to save conversation history to JSON files.
Storing user instructions and model responses in memory files for context management.
LLAMA Model Interaction (aglm.py):

Initialization of a LLAMA language model and tokenizer based on a specified models_folder.
Processing and tokenization of conversation context using the LLAMA model.
Generating contextually relevant responses using the LLAMA model.
AUTOMIND uses a LLAMA language model to generate responses based on user instructions and conversation history. automind encompasses user interface design, memory management, context handling, and interaction with the language model to create a conversational experience for users.

