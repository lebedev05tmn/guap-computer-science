## Структуры данных – списки, кортежи, строки

### Листинг программы

```python
def sliceTask(fstArray, scdArray):
    return sorted([*fstArray, *scdArray])[::-1]

while True:
    try:
        print("Введите через пробел первый массив")
        fstArray = [int(x) for x in input().split()]
        print("Введите через пробел второй массив")
        scdArray = [int(x) for x in input().split()]
        print("Результат", sliceTask(fstArray, scdArray))
        break
    except:
        print("Error, try again")
```
