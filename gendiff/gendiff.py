from gendiff.formatters.abstraction import create_abstraction
from gendiff.parser import parse_file
from gendiff.formatters import formatter


def generate_diff(file_path_1, file_path_2, format_name="stylish"):
    dict1 = parse_file(file_path_1)
    dict2 = parse_file(file_path_2)
    abstraction = create_abstraction(dict1, dict2)
    result = formatter(abstraction, format_name)
    return result
