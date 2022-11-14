deszcz = input("Tym czy pada? Y\\n: ")
bus = input("Czy jest autobus? Y\\n: ")
if (deszcz == "Y" or deszcz == "y") and (bus == "Y" or bus == "y"):
	print("Weź parasol, dostaniesz się na uczelnie")
elif (deszcz == "Y" or deszcz == "y") and (bus == "N" or bus == "n"):
	print("Nie dostaniesz się na uczelnię")
elif (deszcz == "N" or deszcz == "n") and (bus == "Y" or bus == "y"):
	print("Dostaniesz się na uczelnie, miłego dnia i pięknej pogody")
else:
	print("Error")