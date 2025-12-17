from dataclasses import dataclass, asdict
from datetime import datetime, date
import re

@dataclass
class Student:
    """Модель студента с валидацией данных"""
    fio: str           
    birthdate: str     
    group: str         
    gpa: float         
    
    def __post_init__(self):
        """Валидация данных после созданияа"""
        self._validate_birthdate()
        self._validate_gpa()
    
    def _validate_birthdate(self):
        """Проверка формата даты YYYY-MM-DD"""
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, self.birthdate):
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Используйте YYYY-MM-DD")
        
        try:
            year, month, day = map(int, self.birthdate.split('-'))
            date(year, month, day) 
        except ValueError as e:
            raise ValueError(f"Некорректная дата: {self.birthdate}. Ошибка: {e}")
    
    def _validate_gpa(self):
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть в диапазоне 0-5, получено: {self.gpa}")
    
    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, '%Y-%m-%d').date()
        today = date.today()
        
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa,
            'age': self.age()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        student_data = {key: data[key] for key in ['fio', 'birthdate', 'group', 'gpa']}
        return cls(**student_data)
    
    def __str__(self) -> str:
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate} (возраст: {self.age()} лет)\n"
                f"Группа: {self.group}\n"
                f"Средний балл: {self.gpa}")


if __name__ == "__main__":
    try:
        student1 = Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="ИТ-101",
            gpa=4.5
        )
        
        print(student1)
        print("\nСловарь:", student1.to_dict())
        
        # Тест
        print("\nТест валидации:")
        try:
            student2 = Student(
                fio="Петров Петр",
                birthdate="2025-13-45",
                group="ИТ-102",
                gpa=4.0
            )
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            
        try:
            student3 = Student(
                fio="Сидоров Сидор",
                birthdate="2001-08-20",
                group="ИТ-103",
                gpa=6.0 
            )
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            
    except Exception as e:
        print(f"Ошибка: {e}")