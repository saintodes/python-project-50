from gendiff.formatters.stylish import build_stylish

def formatter(abstraction, format):
    if format == 'stylish':
        return build_stylish(abstraction)