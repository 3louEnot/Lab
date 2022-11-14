print("1 - dodawać")
print("2 - odejmować")
print("3 - mnożyć")
print("4 - dzielić ")
print("5 - obliczać resztę")
user = int(input("Wybór: "))
if user == 1:
	arg1 = int(input("Argument 1: "))
	arg2 = int(input("Argument 2: "))
	result = arg1 + arg2
	print(f"Result: {result}")
elif user == 2:
	arg1 = int(input("Argument 1: "))
	arg2 = int(input("Argument 2: "))
	result = arg1 - arg2
	print(f"Result: {result}")
elif user == 3:
	arg1 = int(input("Argument 1: "))
	arg2 = int(input("Argument 2: "))
	result = arg1 * arg2
	print(f"Result: {result}")
elif user == 4:
	arg1 = int(input("Argument 1: "))
	arg2 = int(input("Argument 2: "))
	result = arg1 / arg2
	print(f"Result: {result}")
elif user == 5:
	arg1 = int(input("Argument 1: "))
	arg2 = int(input("Argument 2: "))
	result = arg1 % arg2
	print(f"Result: {result}")