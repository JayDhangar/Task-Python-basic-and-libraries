def f1(a):
    return a + 1

def f2(b):
    return b + 2

def f3(c):
    return c - 1

a = int(input("Give me a number:"))
value1 = f1(a)
value2 = f2(value1)
final_value = f3(value2)
print("Final Output:", final_value)
