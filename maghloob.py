x = int(input())
t = x
sumation = 0
count = 1
while True:
    x = x / 10
    count += 1
    if x < 10:
        break

y = t
for i in range(count, 0, -1):
    k = t % 10 * pow(10, i - 1)
    sumation = k + sumation
    t = t // 10

print("number is :", y)
print("inverse number is :", sumation)

if sumation == y:
    print("maghloob")
else:
    print("not!!")
