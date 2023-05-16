from gendiff.formatters.constants import *


def create_node(key, value, status):
    return {key: {'value': value, 'status': status}}


def create_abstraction(dict1, dict2):
    result = {}
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    removed_keys = set(dict1.keys()) - set(dict2.keys())
    added_keys = set(dict2.keys()) - set(dict1.keys())
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            child = create_abstraction(value1, value2)
            result.update(create_node(key, child, NESTED))
        elif key in removed_keys:
            result.update(create_node(key, dict1.get(key), REMOVED))
        elif key in added_keys:
            result.update(create_node(key, dict2.get(key), ADDED))
        else:
            if value1 == value2:
                result.update(create_node(key, value1, UNCHANGED))
            else:
                result.update({key: {
                    'old_value': value1,
                    'new_value': value2,
                    'status': CHANGED
                }})
    print(result)
    return result
