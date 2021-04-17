#find large number
print("Enter number of element:")
x = int(input())
a = []
for i in range(0 , x):
    print("Enter element : ")
    n = int(input())
    a.append(n)
a.sort()
print("This is a large number in list", a[x-1])


