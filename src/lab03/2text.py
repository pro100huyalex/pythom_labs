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
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("emoji 😀 не слово"))
