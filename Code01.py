import os
clear = lambda: os.system('cls')
clear()

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
userA = int(input("Input userA: "))
if userA > 10:
    print ("userA > 10")
elif userA < 10:
    print ("userA < 10")
else:
    print ("userA is ZERO_10")

userB = "HrenaSebe" if userA == 10 else "NON"
print (userB)
print("="*40)