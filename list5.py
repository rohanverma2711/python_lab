li = []
while True:
	item = input("enter the item")
	li.append(item)
	a = input("enter your choice")
	if a.lower() == 'n':
		break
print(li)
