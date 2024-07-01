# What will be the output of following statements
print({1, 2, 3, 5} - {3, 4, 7, 8})# {1,2,5}
print({1, 2, 3, 5} + {3, 4, 7, 8})# error sets not accepts for '+'

# What will be the output of following programs
print('Hi ' + 'Anil')# Hi Anil
print([1, 2] + [3, 4])# [1,2,3,4]
print('Hi' + [1, 2])# error list not concatenate

# What will be the output of following programs
print((1, 2, 3) * 4)# (1,2,3,1,2,3,1,2,3,1,2,3)
print(8 // 3)# 2
print(21 % 6)# 3

# What will be the output of following programs
a = 7
a /= 2
print(a)# 3.5
b = 5
print(b > 5 and b < 10)# Also write the short form for this expression
                       # False (5 < b < 10)short form expression
print(5 < b < 10)# False

# Write the output of following programs
print(4 and 6)# 6
print(1 or 5)# 1
print(not 7)# False

# what is the output of following programs
print(2 not in [3, 4, 5, 2, 9])# False
print([1, 2, 5, (1, 2)] in ['hi', 3, 4, 5, 2, 9, [1, 2, 5, (1, 2)]])# True

# what is the output of following programs
a = 400.30123
b = 400.30123
print(a is b)# False

i = 23
j = 23
print(i is j)# True
print(i == j)# True

a1 = 999
b1 = 999
print(a1 is b1)# False
print(a1 == b1)# True

y = 4
z = -4
print(y == z)# False

s1 = 4096 * 'a'
s2 = 4096 * 'a'
print(s1 is s2)# True

# write the output of following programs
a = 2
b = 11
print(a & b)# 2
print(a | b)# 11
print(a ^ b)# 9
print(~b)# -12
print(a << 3)# 16
print(b >> 2)# 2

# write the output of following programs
print(+-4)# -4
print(--4)# 4
a = [1, 2, 3]
print(2 * a[1] << 2 > 8 and 9)# 9
print(2 * 3 - 3 ** 2 ** 1 & 5 // 2 + (4 + 2) or 5)# 8
