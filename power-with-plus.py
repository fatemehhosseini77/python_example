x = int(input())
y = int(input())
sum = 0
temp = x
if x != 0:
    for i in range(1, y):
        sum = 0
        for j in range(1, x + 1):
            sum = temp + sum
        temp = sum

print("pow(x,y) is :", {sum})
