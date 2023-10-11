#!/usr/bin/env python3.9

from person import Person
from  numba import njit
from time import perf_counter as pc 
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())


if __name__ == '__main__':

	fibnumba3045 = [i for i in range(30,45)]
	fibnumbatime3045 = []
	for n in fibnumba3045:
		start = pc()
		fib_numba(n)
		end = pc()
		fibnumbatime3045.append(end-start)
	
	plt.plot(fibnumba3045, fibnumbatime3045, label = 'Time for numba')
		
	fibc3045 = [i for i in range(30,45)]
	fibctime3045 = []
	for n in fibc3045:
		start = pc()
		f = Person(n)
		f.fibc()
		end = pc()
		fibctime3045.append(end-start)

	plt.plot(fibc3045, fibctime3045, label = 'Time for c++')

	fibpy3045 = [i for i in range(30,40)] #40 since 45 is too big 
	fibpytime3045 = []
	for n in fibpy3045:
		start = pc()
		fib_py(n)
		end = pc()
		fibpytime3045.append(end-start)	

	plt.plot(fibpy3045, fibpytime3045, label = "Time for python")

	main()

