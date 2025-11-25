import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """Простая конвертация JSON в CSV"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_keys = set()
    for item in data:
        all_keys = all_keys.union(item.keys())
    
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(all_keys))
        writer.writeheader()
        for item in data:
            writer.writerow({key: str(item.get(key, '')) for key in all_keys})

def csv_to_json(csv_path: str, json_path: str) -> None:
    """Простая конвертация CSV в JSON"""
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # Тест
    test_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "city": "London"}
    ]
    
    with open('test.json', 'w') as f:
        json.dump(test_data, f)
    
    json_to_csv('test.json', 'test.csv')
    print("JSON -> CSV выполнено")
    
    csv_to_json('test.csv', 'back.json')
    print("CSV -> JSON выполнено")