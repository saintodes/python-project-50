import pytest
import json

from gendiff.gendiff import generate_diff
from gendiff.formatters.abstraction import create_abstraction


def test_stylish_plain():
    json_dict1 = 'tests/fixtures/plain/file1.json'
    json_dict2 = 'tests/fixtures/plain/file2.json'
    plain_result = 'tests/fixtures/plain/plain_expected.txt'

    assert generate_diff(json_dict1, json_dict2, 'stylish') == open(plain_result, 'r').read()

    yml_dict1 = 'tests/fixtures/plain/file1.yml'
    yml_dict2 = 'tests/fixtures/plain/file2.yml'

    assert generate_diff(yml_dict1, yml_dict2, 'stylish') == open(plain_result, 'r').read()


def test_stylish_nested():
    json_dict1 = 'tests/fixtures/nested/file1.json'
    json_dict2 = 'tests/fixtures/nested/file2.json'
    nested_result = 'tests/fixtures/nested/nested_expected.txt'

    assert generate_diff(json_dict1, json_dict2, 'stylish') == open(nested_result, 'r').read()

    yml_dict1 = 'tests/fixtures/nested/file1.yml'
    yml_dict2 = 'tests/fixtures/nested/file2.yml'

    assert generate_diff(yml_dict1, yml_dict2, 'stylish') == open(nested_result, 'r').read()


# def test_plain_abstraction():
#     json_file1 = 'tests/fixtures/plain/file1.json'
#     json_file2 = 'tests/fixtures/plain/file2.json'
#     with open(json_file1, 'r') as f:
#         dict1 = json.load(f)
#     with open(json_file2, 'r') as f:
#         dict2 = json.load(f)
#     expected_result = 'tests/fixtures/plain/expected_plain_abstraction.txt'

#     assert create_abstraction(dict1, dict2) == open(expected_result, 'r').read()


# def test_nested_abstraction():
#     json_file1 = 'tests/fixtures/nested/file1.json'
#     json_file2 = 'tests/fixtures/nested/file2.json'
#     with open(json_file1, 'r') as f:
#         dict1 = json.load(f)
#     with open(json_file2, 'r') as f:
#         dict2 = json.load(f)
#     expected_result = 'tests/fixtures/nested/expexted_nested_abstraction.txt'

#     assert create_abstraction(dict1, dict2) == open(expected_result, 'r').read()


