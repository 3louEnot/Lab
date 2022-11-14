array = list("qwertyuiopasdfghjklzxcvbnm")
array_2 = list("QWERTYUIOPASDFGHJKLZXCVBNM")
user = input("Litera: ")
cycle = -1
for i in array:
	cycle = cycle + 1
	if user == i:
		print(array_2[cycle])
		break
	elif user != i:
		continue
cycle = -1
for i in array_2:
	cycle = cycle + 1
	if user == i:
		print(array[cycle])
		break
	elif user != i:
		continue