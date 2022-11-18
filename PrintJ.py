for row in range(7):
	for colum in range(4):
		if ((row==0 and colum!=0) or (row==6 and colum!=3) or (colum==2 and colum!=0 and colum!=6) or (row==5 and colum<1)):
			print("*",end=" ")
		else:
			print(end="  ")
	print()