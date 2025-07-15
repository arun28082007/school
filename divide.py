def val(m, n):
    for i in range(n):
        if m[i] % 5 == 0:
            m[i]/=7
        if m[i] % 2 == 0:
            m[i]/=3
l = [21,8,75,12]
val(l, 4)
for i in range(len(l)):
    print(l[i], end=' ')
# This code modifies a list by dividing elements by 7 if they are divisible by 5,
# and by 3 if they are even, then prints the modified list. 