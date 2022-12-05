def zad_3(*args):
    print(args)
    for i in args:
        print(i)
    print()

zad_3(3, 6, "str", 8.86, [3, 6, "str"])
zad_3("hello", 89)

def maximum(arg_1, *args):
    print(arg_1, args)
    k = arg_1
    for i in args:
        if i > k:               # <
            k = i
    return k

print(maximum(6, 0, -5, 68))
print(maximum(8.57, 6, 7.45, -5))
print(maximum("str", "anfi", "Hello"))
# print(maximum()) erorr
