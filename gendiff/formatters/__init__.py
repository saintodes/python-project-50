from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain
from gendiff.formatters.json import build_json


def formatter(abstraction, format):
    if format == "stylish":
        return build_stylish(abstraction)
    elif format == "plain":
        return build_plain(abstraction)
    elif format == "json":
        return build_json(abstraction)
