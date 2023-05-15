import json
import yaml
import os

def parse_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        if file_extension == '.json':
            data = json.load(file)
        elif file_extension in ['.yml', '.yaml']:
            data = yaml.safe_load(file)
        else:
            print(f"Неподдерживаемый формат файла: {file_extension}")
            return None
    return data

