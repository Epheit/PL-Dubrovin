a = int(input())
b = int(input())
if a <= b:
    for i in range(a, b + 1):
        print(i)

n = int(input())
if n <=9:
    if n <0:
        for i in range(1,n-1, -1):
            for p in range(i):
                print(i)
else:
    for i in range(1,n+1, 1):
        for p in range(i):
            print(i)

a = int(input())
b = int(input())
if a <b:
    for i in range(a,b+1,1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

n = int(input())
p = 0
for i in range(1,n+1):
    p+=i**3
    print(p)