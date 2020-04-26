#!/usr/bin/python3

from string import ascii_uppercase
import math
import numpy as np
import sys


def forgasirany(A, B, C):
	mat = np.array([np.subtract(B, A) , np.subtract(C, A)])
	mat = np.transpose(mat)

	return np.linalg.det(mat)

def metszoszakasz(A, B, C, D):
	return [forgasirany(A, B, C), forgasirany(A, B, D), forgasirany(C, D, A), forgasirany(C, D, B)]

def sopres_prior(index, points):
	point = points[index]
	return point[0], index % 2, point[1]

def sopres_rendezes(points):
	tuple_dict = { i : sopres_prior(i, points) for i in range(len(points))}
	point_indicies = [k for k, v in sorted(tuple_dict.items(), key=lambda item: tuple(item[1]))]
	return point_indicies

def metszo_bool(A, B, C, D):
	t1, t2, t3, t4 = metszoszakasz(A, B, C, D)
	if t1*t2 < 0 and t3*t4 < 0:
		return True
	return False

def add_to_sorted_Q(index_of_point, queue, points):
	index = 0
	for l in queue:
		if forgasirany(points[l[0]], points[l[1]], points[index_of_point]) > 0:
			index += 1
	queue.insert(index, [index_of_point, index_of_point+1])
	return queue, index

def get_point(index_of_point, queue, points):
	index = 0
	for x in queue:
		if x[0]==index_of_point or x[1]==index_of_point:
			break
		index += 1
	return index

def sopres(points):
	ordered = sopres_rendezes(points)
	queue = []
	steps=0
	for i in ordered:
		steps+=1
		print ('{}. lepes:'.format(steps))
		if i%2!=0:
			metszo = False
			index = get_point(i, queue, points)
			if index > 0 and index < len(queue)-1:
				A = points[queue[index-1][0]]
				B = points[queue[index-1][1]]
				C = points[queue[index+1][0]]
				D = points[queue[index+1][1]]
				metszo = metszo_bool(A, B, C, D)
				indicies = [queue[index-1][0], queue[index-1][1], queue[index+1][0], queue[index+1][1]]
				_letters = letters(indicies)
				szoveg = '\t{}{} {}{} es {}{} {}{} metszik egymast!'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D)) if metszo else '\t {}{} és {}{} nem metszok.'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D))
				print(szoveg)
			else:
				print('\t Nem kellett vizsgalni.')
			queue.pop(index)		
		else:
			queue, index = add_to_sorted_Q(i, queue, points)
			A = points[queue[index][0]]
			B = points[queue[index][1]]
			if (index > 0):
				C = points[queue[index-1][0]]
				D = points[queue[index-1][1]]
				metszo = metszo_bool(A, B, C, D)
				indicies = [queue[index][0], queue[index][1], queue[index-1][0], queue[index-1][1]]
				_letters = letters(indicies)
				szoveg = '\t{}{} {}{} es {}{} {}{} metszik egymast!'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D)) if metszo else '\t {}{} és {}{} nem metszok.'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D))
				print (szoveg)
					
			else:
				print ('\t Elso pont.')
			if (index < len(queue)-1):
				C = points[queue[index+1][0]]
				D = points[queue[index+1][1]]
				metszo = metszo_bool(A, B, C, D)
				indicies = [queue[index][0], queue[index][1], queue[index+1][0], queue[index+1][1]]
				_letters = letters(indicies)
				szoveg = '\t{}{} {}{} es {}{} {}{} metszik egymast!'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D)) if metszo else '\t {}{} és {}{} nem metszok.'.format(_letters[0], tuple(A), _letters[1], tuple(B), _letters[2], tuple(C), _letters[3], tuple(D))
				print(szoveg)
			else: 
		
				print('\t Utolso pont.')
	print ('Algoritmus vege.')

def get_polar_coords(point, ref):
	point_from_ref = np.subtract(point, ref)
	angle = math.atan2(point_from_ref[1], point_from_ref[0])
	distance = math.hypot(point_from_ref[0], point_from_ref[1])
	if distance == 0:
		angle -= 4 # less than -pi as the ref point has to be the first
	return angle, distance	

def order_by_polar_coords(points):
	# using the first point as reference
	ref = points[0]
	tuple_dict = { x : get_polar_coords(points[x], ref) for x in range(len(points)) }
	tuple_dict = {k: v for k, v in sorted(tuple_dict.items(), key=lambda item: tuple(item[1]))}	
	points = list(tuple_dict.keys())
	return points

def CH_Graham(points):
	indicies = order_by_polar_coords(points)
	stack = [points[indicies[0]], points[indicies[1]], points[indicies[2]]]
	stack_of_indicies = [indicies[0], indicies[1], indicies[2]]
	point = points[indicies[4]]
	i = 3
	steps = 0
	while True:
		steps+=1
		i = i % len(points)
		irany = forgasirany(stack[-2], stack[-1], points[indicies[i]])
		if irany <= 0:
			stack.pop()
			stack_of_indicies.pop()
		else:
			if indicies[i] in stack_of_indicies:
				stack_visible = [tuple(x) for x in stack]
				stack_letters = letters(stack_of_indicies)
				print ('{}. lepes:\n\t Forgasirany: {:.2f}\n\t Stack tartalma: {}\n\t Stack tartalma: {}'.format(steps, irany, stack_visible, stack_letters))
				print ('Algoritmus vege.')
				break
			stack.append(points[indicies[i]])
			stack_of_indicies.append(indicies[i])
			i+=1
		stack_visible = [tuple(x) for x in stack]
		stack_letters = letters(stack_of_indicies)
		print ('{}. lepes:\n\t Forgasirany: {:.2f}\n\t Stack tartalma: {}\n\t Stack tartalma: {}'.format(steps, irany, stack_visible, stack_letters))

def CH_Jarvis(points):
	stack = [points[0]]
	stack_of_indicies = [0]
	index_of_last = 0
	steps = 0	
	while True:
		steps += 1
		change_counter = 0
		index_of_last = (index_of_last + 1) % len(points)
		for x in range(len(points)):
			if forgasirany(stack[-1], points[x], points[index_of_last]) < 0:
				change_counter += 1
				index_of_last = x
		if index_of_last in stack_of_indicies:
			stack_visible = [tuple(x) for x in stack]
			stack_letters = letters(stack_of_indicies)
			print ('{}. lepes:\n\t Referencia pont valtasok szama: {}\n\t Stack tartalma: {}\n\t Stack tartalma: {}'.format(steps, change_counter, stack_visible, stack_letters))
			print ('Algoritmus vege.')
			break
		stack.append(points[index_of_last])
		stack_of_indicies.append(index_of_last)
		stack_visible = [tuple(x) for x in stack]
		stack_letters = letters(stack_of_indicies)
		print ('{}. lepes:\n\t Referencia pont valtasok szama: {}\n\t Stack tartalma: {}\n\t Stack tartalma: {}'.format(steps, change_counter, stack_visible, stack_letters))

def letters(indicies):
	dict_of_letters = {index: letter for index, letter in enumerate(ascii_uppercase, start=0) if index in indicies}
	ret = list(map(lambda x: dict_of_letters[x], indicies))
	return ret

if __name__ == '__main__':
	if sys.argv[1]=='help':
		print('Alga2 2. geom alga ZH solver.\nElso parameternek add meg, melyik feladatot szeretned megoldani,\nutana pedig sorban a pontok koordinatait rendre A1 A2 B1 B2 stb\n')
		print('Elso parameter:\n\t f: forgasirany\n\t m: metszo szakasz\n\t p: polar koordinatak szerinti rendezes\n\t j: Jarvis meneteles\n\t g: Graham-fele pasztazas\n\t s: sopres')
		exit(0)
	args = [float(x) for x in sys.argv[2:]]

	points = [np.array([args[i], args[i+1]]) for i in range(0, len(args), 2)]	
	if sys.argv[1]=='f':
		irany = forgasirany(points[0], points[1], points[2])
		print ('{:.2f}'.format(irany))
	elif sys.argv[1]=='m':
		for x in metszoszakasz(points[0], points[1], points[2], points[3]):
			print ('{:.2f}'.format(x))
	elif sys.argv[1]=='g':	
		CH_Graham(points)	
	elif sys.argv[1]=='j':
		CH_Jarvis(points)
	elif sys.argv[1]=='s':
		sopres(points)
	elif sys.argv[1]=='p':
		stack_visible = [tuple(points[x]) for x in order_by_polar_coords(points)]
		stack_indicies = [x for x in order_by_polar_coords(points)]
		stack_letters = letters(stack_indicies)
		print (stack_visible)
		print (stack_letters)
	else:
		print('Elso parameter:\n\t f: forgasirany\n\t m: metszo szakasz\n\t p: polar koordinatak szerinti rendezes\n\t j: Jarvis meneteles\n\t g: Graham-fele pasztazas\n\t s: sopres')
