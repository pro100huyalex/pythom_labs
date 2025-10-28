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
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
