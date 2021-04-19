# automorphic number
from colorama import Fore

print("enter number:")
x = int(input())
num = x
power = x * x
e = False
b = 10
while x > 0:
    a = power % b
    if a == num:
        e = True
        break
    x = x // 10
    b *= 10


if (e):
    print(Fore.CYAN + "automorphic number")
else:
    print(Fore.MAGENTA + "wrong")


