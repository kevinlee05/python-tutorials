a,b,i = 0,1,1
while b < 50:
	print(b)
	print('loop number {}'.format(i) )
	a,b = b, a + b
	i = i + 1
print('Done')