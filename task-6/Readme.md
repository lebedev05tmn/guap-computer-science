## Работа с файлами

### Листинг программы

```python
while True:
    try:
        f = [x.split() for x in open("some_file.txt")]
        new_file = open("data.txt", "w+")
        new_file.write(f'Количество строк: {len(f)}; \n')
        new_file.write(f'Количество слов: {sum([len(x) for x in f])}; \n')
        new_file.write(f'Количество символов: {sum([len(x) for x in[a for b in f for a in b]])}; \n')
        new_file.close()
        break
    except:
        print("Error, file not found")
```
