import argparse
import sys
from pathlib import Path

def analyze_text(text, top_n=5):
    """Простая функция анализа текста"""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        word = word.strip('.,!?;:"()')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def cat_file(filepath, number_lines=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if number_lines:
                    print(f"{i:6}  {line.rstrip()}")
                else:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Утилиты для работы с текстом",
        prog="python -m src.lab06.cli_text"
    )
    
    # Создаем подкоманды
    subparsers = parser.add_subparsers(
        dest="command", 
        help="Доступные команды",
        required=True
    )
    
    # 1. Команда stats
    stats_parser = subparsers.add_parser(
        "stats", 
        help="Анализ частоты слов в тексте"
    )
    stats_parser.add_argument(
        "--input", 
        required=True,
        help="Путь к текстовому файлу"
    )
    stats_parser.add_argument(
        "--top", 
        type=int, 
        default=5,
        help="Сколько самых частых слов показать (по умолчанию: 5)"
    )
    
    # 2. Команда cat
    cat_parser = subparsers.add_parser(
        "cat", 
        help="Вывод содержимого файла"
    )
    cat_parser.add_argument(
        "--input", 
        required=True,
        help="Путь к файлу"
    )
    cat_parser.add_argument(
        "-n", 
        action="store_true",
        help="Нумеровать строки"
    )
    
    # Разбираем аргументы
    args = parser.parse_args()
    
    # Выполняем команду
    if args.command == "stats":
        # Читаем файл
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Ошибка: файл {args.input} не найден")
            sys.exit(1)
        
        # Анализируем
        result = analyze_text(text, args.top)
        
        # Выводим результат
        print(f"Топ-{args.top} самых частых слов в файле {args.input}:")
        print("-" * 30)
        for word, count in result:
            print(f"{word:<20} : {count:>3}")
            
    elif args.command == "cat":
        cat_file(args.input, args.n)

if __name__ == "__main__":
    main()