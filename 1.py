#Флаг
import os
import time
def flag():
    RED = '\u001b[41m'
    BLUE = '\u001b[44m'
    WHITE = '\u001b[47m'
    RESET = '\u001b[0m'
    print(RED + ' ' * 10 + RESET)
    print(WHITE + ' ' * 10 + RESET)
    print(BLUE + ' ' * 10 + RESET)

#Анимация
def animation():
    GREEN = '\u001b[42m'
    WHITE = '\u001b[47m'
    RESET = '\u001b[0m'
    n = 100
    for i in range(0, n + 1, 1):
        #os.system("cls")
        #делаем курсор невидимым + возвращаем в начало курсор + в конце стираем курсор (чтобы не накладывались кадры друг на друга)
        print('\033[H' + '\033[?25l' + GREEN + ' ' * i + RESET + WHITE + ' ' * (n - i) + RESET + '\n' + 'Loading... ' + f'{i}' + '%' + '\033[K')
        time.sleep(0.1)

#Диаграмма
def chart():
    RED = '\u001b[41m'
    GREEN = '\u001b[42m'
    RESET = '\u001b[0m'
    file = open('sequence.txt')
    arr = [float(x) for x in file]
    sum_chet = 0
    sum_nechet = 0
    for i in range(0, len(arr), 2):
        sum_chet += arr[i]
    for i in range(1, len(arr), 2):
        sum_nechet += arr[i]
    total = abs(sum_chet) + abs(sum_nechet)
    green_chet = int(abs(sum_chet) / total * 100)
    green_chet1 = abs(sum_chet) / total * 100
    red_nechet = int(abs(sum_nechet) / total * 100)
    red_nechet1 = abs(sum_nechet) / total * 100
    print(GREEN + ' ' * green_chet + RESET + RED + ' ' * red_nechet + RESET)
    print(GREEN + ' ' * green_chet + RESET + RED + ' ' * red_nechet + RESET)
    print(GREEN + ' ' * green_chet + RESET + RED + ' ' * red_nechet + RESET)
    print(green_chet1, '%', red_nechet1, '%')

#Узор
def uzor():
    d = ['x+++xx+++x', '+x+x++x+x+', '++x++++x++', '+x+x++x+x+', 'x+++xx+++x']
    RESET = '\u001b[0m'
    WHITE = '\u001b[47m'
    BLACK = '\u001b[40m'
    for a in d:
        s = ''
        for i in a:
            if i == 'x':
                s += BLACK + ' ' + RESET
            else:
                s += WHITE + ' ' + RESET
        print(s)

#Дополнительное Задание
def dop():
    for i in range(5, 0, -1):
        print(' ' * i + 'x')
        print(' ' * 5)


#Конец

animation()
time.sleep(3)
print('================================')
flag()
print('================================')
time.sleep(3)
print('================================')
chart()
print('================================')
time.sleep(3)
print('================================')
uzor()
print('================================')
dop()




