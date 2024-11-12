#               Дрочу на пайтон
import readchar
#             ввод первого числа
a = int(input ("введи число: "))
#               ввод действия
b = input("выберите действие (+,-,*,/,): ")
#              ввод второго числа
c = int(input ("число: "))
#               выбор действия
if b == "+":
   b = a + c
elif b == "*":
    b = a * c
elif b == "-":
    b = a - c
elif b == "/":
    try:
            b = a / c
    except ZeroDivisionError: 
            b = "Деление на ноль запрещено" 
else:
    print("неправильное действие")
print(b)
    

print("нажмите любую клавишу чтобы закрыть") ; readchar.readchar()

