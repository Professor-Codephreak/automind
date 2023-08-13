#memory.py
import os
import pathlib
import time
import ujson

# Define the constant for memory folder
MEMORY_FOLDER = "./memory/"

class DialogEntry:
    def __init__(self, instruction, response):
        self.instruction = instruction
        self.response = response

def save_conversation_memory(memory):
    # Create the folder if it doesn't exist
    if not pathlib.Path(MEMORY_FOLDER).exists():
        pathlib.Path(MEMORY_FOLDER).mkdir(parents=True)

    # Generate a unique filename based on the timestamp
    timestamp = str(int(time.time()))  # Use the current timestamp as the filename
    filename = f"memory_{timestamp}.json"
    memory_file_path = pathlib.Path(MEMORY_FOLDER).joinpath(filename)

    # Format the conversation memory as a list of DialogEntry objects
    memory_records = [DialogEntry(dialog[0], dialog[1]) for dialog in memory]

    # Convert DialogEntry objects to dictionaries
    memory_records_dicts = [{"instruction": entry.instruction, "response": entry.response} for entry in memory_records]

    # Save the memory to the JSON file using ujson
    with open(memory_file_path, "w", encoding="utf-8") as file:
        ujson.dump(memory_records_dicts, file, ensure_ascii=False, indent=2)

    return memory_file_path

def save_conversation_memory(memory):
    # Create the folder if it doesn't exist
    if not pathlib.Path(MEMORY_FOLDER).exists():
        pathlib.Path(MEMORY_FOLDER).mkdir(parents=True)

    # Generate a unique filename based on the timestamp
    timestamp = str(int(time.time()))  # Use the current timestamp as the filename
    filename = f"memory_{timestamp}.json"
    file_path = pathlib.Path(MEMORY_FOLDER).joinpath(filename)

    # Format the conversation memory as a list of dictionaries
    formatted_memory = [{"instruction": dialog[0], "response": dialog[1]} for dialog in memory]

    # Save the memory to the JSON file using ujson
    with open(file_path, "w", encoding="utf-8") as file:
        ujson.dump(formatted_memory, file, ensure_ascii=False, indent=2)

    return file_path
