import json
from typing import List
from .models import Student 


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сериализует список студентов в JSON файл
    
    Args:
        students: список объектов Student
        path: путь к файлу для сохранения
    """
    try:

        data = [student.to_dict() for student in students]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        
        print(f" Данные сохранены в файл: {path}")
        print(f" Сохранено студентов: {len(students)}")
        
    except Exception as e:
        print(f" Ошибка при сохранении в JSON: {e}")
        raise


def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = [Student.from_dict(item) for item in data]
        
        print(f" Данные загружены из файла: {path}")
        print(f" Загружено студентов: {len(students)}")
        
        return students
        
    except Exception as e:
        print(f" Ошибка при загрузке из JSON: {e}")
        raise

if __name__ == "__main__":
    try:

        students = [
            Student(
                fio="Иванов Иван Иванович",
                birthdate="2000-05-15",
                group="ИТ-101",
                gpa=4.5
            ),
            Student(
                fio="Петрова Анна Сергеевна",
                birthdate="2001-08-22",
                group="ИТ-102",
                gpa=4.8
            ),
            Student(
                fio="Сидоров Алексей Викторович",
                birthdate="1999-12-03",
                group="ИТ-103",
                gpa=3.9
            ),
            Student(
                fio="Козлова Мария Дмитриевна",
                birthdate="2002-03-30",
                group="ИТ-101",
                gpa=4.2
            ),
            Student(
                fio="Николаев Денис Олегович",
                birthdate="2000-11-18",
                group="ИТ-104",
                gpa=3.5
            )
        ]
        

        output_path = "../data/lab08/students_output.json"
        students_to_json(students, output_path)

        loaded_students = students_from_json(output_path)
        
        print("\n" + "="*50)
        print("Загруженные студенты:")
        print("="*50)
        for i, student in enumerate(loaded_students, 1):
            print(f"\nСтудент #{i}:")
            print(student)
            print("-" * 30)
            
    except Exception as e:
        print(f"Ошибка в основном блоке: {e}")