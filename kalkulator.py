from time import sleep


print()
print('Kalkulator Punktów do Liceum')
print('Kalkulator nie liczy punktów za tytuł laureta lub finalisty')
#Wyniki egzaminu
podaj1 = int(input('Wynik egzaminu z języka polskiego '))
podaj2 = int(input('Wynik egzaminu z matematyki '))
podaj3 = int(input('Wynik egzaminu z języka angielskiego '))
#Oceny na koniec roku
jp = int(input('Podaj ocenę z Polskiego '))
mat = int(input('Podaj ocenę z Matematyki '))
p1 = int(input('Podaj ocenę z pierwszego dodatkowo punktowanego przedmiotu '))
p2 = int(input('Podaj ocenę z drugiego dodatkowo punktowanego przedmiotu '))
#Świadectwo
dec = input('Czy posiadzasz świadectwo z czerwonym paskiem ? ')
if dec == 'Nie' or 'nie' :
    sw = 0
elif dec == 'Tak' or 'tak' :
    sw = 7
else:
    print('Prosiłem cię tylko o tak lub nie')
    exit()
#Analiza
egz1 = podaj1 * 0.35
egz2 = podaj2 * 0.35
egz3 = podaj3 * 0.30
pjp = 0
if jp == 2 :
    pjp = 2
elif jp == 3 :
    pjp = 8
elif jp == 4 :
    pjp = 14
elif jp == 5 :
    pjp = 17
elif jp == 6 :
    pjp = 18

pm = 0
if mat == 2 :
    pm = 2
elif mat == 3 :
    pm = 8
elif mat == 4 :
    pm = 14
elif mat == 5 :
    pm = 17
elif mat == 6 :
    pm = 18

pp1 = 0
if p1 == 2 :
    pp1 = 2
elif jp == 3 :
    pp1 = 8
elif p1 == 4 :
    pp1 = 14
elif p1 == 5 :
    pp1 = 17
elif p1 == 6 :
    pp1 = 18

pp2 = 0
if p2 == 2 :
    pp2 = 2
elif p2 == 3 :
    pp2 = 8
elif p2 == 4 :
    pp2 = 14
elif p2 == 5 :
    pp2 = 17
elif p2 == 6 :
    pp2 = 18

wynik = egz1 + egz2 + egz3 + pjp + pm + pp1 + pp2 + sw
owynik = round(wynik)

print('Ilość twoich punktów to ' + str(owynik))
sleep(5)


