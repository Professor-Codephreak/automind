automind.py - AutoMind Formatting Utilities
Overview

The automind.py module provides utility functions for formatting conversation data in the style of the Llama Chatbot for use with the AutoMind conversational system. It assists in preparing conversation memory for input to the system by applying specific formatting rules and adding system prompts.
Functions
format_to_llama_chat_style(memory) -> str

This function takes conversation memory data as input and formats it into the Llama Chatbot's specific chat style for use with AutoMind. The function performs the following steps:

    Prepend the default system prompt to the first instruction.
    Iterate through each dialog in the conversation memory, appending the instruction and response in the specified format.
    Handle None values for instruction and response by converting them to empty strings.
    Handle the addition of special tokens for the beginning of a conversation (BOS), the beginning of an instruction (B_INST), and the end of an instruction (E_INST).
    Handle the addition of the system prompt for the first instruction.
    Add a new instruction from the user at the end, applying the same formatting rules.

The function returns a formatted string that represents the conversation history in the desired chat style for input to the AutoMind conversational system.
Constants

    BOS, EOS: Tokens representing the beginning and end of a sequence.
    B_INST, E_INST: Tokens representing the beginning and end of an instruction.
    B_SYS, E_SYS: Tokens representing the beginning and end of a system prompt.
    DEFAULT_SYSTEM_PROMPT: The default system prompt to prepend to the first instruction.

Usage

    Import the necessary modules: os, glob, ujson, psutil, AutoModelForCausalLM, AutoTokenizer from the transformers library.

    Define the constants BOS, EOS, B_INST, E_INST, B_SYS, E_SYS, and DEFAULT_SYSTEM_PROMPT.

    Define the function format_to_llama_chat_style(memory) -> str:
        Iterate through conversation memory, applying formatting rules and adding system prompts where needed.
        Handle special tokens and formatting for instructions and responses.
        Return the formatted conversation history as a string.

Example Use Case

The automind.py module can be utilized within a conversational system to prepare conversation memory for input to AutoMind and AUTOMINDx engine. By formatting conversation data in the specific chat style of the Llama Chatbot, the system ensures that memory data is properly structured and enhanced with system prompts, ready for use in generating context-aware responses within the AutoMind environment.
