import pytest
from StringUtils import StringUtils


@pytest.fixture


def string_utils():
    return StringUtils()


def test_capitalize_positive(string_utils: StringUtils):
    assert string_utils.capitalize("positive") == "Positive"
    assert string_utils.capitalize("example") == "Example"
    assert string_utils.capitalize("") == ""


def test_capitalize_negative(string_utils: StringUtils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)
    with pytest.raises(TypeError):
        string_utils.capitalize(555)


def test_trim_positive(string_utils: StringUtils):
    assert string_utils.trim("  positive") == "positive"
    assert string_utils.trim(" example ") == "example "
    assert string_utils.trim("") == ""


def test_trim_negative(string_utils: StringUtils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)
    with pytest.raises(TypeError):
        string_utils.trim(123)


def test_to_list_positive(string_utils: StringUtils):
    assert string_utils.to_list("f, g, r, y") == ["f", "g", "r", "y"]
    assert string_utils.to_list("8:6:7", ":") == ["8", "6", "7"]
    assert string_utils.to_list("", ",") == []


def test_to_list_negative(string_utils: StringUtils):
    with pytest.raises(AttributeError):
        string_utils.to_list(None)
    with pytest.raises(TypeError):
        string_utils.to_list(123)


def test_contains_positive(string_utils: StringUtils):
    assert string_utils.contains("positive", "p") is True
    assert string_utils.contains("example", "e") is True
    assert string_utils.contains("", "") is False


def test_contains_negative(string_utils: StringUtils):
    assert string_utils.contains("positive", "u") is False
    assert string_utils.contains("", "p") is False
    with pytest.raises(TypeError):
        string_utils.contains(123, "p")
    with pytest.raises(AttributeError):
        string_utils.contains(None, "p")


def test_delete_symbol_positive(string_utils: StringUtils):
    assert string_utils.delete_symbol("positive", "s") == "poitive"
    assert string_utils.delete_symbol("example", "e") == "xampl"
    assert string_utils.delete_symbol("", "") == ""


def test_delete_symbol_negative(string_utils: StringUtils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "i")
    with pytest.raises(TypeError):
        string_utils.delete_symbol(123, "i")


def test_starts_with_positive(string_utils: StringUtils):
    assert string_utils.starts_with("Positive", "P") is True
    assert string_utils.starts_with("example", "e") is True
    assert string_utils.starts_with("", "") is False


def test_starts_with_negative(string_utils: StringUtils):
    assert string_utils.starts_with("Positive", "S") is False
    assert string_utils.starts_with("", "l") is False
    with pytest.raises(TypeError):
        string_utils.starts_with(123, "l")
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, "l")


def test_end_with_positive(string_utils: StringUtils):
    assert string_utils.end_with("Positive", "e") is True
    assert string_utils.end_with("example", "e") is True
    assert string_utils.end_with("", "") is False


def test_end_with_negative(string_utils: StringUtils):
    assert string_utils.end_with("Positive", "y") is False
    assert string_utils.end_with("", "h") is False
    with pytest.raises(TypeError):
        string_utils.end_with(123, "h")
    with pytest.raises(AttributeError):
        string_utils.end_with(None, "h")


def test_is_empty_positive(string_utils: StringUtils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty("  ") is True
    assert string_utils.is_empty("\t\n\r") is True


def test_is_empty_negative(string_utils: StringUtils):
    assert string_utils.is_empty("Positive") is False
    assert string_utils.is_empty(" ") is False
    assert string_utils.is_empty("Not empty") is False


def test_list_to_string_positive(string_utils: StringUtils):
    assert string_utils.list_to_string([5, 6, 7, 8], ", ") == "5, 6, 7, 8"
    assert string_utils.list_to_string(["Sky", "pro"], ", ") == "Sky, pro"
    assert string_utils.list_to_string(["Sky", "pro"], "-") == "Sky-pro"
    assert string_utils.list_to_string([], ", ") == ""


def test_list_to_string_negative(string_utils: StringUtils):
    with pytest.raises(TypeError):
        string_utils.list_to_string("not a list", ",")
    with pytest.raises(ValueError):
        string_utils.list_to_string([1, "two", 3], ",")


pytest
