import math
print("ax^2 + bx + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
D = math.sqrt(math.pow(b, 2) - 4 * a * c)
if D < 0:
	print("Brak prawdziwych korzeni")
elif D >= 0:
	b *= -1
	x_1 = (b + D) / 2 * a
	x_2 = (b - D) / 2 * a
	print(f"x_1 = {x_1}, x_2 = {x_2}")