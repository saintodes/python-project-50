import pytest

from gendiff.scripts.gendiff import generate_diff_from_files


@pytest.fixture
def file1():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file2():
    return "tests/fixtures/file2.json"


@pytest.fixture
def flatten_expected():
    with open("tests/fixtures/expected_diff.txt") as f:
        return f.read()


def test_flatten_diff(file1, file2, flatten_expected):
    assert generate_diff_from_files(file1, file2) == flatten_expected
