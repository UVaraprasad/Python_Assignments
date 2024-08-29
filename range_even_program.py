# WAP to print even numbers from 1 to 25 using the range
print("even numbers:",end='')
for i in range(1,26):
    if i%2 == 0:
        print( i, end=' ')