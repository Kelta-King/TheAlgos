
def libraryFine(d1, m1, y1, d2, m2, y2):

    if y1 > y2:
        return '10000'
    elif y1 == y2 and m1 > m2:
        return str(500*(m1-m2))
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return str(15*(d1-d2))
    else:
        return str(0)


print(libraryFine(9, 6, 2015, 6, 6, 2015))