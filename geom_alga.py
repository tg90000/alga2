#!/usr/bin/python3

import math
import numpy as np
import sys


def forgasirany(A, B, C):
	mat = np.array([np.subtract(B, A) , np.subtract(C, A)])
	mat = np.transpose(mat)

	return np.linalg.det(mat)

def metszoszakasz(A, B, C, D):
	return [forgasirany(A, B, C), forgasirany(A, B, D), forgasirany(C, D, A), forgasirany(C, D, B)]

def sopres(points):
	points = [p for p in sorted(points, key=lambda p: tuple(p))]
	print (points)

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
	tuple_dict = { tuple(p) : get_polar_coords(p, ref) for p in points }
	tuple_dict = {k: v for k, v in sorted(tuple_dict.items(), key=lambda item: tuple(item[1]))}	
	points = list(tuple_dict.keys())
	return np.asarray(points)

def CH_Graham(points):
	points = order_by_polar_coords(points)
	stack = [points[0], points[1], points[2]]
	stack_of_indicies = [0, 1, 2]
	point = points[4]
	i = 3
	steps = 0
	while True:
		steps+=1
		i = i % len(points)
		irany = forgasirany(stack[-2], stack[-1], points[i])
		if irany <= 0:
			stack.pop()
			stack_of_indicies.pop()
		else:
			if i in stack_of_indicies:
				stack_visible = [tuple(x) for x in stack]
				print ('{}. lepes:\n\t Forgasirany: {:.2f}\n\t Stack tartalma: {}\n\t'.format(steps, irany, stack_visible))
				print ('Algoritmus vege.')
				break
			stack.append(points[i])
			stack_of_indicies.append(i)
			i+=1
		stack_visible = [tuple(x) for x in stack]
		print ('{}. lepes:\n\t Forgasirany: {:.2f}\n\t Stack tartalma: {}\n\t'.format(steps, irany, stack_visible))

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
			print ('{}. lepes:\n\t Referencia pont valtasok szama: {}\n\t Stack tartalma: {}'.format(steps, change_counter, stack_visible))
			print ('Algoritmus vege.')
			break
		stack.append(points[index_of_last])
		stack_of_indicies.append(index_of_last)
		stack_visible = [tuple(x) for x in stack]
		print ('{}. lepes:\n\t Referencia pont valtasok szama: {}\n\t Stack tartalma: {}'.format(steps, change_counter, stack_visible))


if __name__ == '__main__':
	if sys.argv[1]=='help':
		print('Alga2 2. geom alga ZH solver.\nElso parameternek add meg, melyik feladatot szeretned megoldani,\nutana pedig sorban a pontok koordinatait rendre A1 A2 B1 B2 stb\n')
		print('Elso parameter:\n\t f: forgasirany\n\t m: metszo szakasz\n\t p: polar koordinatak szerinti rendezes\n\t j: Jarvis meneteles\n\t g: Graham-fele pasztazas\n\t s: sopres')
		exit(0)
	if len(sys.argv) != 8 and len(sys.argv) != 10 and len(sys.argv) != 18:
		print ('Megfelelo szamu koordinatat adj meg!\n\t Peldaul:\n\t ./geom_alga.py f 1 2 3 4 5 6\n\t Futtatas: forgasirany szamitas: A=(1,2) B=(3,4) C=(5,6) eseten.\n\t Csak 3, 4 vagy 8 pont lehetseges.')
		exit(1)
	args = [float(x) for x in sys.argv[2:]]

	if len(args)>0:
		A = np.array([args[0], args[1]])
		B = np.array([args[2], args[3]])
		C = np.array([args[4], args[5]])
	if len(args)>6:
		D = np.array([args[6], args[7]])
	if len(args)>8:
		E = np.array([args[8], args[9]])
		F = np.array([args[10], args[11]])
		G = np.array([args[12], args[13]])
		H = np.array([args[14], args[15]])

	if sys.argv[1]=='f':
		print ('{:.2f}'.format(forgasirany(A, B, C)))
	elif sys.argv[1]=='m':
		for x in metszoszakasz(A, B, C, D):
			print ('{:.2f}'.format(x))
	elif sys.argv[1]=='g':
		points = [A, B, C, D, E, F, G, H]	
		CH_Graham(points)	
	elif sys.argv[1]=='j':
		points = [A, B, C, D, E, F, G, H]
		CH_Jarvis(points)
	elif sys.argv[1]=='s':
		points = [A, B, C, D, E, F, G, H]
		sopres(points)
	elif sys.argv[1]=='p':
		stack_visible = [tuple(x) for x in order_by_polar_coords([A, B, C, D, E, F, G, H])]
		print (stack_visible)
	else:
		print('Elso parameter:\n\t f: forgasirany\n\t m: metszo szakasz\n\t p: polar koordinatak szerinti rendezes\n\t j: Jarvis meneteles\n\t g: Graham-fele pasztazas\n\t s: sopres')
