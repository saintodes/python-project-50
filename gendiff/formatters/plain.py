def build_plain(abstraction):
    result = []
    result.extend(tree_parser(abstraction))
    return "\n".join(result)

def tree_parser(branch, path=""):
    result = []
    for key, node in branch.items():
        if isinstance(node, dict):  
            if 'status' in node:
                if node['status'] == 'unchanged':
                    continue
                if node['status'] == 'added':
                    if isinstance(node['value'], dict):
                        result.append(f"Property '{path}{key}' was added with value: [complex value]")
                        continue
                    value_str = stringify(node['value'])
                    result.append(f"Property '{path}{key}' was added with value: {value_str}")
                elif node['status'] == 'removed':
                    result.append(f"Property '{path}{key}' was removed")
                elif node['status'] == 'changed':
                    old_value = "[complex value]" if isinstance(node['old_value'], dict) else stringify(node['old_value'])
                    new_value = "[complex value]" if isinstance(node['new_value'], dict) else stringify(node['new_value'])
                    result.append(f"Property '{path}{key}' was updated. From {old_value} to {new_value}")
            if 'value' in node and isinstance(node['value'], dict):
                result.extend(tree_parser(node['value'], path=path + key + '.'))
    return result

def stringify(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)

