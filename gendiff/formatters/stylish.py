INDENT_LENGTH = 4
SIGN_LENGTH = 2


def build_stylish(abstraction):
    result = ["{\n"]
    result.extend(tree_parser(abstraction, 1))
    result.append("}")
    return "".join(result)


def unchanged(node, key, ind_s, ind_min_s, level):
    return [f"{ind_s}{key}: {node['value']}\n"]


def added(node, key, ind_s, ind_min_s, level):
    return [f"{ind_min_s}+ {key}: {format_val(node['value'], level)}\n"]


def removed(node, key, ind_s, ind_min_s, level):
    return [f"{ind_min_s}- {key}: {format_val(node['value'], level)}\n"]


def changed(node, key, ind_s, ind_min_s, level):
    return [
        f"{ind_min_s}- {key}: {format_val(node['old_value'], level)}\n",
        f"{ind_min_s}+ {key}: {format_val(node['new_value'], level)}\n",
    ]


def nested(node, key, ind_s, ind_min_s, level):
    return (
        [f"{ind_s}{key}: {{\n"]
        + tree_parser(node["value"], level + 1)
        + [f"{ind_s}}}\n"]
    )


def tree_parser(branch, level):
    status_func_map = {
        "unchanged": unchanged,
        "added": added,
        "removed": removed,
        "changed": changed,
        "nested": nested,
    }

    # indend space
    ind_s = " " * (INDENT_LENGTH * level)
    # indend space minus sign
    ind_min_s = " " * ((INDENT_LENGTH * level) - SIGN_LENGTH)

    result = []
    for key, node in sorted(branch.items()):
        func = status_func_map.get(node["status"])
        if func:
            result.extend(func(node, key, ind_s, ind_min_s, level))
    return result


def format_val(value, level):
    if isinstance(value, dict):
        ind_space = " " * (INDENT_LENGTH)
        formatted_value = ["{\n"]
        for key, val in value.items():
            formatted_value.append(
                f"{ind_space * (level + 1)}{key}: {format_val(val, level +1)}\n"
            )
        formatted_value.append(f"{ind_space * level}}}")
        return "".join(formatted_value)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)
