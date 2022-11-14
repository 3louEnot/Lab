n = int(input('how many students in the class? '))
i = 1
suma = 0
while True:
    x = int(input(f'podai licb{i}: '))
    i += 1
    suma = suma + x
    if i > n:
        break
sred = suma/n
print(round(sred, 2))