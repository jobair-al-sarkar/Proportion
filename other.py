from math import pi

for i in range(5, 10):
    print(i*pi)


lst = [None]*10
start = 3
for i in range(start, len(lst)):
    lst[i] = 'Valid'
print(lst)
