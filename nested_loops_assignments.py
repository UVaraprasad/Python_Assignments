# Find all prime numbers between 2 and n
"""
The standard definition of prime numbers applies only to
positive integers greater than 1. A prime number is defined
as a number that has only two distinct positive divisors: 1 and itself.
For example, 2, 3, 5, 7, 11, etc. are prime numbers
because they can only be divided evenly by 1 and themselves
without leaving a remainder.
"""
n = int(input("Enter a number: "))
if n<=1:
    print("invalid value")
    exit()
for i in range(2, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i)


# Print multiplication tables from 1 to n
"""
Let's say if user inputs 9, you need to generate 1 to 9 tables
"""
n= int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()
