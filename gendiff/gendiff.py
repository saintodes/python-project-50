from gendiff.tree_diff import create_tree_diff
from gendiff.parser import read_file
from gendiff.formatters import formatter


def generate_diff(file_path_1, file_path_2, format_name="stylish"):
    dict1 = read_file(file_path_1)
    dict2 = read_file(file_path_2)
    tree_diff = create_tree_diff(dict1, dict2)
    result = formatter(tree_diff, format_name)
    return result
