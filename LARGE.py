n = int(input())
for i in range(n):
    L1 = [int(i) for i in input().split() ]
    max1= max(L1)
    max2 = 0
    for i in L1 :
        if int(i) != max1 and i > max2:
            max2 = i
    print(max2)
