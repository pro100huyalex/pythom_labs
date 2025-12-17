import pytest
import json
import csv
from pathlib import Path
from json_csv import json_to_csv, csv_to_json

#  ТЕСТЫ

def test_json_to_csv_basic(tmp_path):
    """Корректная конвертация JSON → CSV"""
    json_file = tmp_path / "test.json"
    json_data = [
        {"name": "Иван", "age": 25, "city": "Москва"},
        {"name": "Мария", "age": 30, "city": "СПб"}
    ]
    json_file.write_text(json.dumps(json_data, ensure_ascii=False), encoding='utf-8')
    
    csv_file = tmp_path / "test.csv"
    json_to_csv(str(json_file), str(csv_file))
    
    assert csv_file.exists()
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert len(rows) == 2

    assert set(rows[0].keys()) == {"name", "age", "city"}

    assert rows[0]["name"] == "Иван"
    assert rows[0]["age"] == "25"  
    assert rows[1]["city"] == "СПб"

def test_csv_to_json_basic(tmp_path):
    """Корректная конвертация CSV → JSON"""
    csv_file = tmp_path / "test.csv"
    csv_content = """name,age,city
Иван,25,Москва
Мария,30,СПб"""
    csv_file.write_text(csv_content, encoding='utf-8')
    json_file = tmp_path / "test.json"
    csv_to_json(str(csv_file), str(json_file))
    assert json_file.exists()
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age", "city"}
    assert data[0]["name"] == "Иван"
    assert data[0]["age"] == "25" 
    assert data[1]["city"] == "СПб"
def test_json_csv_round_trip(tmp_path):
    """Тест туда-обратно: JSON → CSV → JSON"""
    original_data = [
        {"id": 1, "value": "test1"},
        {"id": 2, "value": "test2"}
    ]

    json1 = tmp_path / "original.json"
    json1.write_text(json.dumps(original_data), encoding='utf-8')
    
    csv1 = tmp_path / "converted.csv"
    json_to_csv(str(json1), str(csv1))
    
    json2 = tmp_path / "back.json"
    csv_to_json(str(csv1), str(json2))
    

    with open(json2, 'r', encoding='utf-8') as f:
        final_data = json.load(f)
    
    assert len(final_data) == len(original_data)
    assert final_data[0]["id"] == "1" 


def test_json_to_csv_file_not_found(tmp_path):
    """Файл не существует"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("несуществующий.json", str(tmp_path / "output.csv"))

def test_csv_to_json_file_not_found(tmp_path):
    """Файл не существует"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("несуществующий.csv", str(tmp_path / "output.json"))

def test_json_to_csv_empty_file(tmp_path):
    """Пустой JSON файл"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("", encoding='utf-8')
    
    with pytest.raises(ValueError, match="JSON файл пустой"):
        json_to_csv(str(empty_file), str(tmp_path / "output.csv"))

def test_csv_to_json_empty_file(tmp_path):
    """Пустой CSV файл"""
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("", encoding='utf-8')
    
    with pytest.raises(ValueError, match="CSV файл пустой"):
        csv_to_json(str(empty_file), str(tmp_path / "output.json"))

def test_json_to_csv_invalid_json(tmp_path):
    """Некорректный JSON"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("{это не json}", encoding='utf-8')
    

    with pytest.raises(ValueError):
        json_to_csv(str(invalid_file), str(tmp_path / "output.csv"))

def test_json_to_csv_not_a_list(tmp_path):
    """JSON не список"""
    invalid_file = tmp_path / "not_list.json"
    invalid_file.write_text('{"name": "Иван"}', encoding='utf-8')
    
    with pytest.raises(ValueError, match="JSON должен содержать список объектов"):
        json_to_csv(str(invalid_file), str(tmp_path / "output.csv"))

@pytest.mark.parametrize("json_content, should_fail", [
    ('[{"a": 1}]', False),  # нормальный
    ('[]', True),           # пустой список
    ('{}', True),           # не список
    ('"string"', True),     # не список
    ('123', True),          # не список
    ('null', True),         # не список
])
def test_json_to_csv_various_inputs(tmp_path, json_content, should_fail):
    """Различные входные данные для JSON"""
    json_file = tmp_path / "test.json"
    json_file.write_text(json_content, encoding='utf-8')
    
    csv_file = tmp_path / "test.csv"
    
    if should_fail:
        with pytest.raises(ValueError):
            json_to_csv(str(json_file), str(csv_file))
    else:
        json_to_csv(str(json_file), str(csv_file))
        assert csv_file.exists()