# pythom_labsgit
лаба 1
задание 1
name = input("Имя : ")
aage = int(input("Возраст : "))
print("Привет",name,"!", "Через год тебе будет", aage + 1, "." )
```
![alt text](src/images/lab01/знакомство.png)

## задание 2
```bash
first = input()
sec = input()
first = float(first.replace(",","."))
sec = float(sec.replace(",","."))
print(round(first + sec,2), round((first + sec)/2,2))
```
![alt text](src/images/lab01/мредсумм.png)

## задание 3
```bash
price = int(input())
sasale = int(input())
vshevstvennie = int(input())
base = price * (1 - sasale / 100)
hz = base * (vshevstvennie / 100)
itog = base + hz
print("База после скидки: ", base)
print("НДС: ", hz)
print("Итог к оплате: ", itog)
```
![alt text](src/images/lab01/касса.png)

## задание 4
```bash
minets = int(input("Minuti : "))
howers = minets // 60
print(f"{howers}:{minets % 60}")
```
![alt text](src/images/lab01/минутычасы.png)

## задание 5
```bash
familia,ima,otchestwo = input("ФИО : ").split()
iniciala = familia[0] + ima[0] + otchestwo[0]
dlina = len(familia) + len(ima) + len(otchestwo)
print("Инициалы : ", iniciala)
print("Длина : ", dlina + 2) # два потому что у нас три слова и между ними может быть только два пробела не лишних, тк я считал  сплитом и длиной строки , то пробелы я вообще не учитывал
```
![alt text](src/images/lab01/фио.png)


### ЛАБА 2
### задание 1.1
def pp(a):
    if a == "[]":
        return ValueError
    else:
        a = a.replace("[", "")
        a = a.replace("]", "")
        a = a.replace(",", "")
        a = a.split()
        a = list(map(float, a))
        m = min(a)
        bol = max(a)
        if str(m)[-2:] == ".0":
            m = int(str(m)[:-2])
        if str(bol)[-2:] == ".0":
            bol = int(str(bol)[:-2])
        return (m, bol)
asadasdasdas = input()
![alt text](1.1image.png)


### задание 1.2
def pppp(a):
    if a == "[]":
        return a
    else:
        a = a.replace("[", "")
        a = a.replace("]", "")
        a = a.replace(",", "")
        a = a.split()
        b = []
        for i in a:
            if "." in i:
                b.append(float(i))
            else:
                b.append(int(i))
        return list(sorted(set(b)))
s = input()
print(pppp(s))
![alt text](src/images/lab02/1.2.png)

### задание 1.3
import ast
def pspsp(a):
    b = []
    for i in a:
        if i == '"':
            return TypeError
    a = ast.literal_eval(a)
    for i in a:
        for j in i:
            b.append(j)
    return b
sss = input()
print(pspsp(sss))
![alt text](src/images/lab02/1.3.png)
### задание 2.1
 import ast
def psiz(a):
    s = ast.literal_eval(a)
    if not s:
        return []
    for i in range(len(s) - 1):
        if len(s[i]) != len(s[i + 1]):
            return ValueError
    return [list(i) for i in zip(*s)]
aaa = input()
print(psiz(aaa))
![alt text](src/images/lab02/2.1.png)
### задание 2.2
import ast
def psiz(a):
    s = ast.literal_eval(a)
    if not s:
        return []
    for i in range(len(s) - 1):
        if len(s[i]) != len(s[i + 1]):
            return ValueError
    return [sum(i) for i in s]
aaa = input()
print(psiz(aaa))
![alt text](src/images/lab02/2.2.png)
### задание 2.3
import ast
def psiz(a):
    s = ast.literal_eval(a)
    if not s:
        return []
    for i in range(len(s) - 1):
        if len(s[i]) != len(s[i + 1]):
            return ValueError
    return [sum(i) for i in zip(*s)]
aaa = input()
print(psiz(aaa))
![alt text](src/images/lab02/2.3.png)
### задание 3
def ФИО(a):
    grade = a[-1]
    grupp = a[-2]
    inic = list(a[:-2])
    inic = str(inic[0])
    inic = inic.split()
    grade = f"{grade:.2f}"
    if type(grade) != str:
        return ValueError
    initials = inic[0][0].upper() + inic[0][1:]
    for i in inic[1:]:
        initials += " " + i[0].upper() + "."
    itogstr = initials + ", гр. " + grupp + ", " + grade

    return itogstr

print(ФИО(("Иванов uван Иванович", "IKBO-12", 4.6)))
print(ФИО(("Петров Пётр", "IKBO-12", 5.0)))
print(ФИО(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(ФИО(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
![alt text](src/images/lab02/3.png)