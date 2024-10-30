import json
import os
from typing import Any

class DataStorage:
    def __init__(self, file_name="data.json"):
        self.file_name = file_name
        self.file_path = os.path.join(os.getcwd(), self.file_name)

    def save_data(self, data: Any, key: str) -> None:
        """Save data under a specific key in the JSON file."""
        existing_data = self.load_data()
        existing_data[key] = data
        with open(self.file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)

    def load_data(self) -> dict:
        """Load all data from the JSON file."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def retrieve_data(self, key: str) -> Any:
        """Retrieve data for a specific key from the JSON file."""
        data = self.load_data()
        return data.get(key, {})

    def append_data(self, data: Any, key: str) -> None:
        """Append data under a specific key in the JSON file."""
        existing_data = self.load_data().get(key, [])
        if not isinstance(existing_data, list):
            raise ValueError(f"Cannot append to non-list key: {key}")
        existing_data.append(data)
        self.save_data(existing_data, key)

    def remove_data(self, key: str) -> None:
        """Remove data associated with a key from the JSON file."""
        data = self.load_data()
        if key in data:
            del data[key]
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
