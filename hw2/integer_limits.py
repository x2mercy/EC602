
Table="{:<6}{:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for i in range(1,9):
	x0=i
	x1=2**(8*i)-1
	x2=-2**(8*i-1)
	x3=2**(8*i-1)-1
	i=i*2;
	print(Table.format(x0,x1,x2,x3))