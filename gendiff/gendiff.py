from gendiff.tree_diff import create_tree_diff
from gendiff.parser import read_file
from gendiff.formatters import formatter


def parse_files_and_generate_diff(file_path_1, file_path_2):
    dict1 = read_file(file_path_1)
    dict2 = read_file(file_path_2)
    return create_tree_diff(dict1, dict2)


def generate_diff(file_path_1, file_path_2, format_name="stylish"):
    valid_formats = ["stylish", "plain", "json"]
    if format_name not in valid_formats:
        raise ValueError(
            f"Invalid format name: '{format_name}'. Valid formats are {valid_formats}."
        )
    tree_diff = parse_files_and_generate_diff(file_path_1, file_path_2)
    result = formatter(tree_diff, format_name)
    return result
