l1 = l3 = list(map(int, input().split()))
l2 = l4 = list(map(int, input().split()))
l = [l1.append(i) for i in l2 if i not in l2]
lk = [ i for i  in l3 if i in l4]
sy = [ i for i in l if i not in lk]
print(lk)