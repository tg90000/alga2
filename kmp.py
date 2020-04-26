#!/usr/bin/python3

import sys


def create_prefix_array(pattern):
	res = [0]

	for index in range(2, len(pattern) + 1):
		val = pattern[:index]
		suffixes = [val[startIndex:] for startIndex in range(1, len(val))]
		
		for suffix in suffixes:
			if pattern.startswith(suffix):
				res.append(len(suffix))
				
				break
		else:
			res.append(0)
	
	return res


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('2 értéket adj meg, a bemenetet (S) és a mintát (P)')
		
		exit(1)
		
	input = sys.argv[1]
	pattern = sys.argv[2]
	
	print('A szöveg: {}'.format(input))
	print('A minta: {}'.format(pattern))
	
	prefix_array = create_prefix_array(pattern)
	
	print('A prefix függvény értékei: {}'.format(prefix_array))
	
	pattern_index = 0
	matches = []
	
	for index in range(0, len(input)):
		print('{}. iteráció:'.format(index + 1))
		print('Az i értéke: {}. A j értéke: {}'.format(index + 1, pattern_index))
		
		match = input[index] == pattern[pattern_index]
		
		print('bemenet[i] == minta[j+1]: {}'.format('igen' if match else 'nem'))
	
		if match:
			pattern_index += 1
		else:
			pattern_index = prefix_array[pattern_index]

		if pattern_index == len(pattern):
			matches.append(index - pattern_index + 2)
			pattern_index = prefix_array[pattern_index - 1]
	
	print('Egyezések (Az indexek 1-től vannak számozva!!!):')
	
	for match in matches:
		print('Egyezés az i = {} indextől'.format(match))