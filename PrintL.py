for row in range(7):
	for colum in range(4):
		if colum==0 or row==6 and colum!=6:
			print("*",end=' ')
		else:
			print(end=' ')
	print()