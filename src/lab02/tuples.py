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
