from gendiff.formatters.constants import (
    ADDED,
    REMOVED,
    CHANGED,
    UNCHANGED,
    NESTED,
)


def create_node(key, value, status):
    return {key: {"value": value, "status": status}}


def handle_nested(dict1, dict2, key, result):
    child = create_tree_diff(dict1.get(key), dict2.get(key))
    result.update(create_node(key, child, NESTED))


def handle_removed(dict1, key, result):
    result.update(create_node(key, dict1.get(key), REMOVED))


def handle_added(dict2, key, result):
    result.update(create_node(key, dict2.get(key), ADDED))


def handle_changed(dict1, dict2, key, result):
    result.update(
        {
            key: {
                "old_value": dict1.get(key),
                "new_value": dict2.get(key),
                "status": CHANGED,
            }
        }
    )


def handle_unchanged(dict1, key, result):
    result.update(create_node(key, dict1.get(key), UNCHANGED))


def create_tree_diff(dict1, dict2):
    result = {}
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    removed_keys = set(dict1.keys()) - set(dict2.keys())
    added_keys = set(dict2.keys()) - set(dict1.keys())
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            handle_nested(dict1, dict2, key, result)
        elif key in removed_keys:
            handle_removed(dict1, key, result)
        elif key in added_keys:
            handle_added(dict2, key, result)
        else:
            if value1 == value2:
                handle_unchanged(dict1, key, result)
            else:
                handle_changed(dict1, dict2, key, result)
    return result
