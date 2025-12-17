import csv
from typing import List, Optional
import os
from datetime import datetime
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab08.models import Student

class Group:
    """Класс для работы с группой студентов через CSV файл"""
    
    def __init__(self, csv_path: str):

        self.csv_path = csv_path
        self.students: List[Student] = []
        
        if not os.path.exists(csv_path):
            self._create_csv_file()
        

        self._load_from_csv()
    
    def _create_csv_file(self):
        """Создает пустой CSV файл с заголовками"""
        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
        
        with open(self.csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
        
        print(f" Создан новый CSV файл: {self.csv_path}")
    
    def _load_from_csv(self):
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    try:
                        student = Student.from_dict(row)
                        self.students.append(student)
                    except ValueError as e:
                        print(f" Ошибка при загрузке студента {row.get('fio', 'unknown')}: {e}")
                
                print(f" Загружено студентов из CSV: {len(self.students)}")
                
        except Exception as e:
            print(f"✗ Ошибка при загрузке CSV файла: {e}")
            self.students = []
    
    def _save_to_csv(self):
        try:
            with open(self.csv_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
                
                for student in self.students:
                    writer.writerow({
                        'fio': student.fio,
                        'birthdate': student.birthdate,
                        'group': student.group,
                        'gpa': student.gpa
                    })
            
            print(f"Данные сохранены в CSV: {self.csv_path}")
            
        except Exception as e:
            print(f"Ошибка при сохранении в CSV: {e}")
            raise
    
    def add(self, student: Student) -> bool:
        for existing_student in self.students:
            if existing_student.fio.lower() == student.fio.lower():
                print(f"Студент '{student.fio}' уже существует!")
                return False

        self.students.append(student)
        self._save_to_csv()
        
        print(f"Студент '{student.fio}' успешно добавлен")
        return True
    
    def list(self) -> List[Student]:
        return self.students
    
    def find(self, substr: str) -> List[Student]:
        substr = substr.lower()
        found_students = [
            student for student in self.students 
            if substr in student.fio.lower()
        ]
        
        print(f"Найдено студентов по запросу '{substr}': {len(found_students)}")
        return found_students
    
    def remove(self, fio: str) -> bool:
        for i, student in enumerate(self.students):
            if student.fio.lower() == fio.lower():
                removed_student = self.students.pop(i)
                self._save_to_csv()
                
                print(f"Студент '{removed_student.fio}' удален")
                return True
        
        print(f" Студент с ФИО '{fio}' не найден")
        return False
    
    def update(self, fio: str, **fields) -> bool:
        for i, student in enumerate(self.students):
            if student.fio.lower() == fio.lower():
                try:
                    student_data = {
                        'fio': student.fio,
                        'birthdate': student.birthdate,
                        'group': student.group,
                        'gpa': student.gpa
                    }
                    
                    student_data.update(fields)
                    
                    updated_student = Student.from_dict(student_data)
                    
                    self.students[i] = updated_student
                    self._save_to_csv()
                    
                    print(f" Студент '{fio}' обновлен")
                    print(f"  Обновленные поля: {list(fields.keys())}")
                    return True
                    
                except ValueError as e:
                    print(f"Ошибка при обновлении студента: {e}")
                    return False
        
        print(f" Студент с ФИО '{fio}' не найден")
        return False
    
    def get_statistics(self) -> dict:
        if not self.students:
            return {}
        total_gpa = sum(student.gpa for student in self.students)
        avg_gpa = total_gpa / len(self.students)
        
        groups = {}
        for student in self.students:
            groups[student.group] = groups.get(student.group, 0) + 1
        

        total_age = sum(student.age() for student in self.students)
        avg_age = total_age / len(self.students)
        

        max_gpa_student = max(self.students, key=lambda s: s.gpa)
        min_gpa_student = min(self.students, key=lambda s: s.gpa)
        
        return {
            'total_students': len(self.students),
            'average_gpa': round(avg_gpa, 2),
            'average_age': round(avg_age, 1),
            'groups_distribution': groups,
            'max_gpa': {
                'fio': max_gpa_student.fio,
                'gpa': max_gpa_student.gpa
            },
            'min_gpa': {
                'fio': min_gpa_student.fio,
                'gpa': min_gpa_student.gpa
            }
        }
    
    def print_all(self):
        if not self.students:
            print("В группе нет студентов")
            return
        
        print(f"\n{'='*60}")
        print(f"СПИСОК СТУДЕНТОВ (всего: {len(self.students)})")
        print(f"{'='*60}")
        
        for i, student in enumerate(self.students, 1):
            print(f"\n{i}. {student.fio}")
            print(f"   Дата рождения: {student.birthdate} (возраст: {student.age()} лет)")
            print(f"   Группа: {student.group}")
            print(f"   Средний балл: {student.gpa}")
        
        print(f"\n{'='*60}")


if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ КЛАССА GROUP")
    print("=" * 60)
    
    try:
        # Создаем объект Group
        csv_path = "../data/lab09/students.csv"
        group = Group(csv_path)
        
        # Тестируем добавление студентов
        print("\n1. Добавление студентов:")
        print("-" * 40)
        
        new_students = [
            Student("Иванов Иван Иванович", "2000-05-15", "ИТ-101", 4.5),
            Student("Петрова Анна Сергеевна", "2001-08-22", "ИТ-102", 4.8),
            Student("Сидоров Алексей Викторович", "1999-12-03", "ИТ-101", 3.9),
            Student("Козлова Мария Дмитриевна", "2002-03-30", "ИТ-102", 4.2),
            Student("Николаев Денис Олегович", "2000-11-18", "ИТ-103", 3.5),
        ]
        
        for student in new_students:
            group.add(student)
        print("\n2. Список всех студентов:")
        print("-" * 40)
        group.print_all()
        print("\n3. Поиск студентов по подстроке 'ива':")
        print("-" * 40)
        found = group.find("ива")
        for student in found:
            print(f"  - {student.fio}")
        print("\n4. Обновление студента:")
        print("-" * 40)
        group.update("Иванов Иван Иванович", gpa=4.7, group="ИТ-104")
    
        print("\n5. Удаление студента:")
        print("-" * 40)
        group.remove("Николаев Денис Олегович")
        

        print("\n6. Статистика группы:")
        print("-" * 40)
        stats = group.get_statistics()
        for key, value in stats.items():
            if key == 'groups_distribution':
                print(f"  Распределение по группам:")
                for group_name, count in value.items():
                    print(f"    {group_name}: {count} студентов")
            elif key in ['max_gpa', 'min_gpa']:
                print(f"  {key.replace('_', ' ').title()}: {value['fio']} ({value['gpa']})")
            else:
                print(f"  {key.replace('_', ' ').title()}: {value}")
        
        print("\n7. Финальный список студентов:")
        print("-" * 40)
        group.print_all()
        
    except Exception as e:
        print(f"\n✗ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    input("Нажмите Enter для выхода...")