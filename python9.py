a = (1,3,2,3,4,5,6,6,6)
b = []
for i in a:
    if a.count(i) > 1 and i not in a:
        print(i)
        b.append(i)