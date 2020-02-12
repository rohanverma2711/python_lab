l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l = [ i for i  in l1 if i in l2]
print(l)11