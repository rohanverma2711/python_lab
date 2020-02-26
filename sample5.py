s = input()
sub = input()
l1 = len(s)
l2 = len(sub)
c = 0
for i in range(l1-l2+1):
    if s[i:i+l2] == sub:
        c+=1
print(c)