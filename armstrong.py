# armstrong number
from colorama import Fore
print("enter number:")
x = int(input())
t = x
sum = 0
count = 1
while True:
    x = x / 10
    count += 1
    if x < 10:
        break

k = t
while t > 0:
    a = (t % 10)

    a = pow(a, count)

    sum += a
    t = t // 10

if k == sum:
    print(Fore.CYAN + "armstrong number")
else:
    print(Fore.MAGENTA + "wrong")

