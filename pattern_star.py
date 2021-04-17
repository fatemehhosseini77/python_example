
print("------------RECTANGLE------------")
withRec = input("Enter width :")
heightRec =input ("Enter height:")
for i in range ( 0 ,int( heightRec)):
    for j in range( 0 ,int(withRec)):
        print("*" ,end = " ")
    print ("\r")


print ("-----------TRIANGLE1--------------")
numberStr = input( " Enter number :")
for i in range (0 ,int(numberStr)):
   for j in range ( 0 , int(numberStr)):
       if j > i :
            print("*" ,end = " ")
   print (" ")



print ("-----------TRIANGLE2--------------")
numberStr = input( " Enter number :")
for i in range (0 ,int(numberStr)):
   for j in range ( 0 , int(numberStr)):
       if i > j :
            print("*" ,end = " ")
   print (" ")
    

print ("-----------Diamond--------------")
n = int (input( " Enter number :"))
k=0
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end="  ")
    while k!=(2 * i - 1):
        print("*",end=" ")
        k=k+1
    
    k=0
    print(" ")
a=1
k=1
for i in range(1,n):
    for j in range(1,a+1):
        print(end="  ")
    a=a+1
    while k<(2*(n-i)):
        print("*",end=" ")
        k=k+1
    k=1
    print(" ")




