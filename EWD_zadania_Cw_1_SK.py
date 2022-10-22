""" Zad.1
1. Dane z https://dane.gov.pl/pl/dataset/612,rozklad-mocy-dawki-promieniowania-gamma
2. Dostawca Danych: Państwowa Agencja Atomistyki
3. Dane w poszczególnym pliku h z okresów około 15-dniowych 
4. 45 rekordów w pliku z 06.09 - 20.09 (2022)
5. Kolumny to: Stacje, Miejscowosc, Zakres sredniej dziennej mocy dawki [nSv/h], srednia [nSv/h]
6. Dziala, ale tylko uzywajac encoding 'ISO-8859-1'

Zad.6

1. Stacje unique = ['PMS' 'IMiGW']
2. 40 miejscowosci
3. Dla mierzonego okresu najwyzsza wartosc to Krakow (116-122)
4. W zaleznosci od stacji pomiarowej, srednia dla Warszawy to 91 lub 69 dla badanego okresu. Dla lublina 104.
5. Proba wizualizacji ponizej
6. Brak podzialu na wojewodztwa w pliku

Zad. 7

Mozna porownac ilosc miejscowosci i stacje, ale srednie sa dla calego roku, a nie poszczegolnych okresow
"""

import pandas 
import matplotlib.pyplot as plt
import numpy
import csv

file = pandas.read_csv('C:/Users/kaczm/Downloads/Rozkład_mocy_dawki_promieniowania_gamma_06.09.22-20.09.22_4e4R7q7.csv',encoding = 'ISO-8859-1')

#print(pandas.unique(file['Stacje']))
#print(len(pandas.unique(file['Lokalizacja'])))
#print(file[file['Srednia [nSv/h]']==file['Srednia [nSv/h]'].max()])

#Warszawa
#print(file[file['Lokalizacja']=='Warszawa'])

#Lublin
#print(file[file['Lokalizacja']=='Lublin'])

"""plt.plot(file['Lokalizacja'], file['Srednia [nSv/h]'])
plt.show()"""

# Zad.7
file2 = pandas.read_csv('C:/Users/kaczm/Downloads/Wartoci-mocy-dawki-uzyskane-ze-stacji-wczesnego-wykrywania-skae-promieniotworczych-w-2021-r.csv',encoding = 'ISO-8859-1',delimiter = ';')

print(file2)
