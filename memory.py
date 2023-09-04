import os
import pathlib
import time
import ujson
import logging

# Define the constant for memory folder
MEMORY_FOLDER = "./memory/"

# Initialize logging
logging.basicConfig(level=logging.INFO)

class DialogEntry:
    def __init__(self, instruction, response):
        self.instruction = instruction
        self.response = response

    def to_dict(self):
        return {
            "instruction": self.instruction,
            "response": self.response
        }

def save_conversation_memory(memory):
    try:
        # Create the folder if it doesn't exist
        folder_path = pathlib.Path(MEMORY_FOLDER)
        if not folder_path.exists():
            folder_path.mkdir(parents=True, mode=0o700)  # Secure folder permissions

        # Generate a unique filename based on the timestamp
        timestamp = str(int(time.time()))
        filename = f"memory_{timestamp}.json"
        file_path = folder_path.joinpath(filename)

        # Format the conversation memory as DialogEntry objects
        formatted_memory = [DialogEntry(dialog[0], dialog[1]).to_dict() for dialog in memory]

        # Save the memory to the JSON file using ujson
        with open(file_path, "w", encoding="utf-8") as file:
            ujson.dump(formatted_memory, file, ensure_ascii=False, indent=2)

        # Secure file permissions
        os.chmod(file_path, 0o600)

        return file_path

    except Exception as e:
        logging.error(f"An error occurred while saving the conversation memory: {e}")
        return None
