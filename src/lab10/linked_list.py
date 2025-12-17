from typing import Any, Optional, Iterator


class Node:
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        
        self.value = value
        self.next = next_node
    
    def __repr__(self) -> str:
        """Строковое представление узла"""
        return f"Node({self.value})"


class SinglyLinkedList:
    
    def __init__(self):
        """Инициализация пустого списка"""
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:  
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        
        if self.tail is None:  # Если список был пуст
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        elif idx == self._size:
            self.append(value)
            return
        
        new_node = Node(value)
        current = self.head
        
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        if idx == 0:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
        
            current.next = current.next.next

            if current.next is None:
                self.tail = current
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                
                if current.next is None:
                    self.tail = current
                
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, value: Any) -> Optional[int]:
        current = self.head
        idx = 0
        
        while current is not None:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        
        return None
    
    def get(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        elements = list(self)
        return f"SinglyLinkedList({elements})"
    
    def __str__(self) -> str:
        if self.head is None:
            return "Пустой список"
        
        elements = list(self)
        return f"Список с {len(self)} элементами: {elements}"



if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ SINGLY LINKED LIST")
    print("=" * 60)
    
    lst = SinglyLinkedList()
    print(f"Создан: {lst}")
    
    print("\n1. Добавление элементов в конец (append):")
    print("-" * 40)
    for i in range(1, 4):
        lst.append(i * 10)
        print(f"append({i * 10}) -> {lst}")
    
    print("\n2. Добавление элементов в начало (prepend):")
    print("-" * 40)
    for i in range(3, 0, -1):
        lst.prepend(i)
        print(f"prepend({i}) -> {lst}")
    
    print("\n3. Вставка по индексу (insert):")
    print("-" * 40)
    lst.insert(2, 999)
    print(f"insert(2, 999) -> {lst}")
    
    lst.insert(0, -1)
    print(f"insert(0, -1) -> {lst}")
    
    lst.insert(len(lst), 1000)
    print(f"insert({len(lst)-1}, 1000) -> {lst}")
    
    print("\n4. Поиск элемента (find):")
    print("-" * 40)
    values_to_find = [999, 20, 777]
    for val in values_to_find:
        idx = lst.find(val)
        if idx is not None:
            print(f"Значение {val} найдено на позиции {idx}")
        else:
            print(f"Значение {val} не найдено")
    
    print("\n5. Получение элемента по индексу (get):")
    print("-" * 40)
    for i in [0, 2, len(lst) - 1]:
        print(f"get({i}) = {lst.get(i)}")
    
    print("\n6. Удаление по значению (remove):")
    print("-" * 40)
    values_to_remove = [999, 1, 777]
    for val in values_to_remove:
        if lst.remove(val):
            print(f"Удалено значение {val} -> {lst}")
        else:
            print(f"Значение {val} не найдено, список без изменений")
    
    print("\n7. Удаление по индексу (remove_at):")
    print("-" * 40)
    indices_to_remove = [0, 2, len(lst) - 1]
    for idx in indices_to_remove:
        if idx < len(lst):
            print(f"До remove_at({idx}): {lst}")
            lst.remove_at(idx)
            print(f"После remove_at({idx}): {lst}")
    
    print("\n8. Итерация по списку:")
    print("-" * 40)
    print("Элементы списка:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)
    
    input("\nНажмите Enter для выхода...")