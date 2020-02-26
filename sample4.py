a = list(map(int, input().split(",")))
print(a)
for i in a:
    q = ((2*50*i)/30)**0.5
    print(int(q), end =",")