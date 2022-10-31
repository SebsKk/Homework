
import numpy as np 
import pandas as pd 
import matplotlib as mp


# Zad 1 
prez = pd.read_csv('C:/Users/kaczm/Downloads/president_heights.csv')

x = prez['height(cm)'].mean()
print('Srednia wzrostu to {}'.format(x))

y = prez['height(cm)'].std()
print('Std to {}'.format(y))
z = prez['height(cm)'].max()
print('Max wzrost to {}'.format(z))
c = prez['height(cm)'].min()
print('Min wzrost to {}'.format(c))
med = prez['height(cm)'].median()
print('Mediana to {}'.format(med))

desr = prez.describe()
#1.6 25% kwantylu 174.25 cm
#1.7 75% kwantylu to 183 cm
print('25% kwantylu to 174.25')
print('75% kwantylu to 183')

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
no_rain = (seattle[(seattle['PRCP'] == 0)].count())
print('Ilos dni bez deszczu to {}'.format(no_rain[0]))
# ilosc dni bez deszczu to 215
rainy = (seattle[(seattle['PRCP'] > 0)].count())
print('Ilos dni z deszczem {}'.format(rainy[0]))
#3.2 ilosc dni z deszczem to 150
rainy_over = (seattle[(seattle['PRCP'] > 0.5)].count())
print('Ilos dni z deszczem powyzej 0.5 to {}'.format(rainy_over[0]))
#3.3 ilosc dni deszczu powyzej 0.5 to 37
rainy_under = (seattle[(seattle['PRCP'] < 0.2)].count())
print('Ilos dni z deszczem ponizej 0.2 to {}'.format(rainy_under[0]))
#3.4 ilosc dni deszczu ponizej 0.2 to 290
seattle_np = np.array(seattle['PRCP'])
med_rainy = np.ma.median(np.ma.masked_equal(seattle_np, 0))
print('Mediana opadow dni deszczowych w 2014 to {}'.format(med_rainy))
#3.5 Mediana opadow dni deszczowych w 2014 to 0.19488188976377951
arr_summ  = seattle['PRCP']
mymask = np.array([0 if x >= 172 or x < 262 else 1 for x in range(365)])
median_summer = np.ma.masked_array(arr_summ, mask = mymask)
print('mediana opadow latem to {}'.format(np.ma.median(median_summer)))
#3.6 Medianę opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262) to 0.0
mymask = np.array([0 if x >=172 and x <262 else 1 for x in range(365)])
v = np.ma.masked_array(seattle['PRCP'], mask = mymask)
print('Maksymalne opady latem 2014 r to {}'.format(np.ma.max(v)))
#3.7 Maksymalne opady latem 2014 roku to 0.8503937007874016
mymask2 = np.array([0 if x < 172 and x >- 262 else 1 for x in range(365)])
list_of_non_summer_days = np.ma.masked_array(arr_summ, mask = mymask2)
print('Maksymalne opady poza latem to {}'.format(np.ma.max(list_of_non_summer_days)))
#3.8 Maksymalne opady poza latem 2014 roku (czyli wiosna, jesień i zima) to 1.8385826771653544

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



