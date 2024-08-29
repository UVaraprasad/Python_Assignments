"""
Count Occurrences: Given a list and a target element,
count the occurrences of the target in the list.
"""
numbers = [1, 2, 3, 4, 5, 2, 2, 6, 7,2,5]
target = int(input("Enter the number to find the number of occurrence "))
cnt=0
for i in numbers:
    if i==target:
        cnt+=1

print("occurences:",cnt)


# Count and display vowels in a string
s1 = input("Enter the string to find the vowels in a string ")
cnt=0
for i in s1:
    if i == 'a' or i == 'e' or i == 'i' or i=='o' or i == 'u':
        cnt+=1
        print(i)
print("cnt:",cnt)


# Calculate the factorial of a number
n = int(input("Enter the number to calculate the factorial "))
j=1
for i in range(1,n+1):
    j=j*i

print("factorial:",j)

"""
A palindrome number is a number that remains the same when its digits are reversed.
For example, 121, 1331, 16461 are palindrome numbers, while 123 and 321 are not.
"""

n=int(input("enter a number:"))
m=n
sum=0
while 0<n:
    rem=n%10
    sum=sum*10+rem
    n//=10

if sum == m:
    print("palindrome")
else:
    print("not a palindrome")


# WAP to unlock the mobile device using a pattern
"""
User enters a correct password in 5 attempts, phone will be unlocked.
If a user enters an incorrect password for 5 attempts,
You have to wait for 30 seconds to try again.
This process repeats
"""
import time
password=1234
i=1
while i<6:
    up=int(input("enter a password:"))
    if up==password:
        print("mobile unlocked")
        break
    elif i==5:
        print("wait 30 sec")
        time.sleep(30)
        i=0
    else:
        print("password wrong")
        i+=1
