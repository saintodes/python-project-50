# import pytest
# import json
from gendiff.tree_diff import create_node, create_tree_diff
from gendiff.formatters.constants import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED
from gendiff.gendiff import generate_diff


def test_stylish_flat():
    json_dict1 = "tests/fixtures/flat/file1.json"
    json_dict2 = "tests/fixtures/flat/file2.json"
    flat_result = "tests/fixtures/flat/expected_diff.txt"

    assert (
        generate_diff(json_dict1, json_dict2, "stylish")
        == open(flat_result, "r").read()
    )

    yml_dict1 = "tests/fixtures/flat/file1.yml"
    yml_dict2 = "tests/fixtures/flat/file2.yml"

    assert (
        generate_diff(yml_dict1, yml_dict2, "stylish")
        == open(flat_result, "r").read()
    )


def test_stylish_nested():
    json_dict1 = "tests/fixtures/nested/file1.json"
    json_dict2 = "tests/fixtures/nested/file2.json"
    nested_result = "tests/fixtures/nested/nested_expected.txt"

    assert (
        generate_diff(json_dict1, json_dict2, "stylish")
        == open(nested_result, "r").read()
    )

    yml_dict1 = "tests/fixtures/nested/file1.yml"
    yml_dict2 = "tests/fixtures/nested/file2.yml"

    assert (
        generate_diff(yml_dict1, yml_dict2, "stylish")
        == open(nested_result, "r").read()
    )


def test_plain_nested():
    json_dict1 = "tests/fixtures/nested/file1.json"
    json_dict2 = "tests/fixtures/nested/file2.json"
    nested_result = "tests/fixtures/plain/plain_expected.txt"

    assert (
        generate_diff(json_dict1, json_dict2, "plain")
        == open(nested_result, "r").read()
    )

    yml_dict1 = "tests/fixtures/nested/file1.yml"
    yml_dict2 = "tests/fixtures/nested/file2.yml"

    assert (
        generate_diff(yml_dict1, yml_dict2, "plain")
        == open(nested_result, "r").read()
    )


def test_json_nested():
    json_dict1 = "tests/fixtures/nested/file1.json"
    json_dict2 = "tests/fixtures/nested/file2.json"
    nested_result = "tests/fixtures/to_json/json_expected.txt"

    assert (
        generate_diff(json_dict1, json_dict2, "json")
        == open(nested_result, "r").read()
    )

    yml_dict1 = "tests/fixtures/nested/file1.yml"
    yml_dict2 = "tests/fixtures/nested/file2.yml"

    assert (
        generate_diff(yml_dict1, yml_dict2, "json")
        == open(nested_result, "r").read()
    )


def test_create_node():
    key = "test"
    value = "value"
    status = "status"
    expected = {key: {"value": value, "status": status}}
    assert create_node(key, value, status) == expected


def test_create_tree_diff_unchanged():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = {"key1": "value1", "key2": "value2"}
    expected = {
        "key1": {"value": "value1", "status": UNCHANGED},
        "key2": {"value": "value2", "status": UNCHANGED},
    }
    assert create_tree_diff(dict1, dict2) == expected


def test_create_tree_diff_added():
    dict1 = {"key1": "value1"}
    dict2 = {"key1": "value1", "key2": "value2"}
    expected = {
        "key1": {"value": "value1", "status": UNCHANGED},
        "key2": {"value": "value2", "status": ADDED},
    }
    assert create_tree_diff(dict1, dict2) == expected


def test_create_tree_diff_removed():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = {"key1": "value1"}
    expected = {
        "key1": {"value": "value1", "status": UNCHANGED},
        "key2": {"value": "value2", "status": REMOVED},
    }
    assert create_tree_diff(dict1, dict2) == expected


def test_create_tree_diff_changed():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = {"key1": "value1", "key2": "value3"}
    expected = {
        "key1": {"value": "value1", "status": UNCHANGED},
        "key2": {"old_value": "value2", "new_value": "value3", "status": CHANGED},
    }
    assert create_tree_diff(dict1, dict2) == expected


def test_create_tree_diff_nested():
    dict1 = {"key1": {"subkey1": "value1"}, "key2": "value2"}
    dict2 = {"key1": {"subkey1": "value1"}, "key2": "value3"}
    expected = {
        "key1": {
            "value": {"subkey1": {"value": "value1", "status": UNCHANGED}},
            "status": NESTED,
        },
        "key2": {"old_value": "value2", "new_value": "value3", "status": CHANGED},
    }
    assert create_tree_diff(dict1, dict2) == expected
