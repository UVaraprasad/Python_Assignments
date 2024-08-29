"""
1. Array and String Manipulation
Question: Given an array of integers, write a function that
returns the array with all zeros moved to the end while
maintaining the relative order of the non-zero elements.
input: [2, 0, 1, 34, 0, 900]
output: [2, 1, 34, 900, 0, 0]
"""
a = [2, 0, 1, 34, 0, 900]
l = len(a)
j = 0
print(a)
for i in a:
    if i != 0:
        a[j] = i
        j += 1
for k in range(j, l):
    a[k] = 0
print(a)

# write a Python program to find the fibonacci series using recursive and non recursive functions

def fibonacci(n):
    a=0
    b=1
    c=0
    while a < n:
        print(a,end='')
        c=a+b
        a, b = b, c


n = 10
fibonacci(n)


print()
def fibonacci_rec(n, a=0, b=1):
    if a > n:
        return
    print(a,end='')
    fibonacci_rec(n, b, a + b)


n = 10
fibonacci_rec(n)


