import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тест 1

@pytest.mark.positive
@pytest.mark.parametrize("input_string,expected", [("python", "Python"),
                                                   ("java", "Java"),
                                                   ("giga_chat", "Giga_chat")])
def test_capitalize_positive(input_string, expected):
    assert string_utils.capitalize(input_string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string,expected", [("333python", "333python"),
                                                   (",", ","),
                                                   ("  ", "  ")])
def test_capitalize_negative(input_string, expected):
    assert string_utils.capitalize(input_string) == expected


# Тест 2

@pytest.mark.positive
@pytest.mark.parametrize("input_string,expected", [("  python.", "python."),
                                                   (" 123", "123"),
                                                   (" .", ".")])
def test_trim_positive(input_string, expected):
    assert string_utils.trim(input_string) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_string,expected", [("222", "222"),
                                                   (".", "."),
                                                   ("", "")])
def test_trim_negative(input_string, expected):
    assert string_utils.trim(input_string) == expected

# Тест 3

@pytest.mark.positive
@pytest.mark.parametrize("input_string, simbol, res", [("Pip", "P", True),
                                                  ("Giga", "g", True),
                                                  ("java", "v", True)])
def test_contains_positive(input_string, simbol, res):
    result = string_utils.contains(input_string, simbol)
    assert result == res

@pytest.mark.negative
@pytest.mark.parametrize("input_string, simbol, res", [("Pip", "y", False),
                                                  ("Giga", "M", False),
                                                  ("java", "u", False)])
def test_contains_negative(input_string, simbol, res):
    result = string_utils.contains(input_string, simbol)
    assert result == res

# Тест 4

@pytest.mark.positive
@pytest.mark.parametrize("input_string, delete_symbol, res", [("GigaChat3", "Chat", "Giga3"),
                                                              ("Megatron ", "Mega", "tron "),
                                                              ("Opel.", "Op", "el.")])

def test_delete_symbol_positive(input_string, delete_symbol, res):
    result = string_utils.delete_symbol(input_string, delete_symbol)
    assert result == res

@pytest.mark.negative
@pytest.mark.parametrize("input_string, delete_symbol, res", [("12", ".", "12"),
                                                              ("Lop", "pol", "Lop"),
                                                              ("Opel.", "oPEL", "Opel.")])
def test_delete_symbol_negative(input_string, delete_symbol, res):
    result = string_utils.delete_symbol(input_string, delete_symbol)
    assert result == res