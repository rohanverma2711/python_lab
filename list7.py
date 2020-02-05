li = []
while True:
	item = input("enter the item ")
	li.append(item)
	li.sort(reverse = True, key = max)
	a = input("enter your choice ")
	if a.lower() == 'n':
		break
print(li)
