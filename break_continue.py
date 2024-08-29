# Let’s write a loop that processes numbers from 1 to 10, skips multiples of 3, and stops processing if a number is greater than 7

for i in range(1,11):
    if i%3 == 0:
        continue
    if i>7:
        break
    print(i)
print("loop completed")
