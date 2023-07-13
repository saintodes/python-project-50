import json
import yaml
import os


def parse_data(data, format):
    parsers = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }

    try:
        parser = parsers[format]
    except KeyError:
        raise ValueError(f"Unsupported data format: {format}")
    return parser(data)


def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)

    with open(file_path, "r") as file:
        data = file.read()

    return parse_data(data, file_extension)
