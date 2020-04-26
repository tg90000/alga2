#!/usr/bin/python3

import sys

def h(val, q):
	return val % q
	
if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('3 értéket adj meg, az input (T), a minta (P) és a modulus a hasító függvényben (Q)')
		
		exit(1)
		
	input = sys.argv[1]
	pattern = sys.argv[2]
	q = int(sys.argv[3])
	
	print('A szöveg: {}'.format(input))
	print('A minta: {}'.format(pattern))
	print('A hasító függvény: x mod {}'.format(q))
	
	pattern_length = len(pattern)
	pattern_hash = h(int(pattern), q)
	
	print('A minta hash-e: {}'.format(pattern_hash))
	
	for index in range(0, len(input) - pattern_length + 1):
		current_input = input[index:index+pattern_length]
		hash = h(int(current_input), q)
		
		print('Vizsgált szöveg: {}'.format(current_input))
		print('\tA hash-e: {}'.format(hash))
		print('\tEgyezik a hash' if hash == pattern_hash else '\tNEM egyezik a hash')
	else:
		hash = h(10 * (hash - h(100, q) * int(current_input[0])), q)
		diff = pattern_hash - hash
		
		print('Vizsgált szöveg: {}y'.format(current_input[1:]))
		print('\tAhhoz hogy egyezzen a hash, az y értéke: {}'.format(diff if diff >= 0 else h(diff, q)))