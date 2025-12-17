from collections import deque
from typing import Any, Optional


class Stack:
    
    def __init__(self):
        """Инициализация пустого стека"""
        self._data = []
    
    def push(self, item: Any) -> None:
        self._data.append(item)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Нельзя выполнить pop(): стек пуст")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Stack({self._data})"
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Пустой стек"
        return f"Стек с {len(self)} элементами, верхний: {self.peek()}"


class Queue:
    
    def __init__(self):
        """Инициализация пустой очереди"""
        self._data = deque()
    
    def enqueue(self, item: Any) -> None:
        self._data.append(item)
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Нельзя выполнить dequeue(): очередь пуста")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Пустая очередь"
        return f"Очередь с {len(self)} элементами, первый: {self.peek()}"

if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ STACK И QUEUE")
    print("=" * 60)
    
    print("\n1. Тестирование Stack:")
    print("-" * 40)
    
    stack = Stack()
    print(f"Создан: {stack}")
    
    for i in range(1, 6):
        stack.push(i * 10)
        print(f"push({i * 10}) -> {stack}")
    
    print(f"\nВерхний элемент (peek): {stack.peek()}")
    print(f"Размер стека: {len(stack)}")
    
    while not stack.is_empty():
        item = stack.pop()
        print(f"pop() -> {item}, осталось: {stack}")
    
    print("\n2. Тестирование Queue:")
    print("-" * 40)
    
    queue = Queue()
    print(f"Создана: {queue}")

    for i in range(1, 6):
        queue.enqueue(i * 10)
        print(f"enqueue({i * 10}) -> {queue}")
    
    print(f"\nПервый элемент (peek): {queue.peek()}")
    print(f"Размер очереди: {len(queue)}")
    
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"dequeue() -> {item}, осталось: {queue}")
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)
    
    input("\nНажмите Enter для выхода...")