#!/usr/bin/env python3.9

from person import Person
from  numba import njit
from time import perf_counter as pc 

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

	for x in range(30, 45):
		f = Person(x)
		print(f.fib())






if __name__ == '__main__':
	for i in range(30, 45):
		start = pc()
		fib_py(i)
		end = pc()
		print(f'Python took {round(end-start, 2)} seconds ')

		start = pc()
		fib_numba(i)
		end = pc()
		print(f'Numba took {round(end-start, 2)} seconds ')

		start = pc()
		Person.fib()
		end = pc()
		print(f'C++ took {round(end-start, 2)} seconds ')

	main()

