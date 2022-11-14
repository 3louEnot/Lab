n = int(input('how many students in the class? '))
i = 1
suma = 0
while i <= n:
    x = int(input(f'podai licb{i}: '))
    if x<0 or x>100:continue
    i += 1
    suma = suma + x
sred = suma/n