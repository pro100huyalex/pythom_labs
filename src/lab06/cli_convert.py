import argparse
import sys
import json
import csv
from pathlib import Path

def json_to_csv(json_file, csv_file):
    """Конвертирует JSON в CSV"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not data:
            print("Ошибка: JSON файл пустой")
            return False
        if isinstance(data, list):
            headers = data[0].keys()
            
            with open(csv_file, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
        else:
            print("Ошибка: JSON должен содержать список объектов")
            return False
            
        print(f"✓ Конвертировано: {json_file} → {csv_file}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")
        return False

def csv_to_json(csv_file, json_file):
    """Конвертирует CSV в JSON"""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Конвертировано: {csv_file} → {json_file}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
        return False

def csv_to_xlsx(csv_file, xlsx_file):
    """Конвертирует CSV в XLSX"""
    try:
        # Для простоты используем csv.reader и записываем как текст
        with open(csv_file, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(xlsx_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"⚠ Внимание: это заглушка! Реальную конвертацию реализуйте через openpyxl")
        print(f"Файл создан: {csv_file} → {xlsx_file}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации CSV в XLSX: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Конвертер форматов файлов",
        prog="python -m src.lab06.cli_convert"
    )
    
    # Создаем подкоманды
    subparsers = parser.add_subparsers(
        dest="command", 
        help="Доступные команды конвертации",
        required=True
    )
    
    # 1. Команда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", 
        help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", 
        dest="input_file",
        required=True,
        help="Входной JSON файл"
    )
    json2csv_parser.add_argument(
        "--out", 
        dest="output_file",
        required=True,
        help="Выходной CSV файл"
    )
    
    # 2. Команда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", 
        help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", 
        dest="input_file",
        required=True,
        help="Входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", 
        dest="output_file",
        required=True,
        help="Выходной JSON файл"
    )
    
    # 3. Команда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", 
        help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", 
        dest="input_file",
        required=True,
        help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", 
        dest="output_file",
        required=True,
        help="Выходной XLSX файл"
    )
    
    # Разбираем аргументы
    args = parser.parse_args()
    
    # Выполняем команду
    if args.command == "json2csv":
        json_to_csv(args.input_file, args.output_file)
        
    elif args.command == "csv2json":
        csv_to_json(args.input_file, args.output_file)
        
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input_file, args.output_file)

if __name__ == "__main__":
    main()