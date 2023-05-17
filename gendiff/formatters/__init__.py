from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain



def formatter(abstraction, format):
    if format == 'stylish':
        return build_stylish(abstraction)
    elif format == 'plain':
        return build_plain(abstraction)