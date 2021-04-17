#fibonaci
print("number:")
x = int(input())
a = 0
b = 1
i = 2
print(b)
while i < x+1:
    c = a + b
    print(c)
    a = b
    b = c
    i = i+1
