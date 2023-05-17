def build_plain(abstraction):
    result = []
    result.extend(tree_parser(abstraction))
    return "\n".join(result)


def add_property(result, path, key, value):
    if isinstance(value, dict):
        result.append(
            f"Property '{path}{key}' was added with value: [complex value]"
        )
    else:
        value_str = stringify(value)
        result.append(
            f"Property '{path}{key}' was added with value: {value_str}"
        )


def remove_property(result, path, key):
    result.append(f"Property '{path}{key}' was removed")


def update_property(result, path, key, old_value, new_value):
    if isinstance(old_value, dict):
        new_value_str = stringify(new_value)
        result.append(
            f"Property '{path}{key}' was updated. From [complex value] to {new_value_str}"
        )
    elif isinstance(new_value, dict):
        old_value_str = stringify(old_value)
        result.append(
            f"Property '{path}{key}' was updated. From {old_value_str} to [complex value]"
        )
    else:
        old_value_str = stringify(old_value)
        new_value_str = stringify(new_value)
        result.append(
            f"Property '{path}{key}' was updated. From {old_value_str} to {new_value_str}"
        )


def process_node(result, key, node, path=""):
    if isinstance(node, dict):
        if "status" in node:
            status = node["status"]
            if status == "unchanged":
                return
            elif status == "added":
                add_property(result, path, key, node["value"])
            elif status == "removed":
                remove_property(result, path, key)
            elif status == "changed":
                old_value = node["old_value"]
                new_value = node["new_value"]
                update_property(result, path, key, old_value, new_value)
        if "value" in node and isinstance(node["value"], dict):
            new_path = f"{path}{key}."
            result.extend(tree_parser(node["value"], path=new_path))


def tree_parser(branch, path=""):
    result = []

    for key, node in branch.items():
        process_node(result, key, node, path)

    return result


def stringify(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
