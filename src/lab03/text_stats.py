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
def teststsd(sss:str):
    a = tokenize(normalize(sss))
    prow = set(a)

    prow = sorted(a)
    schet = {}
    vsego = 0
    for i in prow:
        schet[i] = a.count(i)
    for key in schet:
        vsego += schet[key]
    print("Всего слов:", vsego)
    print("Уникальных слов:", len(schet))
    print("Топ 5:")
    for i in sorted(schet.items(), reverse=True)[:5]:
        print(f"{i[0]}: {i[1]}")
teststsd("Привет, мир! Привет")


