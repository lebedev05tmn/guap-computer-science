## Структуры данных – списки, кортежи, строки

### Листинг программы

```python
def task(lenOfWords, inputString):
    taskResult = []
    for i in range(0, len(inputString)):
        if (len(inputString)-i)>=lenOfWords:
            s = ""
            for j in range(lenOfWords):
                s+=inputString[i+j]
            taskResult += [s]
    return taskResult

while True:
    try:
        taskLength = int(input("Введите длину строки"))
        taskString = input("Введите строку")

        print("Результат", task(taskLength, taskString))
        break
    except:
        print("Error, try again")
```
