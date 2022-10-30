#numpy to temat przewodni dzisiejszego cwiczenia 
import numpy as np 
import pandas as pd

# Zad 1 
prez = pd.read_csv('C:/Users/kaczm/Downloads/president_heights.csv')

x = prez['height(cm)'].mean()
#1.1 srednia wzrostu to 179.73809523809524 cm
y = prez['height(cm)'].std()
#1.2 std to 7.0158688553582955 cm
z = prez['height(cm)'].max()
#1.3 max wzrost to 193 cm
c = prez['height(cm)'].min()
#1.4 min wzrost to 163 cm

med = prez['height(cm)'].median()
#1.5 mediana to 182 cm

desr = prez.describe()
#1.6 25% kwantylu 174.25 cm
#1.7 75% kwantylu to 183 cm

# Zad 2 

zad2 = np.array(pd.read_csv('C:/Users/kaczm/Downloads/Zadanie_2.csv', delimiter = ';', header = None))


ww, wm = np.linalg.eig(zad2)
#2.1 a)  wartosci macierzy
ww
#2.1 b) wektory macierzy
wm

#2.2 odwrocona macierz:
rev_mat = np.linalg.inv(zad2)
rev_mat

# Zad 3

seattle = pd.read_csv('C:/Users/kaczm/Downloads/Seattle2014.csv')

seattle['PRCP'] /= 254.0

#3.1 Number of days without rain
print((seattle[(seattle['PRCP'] ==0)].count()))

# ilosc dni bez deszczu to 215
print((seattle[(seattle['PRCP'] > 0)].count()))
#3.2 ilosc dni z deszczem to 150
print((seattle[(seattle['PRCP'] > 0.5)].count()))
#3.3 ilosc dni deszczu powyzej 0.5 to 37
print((seattle[(seattle['PRCP'] < 0.2)].count()))
#3.4 ilosc dni deszczu ponizej 0.2 to 290

#3.5 Mediana opadow dni deszczowych w 2014 

seattle_np = np.array(seattle['PRCP'])
print(np.ma.median(np.ma.masked_equal(seattle_np, 0)))
#Mediana w dni deszczowe to 0.19488188976377951

#3.6 Medianę opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262)

mymask = np.array([0 if x < 170 or x >=200 else 1 for x in range(365)])

x = np.ma.masked_array(seattle['PRCP'], mask = mymask)
print(np.ma.median(x))
# Mediana opadów w lecie to 0.0

#3.7 Maksymalne opady latem 2014 roku

print(list_of_summer_days.max())
# Maksymalne opady w lecie to 0.8503937007874016

#3.8 Maksymalne opady poza latem 2014 roku (czyli wiosna, jesień i zima)

list_of_non_summer_days = np.array([val for ind, val in enumerate(arr_summ) if ind < 171 or ind >= 262])
print(list_of_non_summer_days.max())
# Maksymalne opady poza latem to 1.8385826771653544

#Zad 4 

A = [0,3,2,5]
B = [0,3,1,4]

#4.1 - Dodawanie wektorów 

vec = [a + b for a,b in zip(A,B)]
#Mozna tez zrobic to w numpy: np.array(A) + np.array(B)

#4.2 Odejmowanie wektorów

vec2 = [a - b for a,b in zip(A,B)]
#Mozna tez zrobic to w numpy: np.array(A) - np.array(B)

#4.3 Mnożenie wektora przez skalar

sc = 4 

multiplied_A = np.array(A)*sc

#4.4 Obliczanie iloczynu skalarnego A i B

scalar = np.dot(A,B)

#iloczyn skalarny A i B to 31

#4.5 Długość wektora B

length_B = np.linalg.norm(B)
#Długość wektora B to 5.0990195135927845
