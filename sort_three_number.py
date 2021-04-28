x = int(input())
y = int(input())
z = int(input())
n = 0
while n < 3:
    if x > y:
        temp = x
        x = y
        y = temp

    if y > z:
        temp = y
        y = z
        z = temp
    if x > z:
        temp = x
        x = z
        z = temp
    n += 1

print("sorted three number", x, y, z)
