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
        v_s = stringify(value)  # value string
        result.append(f"Property '{path}{key}' was added with value: {v_s}")


def remove_property(result, path, key):
    result.append(f"Property '{path}{key}' was removed")


def update_property(result, path, key, old_value, new_value):
    if isinstance(old_value, dict):
        nvs = stringify(new_value)  # new value string
        result.append(
            f"Property '{path}{key}' was updated. From [complex value] to {nvs}"
        )
    elif isinstance(new_value, dict):
        ovs = stringify(old_value)  # old value string
        result.append(
            f"Property '{path}{key}' was updated. From {ovs} to [complex value]"
        )
    else:
        ovs = stringify(old_value)
        nvs = stringify(new_value)
        result.append(
            f"Property '{path}{key}' was updated. From {ovs} to {nvs}")


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
