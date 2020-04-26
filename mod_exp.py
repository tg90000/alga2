#!/usr/bin/python3

import sys


def to_binary(num):
	if num == 0:
		return '0'

	binary = []
	while num > 0:
		binary.insert(0, num % 2)
		num >>= 1
		
	return ''.join(str(integer) for integer in binary)


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('3 értéket adj meg, az alapot (a), a kitevőt (b) és az osztót (n).')
		
		exit(1)
		
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	n = int(sys.argv[3])
	
	print('Beolvasott érték {}^{} mod {}'.format(a, b, n))
	
	binary = to_binary(b)
	
	print('Az a bináris értéke: {}'.format(binary))
	
	d = 1
	counter = 1
	
	for integer in binary:
		d = (d ** 2) % n
		
		if integer == '1':
			d = (d * a) % n
		
		print('{}. iteráció végén a d értéke: {}'.format(counter, d))
		counter += 1
	
	print('A kifejezés értéke: {}'.format(d))