# strong number
from colorama import Fore

print("enter number:")
x = int(input())
t = x
sum = 0
while x > 0:
    a = x % 10
    i = 1
    k = 1
    while i < a + 1:
        k = i * k
        i += 1

    x = x // 10
    sum += k

if t == sum:
    print(Fore.CYAN + "strong number")
else:
    print(Fore.MAGENTA + "wrong")


