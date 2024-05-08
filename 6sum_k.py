# Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

a = [1, 5, 7, -1]
k = 6

c = 0
f = {}

for n in a:
    c += f.get(k - n, 0)
    f[n] = f.get(n, 0) + 1

print(c)
