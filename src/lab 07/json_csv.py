import json
import csv
from pathlib import Path

def json_to_csv(src_path: str, dst_path: str) -> None:
    """Конвертирует JSON в CSV"""
    if not Path(src_path).exists():
        raise FileNotFoundError(f"Файл не найден: {src_path}")
    
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        raise ValueError("JSON файл пустой")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    # Получаем заголовки из первого объекта
    headers = list(data[0].keys())
    
    with open(dst_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(src_path: str, dst_path: str) -> None:
    """Конвертирует CSV в JSON"""
    if not Path(src_path).exists():
        raise FileNotFoundError(f"Файл не найден: {src_path}")
    
    with open(src_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    if not data:
        raise ValueError("CSV файл пустой")
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)