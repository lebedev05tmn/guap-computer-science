## Управляющие структуры

### Проблематика

#### Задача предполагает несколько подходов к её решению:

- Ординарный

##### Ординарный подход решает задачу только для основания системы счисления - 2

```python
a = 10
bin(a)[2:] # 1010
```

- Универсальный

#### Универсальный подход решает задачу для любой системы счисления

```python
base = 2
a = 10
def uniResult(a, base):
    s = ""
    while a > 0:
        s += str(a%base)
        a //= base
    return s[::-1]
uniResult(a, base) #1010
```

### Листинг программы

```python

def ordinaryResult(a):
    return bin(a)[2:]

def uniResult(a, base):
    s = ""
    while a > 0:
        s += str(a%base)
        a //= base
    return s[::-1]

while True:
    try:
        base = 2
        print("Введите целое число")
        a = int(input())
        print("Результат", uniResult(a, base))
        break
    except:
        print("Error, try again")

```
