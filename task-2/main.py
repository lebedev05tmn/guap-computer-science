# Вариант реализации без использования циклов

def ordinaryResult(a):
    return bin(a)[2:]

# Вариант реализации Универсальной функции с использованием строчки
def uniResult(a, base):
    s = ""
    while a > 0:
        s += str(a%base)
        a //= base
    return s[::-1]

#Вывод
while True:
    try:
        # основание системы счисления - base
        base = 2
        print("Введите целое число")
        a = int(input())
        print("Результат", uniResult(a, base))
        break
    except:
        print("Error, try again")
