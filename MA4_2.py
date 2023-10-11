#!/usr/bin/env python3.9

from person import Person
from  numba import njit
from time import perf_counter as pc
from time import sleep as pause 

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
		return(fib_py(n-1) + fib_py(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

	f = Person(5)
	print(f.fib())






if __name__ == '__main__':

	start = pc()
	py = fib_py()
	end = pc()

	start = pc()
	numba = fib_numba()
	end = pc()

	start = pc()
	c = Person.fib()
	end = pc()

	print(py)
	print(numba)
	print(c)

	main()

