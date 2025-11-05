from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8"):
    p = Path(path)
    
    with open(p, "r", encoding=encoding) as f:
        content = f.read()  
    return content
file_path = "a.txt"
if not Path(file_path).exists():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Это тестовый файл a.txt\nПривет, мир!")
print(read_text(file_path))



from pathlib import Path
import csv

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None):
    p = Path(path)
    if rows:
        first_row_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_row_length}")
            

    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError(f"Заголовок имеет длину {len(header)}, а строки данных - {len(rows[0])}")
    with open(p, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")

        if header is not None:
            writer.writerow(header)
        
        writer.writerows(rows)

# Пример использования
if __name__ == "__main__":
    data = [
        ("Иван", 25, "Москва"),
        ("Мария", 30, "СПб"),
        ("Петр", 35, "Казань")
    ]
    
    header = ("Имя", "Возраст", "Город")
    
    write_csv(data, "people.csv", header)
    print("Файл создан")
    
    # Пример с ошибкой
    try:
        invalid_data = [
            ("Анна", 28),
            ("Сергей", 32, "Москва", "лишнее")
        ]
        write_csv(invalid_data, "error.csv", header)
    except ValueError as e:
        print(f"Ошибка: {e}")