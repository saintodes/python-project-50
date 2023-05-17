INDENT_LENGTH = 4
SIGN_LENGTH = 2


def build_stylish(abstraction):
    result = ["{\n"]
    result.extend(tree_parser(abstraction, 1))
    result.append("}")
    return "".join(result)


def tree_parser(branch, level):
    indent_space = " " * (INDENT_LENGTH * level)
    indent_space_minus_sign = " " * ((INDENT_LENGTH * level) - SIGN_LENGTH)
    result = []
    for key, node in sorted(branch.items()):
        if node["status"] == "unchanged":
            result.append(f"{indent_space}{key}: {node['value']}\n")
        elif node["status"] == "added":
            result.append(
                f"{indent_space_minus_sign}+ {key}: {format_value(node['value'], level)}\n"
            )
        elif node["status"] == "removed":
            result.append(
                f"{indent_space_minus_sign}- {key}: {format_value(node['value'], level)}\n"
            )
        elif node["status"] == "changed":
            result.append(
                f"{indent_space_minus_sign}- {key}: {format_value(node['old_value'], level)}\n"
            )
            result.append(
                f"{indent_space_minus_sign}+ {key}: {format_value(node['new_value'], level)}\n"
            )
        elif node["status"] == "nested":
            result.append(f"{indent_space}{key}: {{\n")
            result.extend(tree_parser(node["value"], level + 1))
            result.append(f"{indent_space}}}\n")
    return result


def format_value(value, level):
    if isinstance(value, dict):
        indent_space = " " * (INDENT_LENGTH)
        formatted_value = ["{\n"]
        for key, val in value.items():
            formatted_value.append(
                f"{indent_space * (level + 1)}{key}: {format_value(val, level +1)}\n"
            )
        formatted_value.append(f"{indent_space * level}}}")
        return "".join(formatted_value)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)
