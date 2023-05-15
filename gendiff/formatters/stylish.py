from gendiff.formatters.constants import *

def build_line(key, status_symbol, value):
    return f"  {status_symbol} {key}: {str(value).lower()}\n"

def handle_status(status, key, value):
    status_mapper = {
        'removed': '-',
        'added': '+',
        'unchanged': ' ',
        'changed': ['-', '+']  # для 'changed' мы имеем два символа статуса
    }
    if status == 'changed':
        return build_line(key, status_mapper[status][0], value['old_value']) + build_line(key, status_mapper[status][1], value['new_value'])
    else:
        return ''.join([build_line(k, status_mapper[status], v) for k, v in value.items()])

def build_stylish(node):
    result = "{\n"
    for key in node:
        if key['status'] in ['removed', 'added', 'unchanged']:
            result += handle_status(key['status'], list(key['value'].keys())[0], key['value'])
        elif key['status'] == 'changed':
            result += handle_status(key['status'], key['key'], key)
    result += "}"
    return(result)
