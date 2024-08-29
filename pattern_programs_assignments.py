"""
Floyd's triangle pattern
The Floyd's triangle is a right-angled triangle that contains
consecutive natural numbers, starting with a 1 in the top left corner.
"""
"""
1
2 3
4 5 6
7 8 9 10
"""
n=int(input("enter a number:"))
number=1
for i in range(1,n+1):
    for j in range(i):
        print(number,end=' ')
        number+=1
    print()

# Checkerboard Pattern
"""
The pattern typically contains two colours where a single checker
(that is a single square within the check pattern) is surrounded
on all four sides by a checker of a different colour.
"""
"""
B W B W
W B W B
B W B W
W B W B
"""
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2==0:
            print("B",end=' ')
        else:
            print("W",end=' ')
    print()
# Hollow Square star pattern
"""
* * * *
*     *
*     *
* * * *
"""
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n  or j == 1 or j == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Diamond Pattern
"""
    *
   ***
  *****
 *******
  *****
   ***
    *
"""
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(-n+1,n+1):
        if j<0:
            j=j*(-1)
        if i<=j:
            print(" ",end='')
        else:
            print("*",end='')
    print()
for i in range(n-1,0,-1):
    for j in range(-n+1,n+1):
        if j<0:
            j=j*(-1)
        if i<=j:
            print(" ",end='')
        else:
            print("*",end='')
    print()