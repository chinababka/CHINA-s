from random import randint
import copy

# ПОВЕРНУТЬ МАТРИЦУ НА -90 ГРАДУСОВ
n = int(input("Enter the amount of rows and columns: "))
xu4 = [[randint(0, 9) for j in range(n)] for i in range(n)]  # Создаю матрицу размером n * n
print("MAIN")
for i in range(len(xu4)):
    for j in range(len(xu4[i])):
        print(xu4[i][j], end=" ")
    print()
print()
piz4a = copy.deepcopy(xu4)
print("ROTATED(-90')")
y = 0
for i in range(len(piz4a)):
    x = n - 1
    for j in range(len(piz4a[i])):
        piz4a[i][j] = xu4[x][y]
        x -= 1
        print(piz4a[i][j], end=" ")
    y += 1
    print()