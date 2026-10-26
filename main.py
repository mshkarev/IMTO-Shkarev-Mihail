import csv
import random 
import xml.etree.ElementTree as ET
file = 'books-en.csv'
with open(file) as f:
    stroc = list(csv.reader(f, delimiter=';'))
data = stroc[1:]
k1 = 0
for stroc in data:
    if len(stroc[1]) > 30:
        k1 += 1
print(k1) #кол-во книг с кол-вом символов больше 30
#=====================================================
input()
def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index
search = input('Введи имя автора, книгу которого вы хотите найти ')
k2 = 0
for stroc in data:
    if find_string(search, stroc[2]) != -1:
        if stroc[3].isnumeric():
            if int(stroc[3]) < 1990:
                print(stroc[1], stroc[3], stroc[2])
                k2 += 1
                if k2 == 2:
                    break 
if k2 == 0:
    print('Не найдено')
#==================================================================================
input()
resultfile = open('result.txt', 'w')
k3 = 0
for stroc in random.sample(data, 20):
    k3 += 1
    resultfile.write(f'{k3}) {stroc[2]}. {stroc[1]} - {stroc[3]}\n')
resultfile.close()
print('Конец - данные загружены в result.txt')
#==================================================================================
input()
tree = ET.parse('currency.xml')
root = tree.getroot()
for valute in root.iter('Valute'):
    if valute.findtext('Nominal') == '1':
         print(valute.findtext('Name'))

