n = int(input('Введите число: '))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pole_ = []

for i in range(len(a)):
    if n == a[i]:
        continue
    for j in range(a[i], len(b)):
        if a[i] == b[j]:
            continue
        if n % (a[i] + b[j]) == 0:
            pole_.append(a[i])
            pole_.append(b[j])
        else:
            continue

print(f'{pole_}')
