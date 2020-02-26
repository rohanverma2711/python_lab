a = list(map(int, input().split()))
l = len(a)
b = []
c = []
for i in a:
    if i != 0:
        b.append(i)
    else:
        c.append(i)
print(b+c)


