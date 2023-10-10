#!/usr/bin/env python3.9

from person import Person
from  numba import njit
import time 

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


def runner_py(n):
	for _ in range()


if __name__ == '__main__':
	main()
