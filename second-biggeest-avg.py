print("enter number of student")
n = int(input())
max1 = -1
max2 = -1
id1 = -1
id2 = -1
if n < 2:
    print("number of student not enough for find!!!")
else:
    for i in range(1, n + 1):
        print("Enter id of student:")
        id = int(input())
        print("Enter average:")
        avg = float(input())
        if avg > max1:
            id2 = id1
            max2 = max1
            max1 = avg
            id1 = id
        else:
            max2 = avg
            id2 = id
    print("two bigger avg is ", {max2}, "it is for id", {id2})
