import os
from time import sleep
clear = lambda: os.system('cls')
clear()
# print("="*80)
print("▬"*20,"os name is :", os.name, "▬"*20)
# print("="*80)
# =================== For Proc PRINT sep разделяет вывод параметров, а end задает символ конца строки, \t = TAB, \n = end line
# print("="*40)
# print("\"Code", "\tstepping\" ", 21+3, sep="*", end="\n")
# print(min(3,4,5,-4))
# print(max(3,4,5,-4))
# print(abs(-100))
# print(pow(5,40))
# print("="*40)
# =================== INPUT data
# number = 0
# number = int(input("Input parametr NUM:"))
# print("NUM=",number)
# del number
# number = 0
# number +=10
# print("NUM=",number)
# print("="*40)
# =================== Lesson_05 IF
# break = Прерывает цикл и выходит из него
# continue = переходит к следующей итерации цикла
# userA = int(input("Input userA: "))
# if userA > 10:
#     print ("userA > 10")
# elif userA < 10:
#     print ("userA < 10")
# else:
#     print ("userA is ZERO_10")

# userB = "HrenaSebe" if userA == 10 else "NON"
# print (userB)
# sleep(1)
# os.system('cls')
# =================== Lesson_06 FOR WHILE
# for i in range (5, 0, -1):
#     print (i)
#     sleep(1)
#     os.system('cls')

# print("="*40)
# =================== Lesson_07 List. Для создания списка используем [] скобки.
# BigList = [5, 4, 21, -1, True, 21, 3.1415, False, 5, 26]
# print(BigList)
# print("="*40)
# print(len(BigList))
# print("="*40)
# for i in range (0, len(BigList)):
#     print (BigList[i])
# print("="*40)
# for i in BigList:
#     print (i*2)
# print("="*40)
# BigList.sort()
# print(BigList)
# print("="*40)
# BigList.reverse()
# print(BigList)
# print("="*40)
# BigList.append(100) добавляем в конец элемент 100
# BigList.insert(5,21) вставляем в нужную позицию
# BigList.pop() pop(-2) pop(3) удаляем хвост или указанную позицию
# BigList.remove(21) удалить значение из списка
# BigList.count(21) ищет количество совпадений в списке со значением
# BigList.clear() очистить список
# =================== Lesson_08 Функции строк. Индексы и срезы. 
tWord = "One, two, three, four, fiVe, six, seveN"
print ("String:", tWord, "; Count T:" , tWord.count('t'), "; LenString: ", len(tWord))
# print (tWord.lower()) # islower, upper, isupper, capitalize ...
# print ("String:", tWord, "; Count T:" , tWord.count('t'), "; LenString: ", len(tWord))
tDig = tWord.split(', ')
# for i in tDig:
#     print (i)
# print("="*40)

for i in range(len(tDig)):
    tDig[i] = tDig[i].capitalize()
    print(tDig[i])
print("="*40)
tRes = "; ".join(tDig)
print (tRes)
print (tDig[1:6:2])
print("="*40)
# =================== Lesson_09 Кортежи (tuple). Для создания используем () скобки.
tCort = (4, 6, 7, True, 5.6, "Hello")
print (tCort[1:5], len(tCort), "\n", tDig, "\n", tuple(tDig))
# =================== Lesson_10 Словари (dict) {} скобки
print("="*40)
# country = {'code': "RU", 'name': "Russia", 'population' : 144}
country = dict(code="RU", name="Russia", population=144)

print (country['code'],country['name'], country["population"])

# =================== Lesson_11 Множества (set and frozenset)
# [] Лист (list)
# () Кортежи (tuple)
# {} Словари (dict)
print("="*40)
nums = [5,3,2,5,21,1, 2]
new_data = frozenset(nums)
print (set(nums), "\n", new_data)
# =================== Lesson_12 Функции
print("="*40)
def TestFunc():
    print ("Hello")
    pass
TestFunc()
def summa (a,b):
    return a+b
print (summa(1.3, 1.9))

func = lambda x, y: x*y
res=func(5,922234647)
print (res)
# =================== Lesson_13 Работа с файлами
print("="*40)
file=open('test01_text.txt', 'w')
file.write("Terminal 0212")
file.close()




# FINAL
print("▬"*57)