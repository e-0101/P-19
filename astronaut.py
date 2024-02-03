from collections import Counter


def beolvas():
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        forrasfajl.readline()
        datumok = []
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            datumok.append(adatok[4])
    return datumok


def honapok(datumok):
    honapok_szamai = []
    for datum in datumok:
        honap = datum.split('/')[0]
        honapok_szamai.append(honap)
    return honapok_szamai


def elemzes(honapok_lista):
    eredmenyek = set()
    count = Counter(honapok_lista)
    for honap, value in count.items():
        eredmeny = round(value / len(honapok_lista) * 100, 1)
        eredmenyek.add((eredmeny, int(honap)))
    sorrend = sorted(eredmenyek, reverse=True)

    print('A három leggyakoribb születési hónap:')
    for i in range(0, 3):
        print(f'{sorrend[i][1]}. {sorrend[i][0]}%')


def main():
    elemzes(honapok(beolvas()))


main()
