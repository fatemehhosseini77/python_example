#prime number
print("Enter a number:")
x = int(input())
if x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print("not prime!")
            break
    else:
         print("prime!!")
