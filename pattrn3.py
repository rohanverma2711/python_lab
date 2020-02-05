space=1
for i in range(1,6):
	if(i!=1):
		print(' '*(5-i),'*',' '*space,'*',sep='')
        space=space+2
 else:
		print(' '*(5-i),'*',sep='')
