import re


def calcul():
    while True:
        print(" Hello human how can we help you today !!")
        num = input(">> ")
        fonct = re.sub('[a-z,A-Z,;#!():$§£&]', '', num)
        s = eval(fonct)
        print("=> Resultat:", s)
        print("----Do you want to calculate another thing ? Y/N")
        resp = input()
        if resp == 'N' or resp == 'n':
            print('Thank you for visiting us ! GoodBy human ')
            break



calcul()
