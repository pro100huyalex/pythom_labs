import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from text import normalize, tokenize, count_freq, top_n

# ТЕСТ 1: normalize
def test_normalize_basic():
    """Базовые случаи для normalize"""
    assert normalize("Привет МИР") == "привет мир"
    assert normalize("  ПРОБЕЛЫ  ") == "пробелы"
    assert normalize("") == ""

def test_normalize_edge_cases():
    """Граничные случаи"""
    assert normalize("   ") == ""
    assert normalize("a" * 100) == "a" * 100
    assert normalize("СоВсЕм ДРУГой РеГИстр") == "совсем другой регистр"

# Параметризованный тест для normalize
@pytest.mark.parametrize("input_text, expected", [
    ("Hello", "hello"),
    ("  TEST  ", "test"),
    ("Много   пробелов", "много   пробелов"),
    ("", ""),
    ("123", "123"),
])
def test_normalize_parametrized(input_text, expected):
    assert normalize(input_text) == expected

# ТЕСТ 2: tokenize
def test_tokenize_basic():
    """Базовые случаи для tokenize"""
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("один, два. три!") == ["один", "два", "три"]

def test_tokenize_empty():
    """Пустые строки"""
    assert tokenize("") == []
    assert tokenize("   ") == []
    assert tokenize(".,!") == []

def test_tokenize_special_chars():
    """Спецсимволы"""
    assert tokenize("word-with-hyphens") == ["word-with-hyphens"]
    assert tokenize("email@example.com") == ["email@example.com"]
    assert tokenize("(скобки) [и] {фигурные}") == ["скобки", "и", "фигурные"]

# ТЕСТ 3: count_freq
def test_count_freq_basic():
    """Базовые случаи для count_freq"""
    tokens = ["я", "люблю", "питон", "питон"]
    result = count_freq(tokens)
    assert result == {"я": 1, "люблю": 1, "питон": 2}

def test_count_freq_empty():
    """Пустой список"""
    assert count_freq([]) == {}

def test_count_freq_repeats():
    """Повторы"""
    tokens = ["а", "а", "а", "б", "б"]
    result = count_freq(tokens)
    assert result["а"] == 3
    assert result["б"] == 2

# ТЕСТ 4: top_n
def test_top_n_basic():
    """Базовые случаи для top_n"""
    freq = {"я": 3, "люблю": 5, "питон": 2}
    result = top_n(freq, 2)
    assert result == [("люблю", 5), ("я", 3)]

def test_top_n_equal_frequency():
    """Проверка сортировки по алфавиту при равной частоте"""
    freq = {"яблоко": 3, "апельсин": 3, "банан": 5, "вишня": 3}
    result = top_n(freq, 4)
    assert result == [("банан", 5), ("апельсин", 3), ("вишня", 3), ("яблоко", 3)]

def test_top_n_edge_cases():
    """Граничные случаи для top_n"""
    assert top_n({"а": 1}, 10) == [("а", 1)]
    assert top_n({"а": 1, "б": 2}, 0) == []
    assert top_n({}, 5) == []
    assert top_n({"а": 1}, -1) == []
def test_full_chain():
    """Тест всей цепочки функций"""
    text = "Привет мир! Мир прекрасен. Привет всем."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, 2)
    
    assert normalized == "привет мир! мир прекрасен. привет всем."
    assert tokens == ["привет", "мир", "мир", "прекрасен", "привет", "всем"]
    assert freq == {"привет": 2, "мир": 2, "прекрасен": 1, "всем": 1}
    assert top == [("мир", 2), ("привет", 2)]