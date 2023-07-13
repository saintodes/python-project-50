from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import build_plain
from gendiff.formatters.json import build_json


def formatter(tree_diff, format):
    if format == "stylish":
        return stylish_format(tree_diff)
    elif format == "plain":
        return build_plain(tree_diff)
    elif format == "json":
        return build_json(tree_diff)
