import pytest
from src.security import validate_tool

def test_tool_allowlist_valid():
    validate_tool("predict")

def test_tool_allowlist_invalid():
    with pytest.raises(ValueError):
        validate_tool("rm -rf")

def test_tool_allowlist_another_invalid():
    with pytest.raises(ValueError):
        validate_tool("delete_all_data")


def test_threshold_valid():
    threshold = 0.5
    assert 0 <= threshold <= 1

def test_threshold_invalid():
    threshold = 2
    assert not (0 <= threshold <= 1)
