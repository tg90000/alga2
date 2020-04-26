#!/usr/bin/python3

import sys
from tabulate import tabulate


def get_suffixes(word):
	return [word[startIndex:] for startIndex in range(1, len(word))]


def get_suffix_at_start(pattern, word):
	suffixes = get_suffixes(word)
	
	for suffix in suffixes:
		if pattern.startswith(suffix):
			return len(suffix)
	
	return 0


def create_state(pattern, index, sigma):
	obj = {}
	obj['state'] = index
	
	for char in sigma:
		if index < len(pattern) and char == pattern[index]:
			obj[char] = index + 1
		else:
			word = '{}{}'.format(pattern[:index], char)
			
			obj[char] = get_suffix_at_start(pattern, word)
	
	return obj

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('2 értéket adj meg, a bemenetet (S) és a mintát (P).')
		
		exit(1)

	input = sys.argv[1]
	pattern = sys.argv[2]
	
	print('Beolvasott bemenet: {}'.format(input))
	print('Beolvasott minta: {}'.format(pattern))
	
	sigma = sorted(list(set(pattern)))
	table = []
	
	for index in range(0, len(pattern) + 1):
		table.append(create_state(pattern, index, sigma))
	
	dict = { i : i for i in sigma}
	dict['state'] = '/'
	
	printable_table = []
	
	for row in table:
		new_row = { key: 'q{}'.format(value) for key, value in row.items() }
		printable_table.append(new_row)
	
	print('--------------------------------------')
	print('Állapot átmenet függvény táblázatosan:')
	print(tabulate(printable_table, headers=dict))
	
	table_header = [str(num) for num in range(0, len(input) + 1)]
	table_header.insert(0, 'i')
	
	first_row = [char for char in input]
	first_row.insert(0, '')
	first_row.insert(0, 'S[i]')
	
	res = ['qi', 'q0']
	state = 0
	
	for letter in input:
		state = table[state][letter]
		res.append('q{}'.format(state))
	
	print('-------------------------------------')
	print('Az algoritmus futását leíró táblázat:')
	print(tabulate([first_row, res], headers=table_header))
	