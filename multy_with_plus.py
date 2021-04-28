x = int(input())
y = int(input())
sum = 0
if x == 0 or y == 0:
    raise ValueError("one of number is zero")
else:
    if y > 0:
        for i in range(1, y + 1):
            sum = x + sum
    if y < 0:
        y = -y
        for i in range(1, y + 1):
            sum = x + sum
        sum = -sum
    print("multi", x, "*", y, "is", sum)
