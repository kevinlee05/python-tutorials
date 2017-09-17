a,b = 9,5
if a < b:
	print('a ({}) is less than b ({})'.format(a,b))
else:
	print('a ({}) is not less than b ({})'.format(a,b))

print("a < b" if a < b else "a not < b")