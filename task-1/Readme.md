## Введение в Python. Алгоритмы линейной структуры.

### Листинг программы

```python
import math
def result (a,b,c,d):
    return ((a/(2*math.pi*(b-(b**2-c**2)**0.5)))**0.5)+math.sin(d)

while True:
    try:
        print("Введите A,B,C,В")
        a, b, c, d = [float(input()) for x in range(3)]

        print("Результат",result(a,b,c,d))
        break
    except:
        print("Error, try again")
```