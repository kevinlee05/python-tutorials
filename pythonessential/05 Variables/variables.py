  #!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
	d = dict (
			one = 1, two = 2, three = 3, four = 41234, five = 'five'
		)
	print(d)
	d['seven'] = 777
	print(d)
	sorted(d)
	print(sorted(d))

if __name__ == "__main__": main()
