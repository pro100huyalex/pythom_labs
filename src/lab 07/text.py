def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру и удаляет пробелы по краям"""
    if not text:
        return ""
    return text.lower().strip()

def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова, удаляя знаки препинания"""
    if not text:
        return []
    
    words = text.split()
    result = []
    
    for word in words:
        # Убираем знаки препинания
        cleaned = word.strip('.,!?;:"()[]{}«»—')
        if cleaned:
            result.append(cleaned)
    
    return result

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает частоту слов в списке"""
    freq = {}
    
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    
    return freq

def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Возвращает N самых частых слов"""
    if not freq or n <= 0:
        return []
    
    # Сортировка: сначала по частоте (убывание), потом по слову (возрастание)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]