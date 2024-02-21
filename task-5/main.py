def fstTask(a, n):
    summTask = 0
    countOfPositives = 0
    for i in range(n):
        for j in range(n):
            if j > i: 
                summTask += a[i][j]
                if a[i][j] > 0:
                    countOfPositives += 1
    return [summTask,countOfPositives]

def scdTask(b, n, m):
    for i in range(n):
        maxOfTableLine = b[i][0]
        minOfTableLine = b[i][0]
        for j in range(m):
            maxOfTableLine = max(b[i][j], maxOfTableLine)
            minOfTableLine = min(b[i][j], minOfTableLine)
        b[i][b[i].index(maxOfTableLine)]=b[i][0]
        b[i][0]=maxOfTableLine
        b[i][b[i].index(minOfTableLine)]=b[i][-1]
        b[i][-1]=minOfTableLine
    return b

while True:
    try:
        n1 = int(input(("Введите n для первой задачи\n")))
        fstMatrix = []
        for i in range(n1):
            print(f'Введите {i+1} строку матрицы через пробел')
            s = [int(x) for x in input().split()]
            if len(s)!=n1:
                print("Error, try again")
                continue
            else:
                fstMatrix += [s]
        print("Результат первой задачи", fstTask(fstMatrix, n1))

        n2 = int(input(("Введите n для второй задачи")))
        m = int(input(("Введите m для второй задачи")))
        scdMatrix = []
        for i in range(n2):
            print(f'Введите {i+1} строку матрицы через пробел')
            s = [int(x) for x in input().split()]
            if len(s)!=m:
                print("Error, try again")
                continue
            else:
                fstMatrix += [s]
        print("Ответ для второй задачи", scdTask(scdMatrix, n2, m))

        break
    except: 
        print("Error, try again")
