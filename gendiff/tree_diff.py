from gendiff.formatters.constants import (
    ADDED,
    REMOVED,
    CHANGED,
    UNCHANGED,
    NESTED,
)


def create_node(key, value, status):
    return {key: {"value": value, "status": status}}


def handle_nested(dict1, dict2, key):
    child = create_tree_diff(dict1.get(key), dict2.get(key))
    return create_node(key, child, NESTED)


def handle_removed(dict1, key):
    return create_node(key, dict1.get(key), REMOVED)


def handle_added(dict2, key):
    return create_node(key, dict2.get(key), ADDED)


def handle_changed(dict1, dict2, key):
    return {
        key: {
            "old_value": dict1.get(key),
            "new_value": dict2.get(key),
            "status": CHANGED,
        }
    }


def handle_unchanged(dict1, key):
    return create_node(key, dict1.get(key), UNCHANGED)


def generate_diff_keys(dict1, dict2):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    removed_keys = set(dict1.keys()) - set(dict2.keys())
    added_keys = set(dict2.keys()) - set(dict1.keys())
    return all_keys, removed_keys, added_keys


def handle_key(dict1, dict2, key, removed_keys, added_keys):
    result = None

    if key in removed_keys:
        result = handle_removed(dict1, key)
    elif key in added_keys:
        result = handle_added(dict2, key)
    elif isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
        result = handle_nested(dict1, dict2, key)
    elif dict1.get(key) == dict2.get(key):
        result = handle_unchanged(dict1, key)
    else:
        result = handle_changed(dict1, dict2, key)

    return result


def handle_keys(dict1, dict2, all_keys, removed_keys, added_keys):
    result = {}
    for key in all_keys:
        result.update(handle_key(dict1, dict2, key, removed_keys, added_keys))
    return result


def create_tree_diff(dict1, dict2):
    all_keys, removed_keys, added_keys = generate_diff_keys(dict1, dict2)
    return handle_keys(dict1, dict2, all_keys, removed_keys, added_keys)
