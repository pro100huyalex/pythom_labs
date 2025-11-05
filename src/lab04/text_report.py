from io_txt_csv import read_text, write_csv
from pathlib import Path
import csv

def normalize(text: str, *, casefold: bool = True, yoe: bool = True):
    resu = text
    contro = ['\t', '\r', '\n', '\v', '\f']
    for char in contro:
        resu = resu.replace(char, ' ')
    while '  ' in resu:
        resu = resu.replace('  ', ' ')
    resu = resu.strip()
    if yoe:
        resu = resu.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        resu = resu.casefold()
    return resu

def tokenize(text: str):
    result = []
    current_word = []
    for i, char in enumerate(text):
        if char.isalnum() or char == '_':
            current_word.append(char)
        elif char == '-' and current_word and i + 1 < len(text) and (text[i + 1].isalnum() or text[i + 1] == '_'):
            current_word.append(char)
        else:
            if current_word:
                result.append(''.join(current_word))
                current_word = []
    if current_word:
        result.append(''.join(current_word))
    return result

def analyze_text(file_path: str = "data/input.txt"):
    text = read_text(file_path)
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    word_counts = {}
    for word in tokens:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    report_path = "data/report.csv"
    Path("data").mkdir(exist_ok=True)
    rows = [(word, count) for word, count in sorted_words]
    header = ("word", "count")
    
    write_csv(rows, report_path, header)
    total_words = len(tokens)
    unique_words = len(word_counts)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in sorted_words[:5]:
        print(f"  {word}: {count}")

if __name__ == "__main__":
    file_path = "data/input.txt"
    if not Path(file_path).exists():
        Path("data").mkdir(exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Это тестовый файл input.txt\nПривет, мир! Привет всем. Тестовый-файл тестовый текст.")
    analyze_text(file_path)