# import pytest
# import json

from gendiff.gendiff import generate_diff
# from gendiff.formatters.abstraction import create_abstraction


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
