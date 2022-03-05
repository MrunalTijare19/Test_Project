
#WHILE LOOP:
#WAP to print first 10 number.

i=1
while i<10:
    print(i)
    i=i+1
print()


n=int(input('Enter number :'))
for i in range(1,n):
    for j in range(1,n-i):
        print('  ',end='')
    for j in range(1,i+i):
        print('*',end='  ')
    print()

n=int(input('Enter number :'))
for i in range(0,n+1,1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print('*',end="")
    print()
print()

n=int(input("Enter Number: "))
for i in range(0,n,1):
    for j in range(0,n-i):
        print("  ",end=" ")
    for j in range (1,i+1):
        print( j,end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,n-i):
        print("  ",end=" ")
    for j in range (1,i+1):
        print(j,end=" ")
    print()
print()

n=int(input("Enter Number: "))
for i in range(0,n+1,1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for j in range (1,i+1):
        print("*",end=" ")
    print()
