l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l = [l1.append(i) for i in l2 if i not in l2]
print(l1)