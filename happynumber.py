# happy number
from colorama import Fore
print("enter number:")
t = int(input())
sum = 0
while sum != 1 and sum != 4:
    sum = 0
    while t > 0:
        z = t % 10
        sum += pow(z, 2)
        t //= 10
    t = sum
if sum == 1 or sum == 4:
    print(Fore.CYAN + "happy number")
else:
    print(Fore.MAGENTA + "wrong")

