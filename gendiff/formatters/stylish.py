INDENT_LENGTH = 4
SIGN_LENGTH = 2


def format_dict(value, level):
    ind_space = " " * (INDENT_LENGTH)
    formatted_value = ["{\n"]
    formatted_value.extend(
        f"{ind_space * (level + 1)}{key}: {format_val(val, level + 1)}" f"\n"
        for key, val in value.items()
    )
    formatted_value.append(f"{ind_space * level}}}")
    return "".join(formatted_value)


def format_val(value, level):
    if isinstance(value, dict):
        return format_dict(value, level)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def format_status_unchanged(node, key, indentation, level):
    return [f"{indentation}{key}: {format_val(node['value'], level)}\n"]


def format_status_added(node, key, indentation, level):
    ind_min_s = indentation[:-SIGN_LENGTH]
    return [f"{ind_min_s}+ {key}: {format_val(node['value'], level)}\n"]


def format_status_removed(node, key, indentation, level):
    ind_min_s = indentation[:-SIGN_LENGTH]
    return [f"{ind_min_s}- {key}: {format_val(node['value'], level)}\n"]


def format_status_changed(node, key, indentation, level):
    ind_min_s = indentation[:-SIGN_LENGTH]
    return [
        f"{ind_min_s}- {key}: {format_val(node['old_value'], level)}\n",
        f"{ind_min_s}+ {key}: {format_val(node['new_value'], level)}\n",
    ]


def format_status_nested(node, key, indentation, level):
    return (
        [f"{indentation}{key}: {{\n"]
        + tree_parser(node["value"], level + 1)
        + [f"{indentation}}}\n"]
    )


STATUS_FUNCTIONS = {
    "unchanged": format_status_unchanged,
    "added": format_status_added,
    "removed": format_status_removed,
    "changed": format_status_changed,
    "nested": format_status_nested,
}


def tree_parser(branch, level):
    indentation = " " * (INDENT_LENGTH * level)

    result = [
        STATUS_FUNCTIONS.get(node["status"], lambda *args: [])(
            node, key, indentation, level
        )
        for key, node in sorted(branch.items())
    ]
    return [item for sublist in result for item in sublist]


def stylish_format(tree_diff):
    return "{\n" + "".join(tree_parser(tree_diff, 1)) + "}"
