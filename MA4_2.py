#!/usr/bin/env python3.9

from person import Person
from  numba import njit
from time import perf_counter as pc 
import matplotlib.pyplot as plt

#creates function to calculate fib with only python
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

#creates function to calculate fib with numba. It translates the python code to c++ since it's faster	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	# f = Person(5)
	# print(f.get())
	# f.set(7)
	# print(f.get())

	fibnumba3045 = [i for i in range(30,45)] #uses list comprehension to create list with numbers between 30 and 45
	fibnumbatime3045 = [] #creates empty list
	for n in fibnumba3045: #for each number in the list, measures the time
		start = pc() #starts timer
		fib_numba(n) 
		end = pc() #ends timer
		fibnumbatime3045.append(end-start) #adds the data to list
	
	#plots the figure
	plt.plot(fibnumba3045, fibnumbatime3045, label = 'Time for numba')
	plt.xlabel('Fibonacci number')
	plt.ylabel('Time (s)')
	plt.legend(loc = 'upper left')
	plt.savefig('fib_numba_3045.png')
		
	fibc3045 = [i for i in range(30,45)]
	fibctime3045 = []
	for n in fibc3045:
		start = pc()
		f = Person(n)
		f.fibc()
		end = pc()
		fibctime3045.append(end-start)

	plt.plot(fibc3045, fibctime3045, label = 'Time for c++')
	plt.xlabel('Fibonacci number')
	plt.ylabel('Time (s)')
	plt.legend(loc = 'upper left')
	plt.savefig('fib_c++_3045.png')
	
	fibpy3045 = [i for i in range(30,40)] #40 since 45 is too big 
	fibpytime3045 = []
	for n in fibpy3045:
		start = pc()
		fib_py(n)
		end = pc()
		fibpytime3045.append(end-start)	

	plt.plot(fibpy3045, fibpytime3045, label = "Time for python")
	plt.xlabel('Fibonacci number')
	plt.ylabel('Time (s)')
	plt.legend(loc = 'upper left')
	plt.savefig('fib_py_3045.png')

	fibnumba2030 = [i for i in range(20,30)]
	fibnumbatime2030 = []
	for n in fibnumba2030:
		start = pc()
		fib_numba(n)
		end = pc()
		fibnumbatime2030.append(end-start)
	
	plt.plot(fibnumba2030, fibnumbatime2030, label = 'Time for numba')
	plt.xlabel('Fibonacci number (n)')
	plt.ylabel('Time (s)')
	plt.legend(loc = 'upper left')
	plt.savefig('fib_numba_2030.png')
	#the graph looks like it does since it must translate the code from python to c++ and therefore, it takes longer time in the beginning

	fibpy2030 = [i for i in range(20,30)] #40 since 45 is too big 
	fibpytime2030 = []
	for n in fibpy2030:
		start = pc()
		fib_py(n)
		end = pc()
		fibpytime2030.append(end-start)	

	plt.plot(fibpy2030, fibpytime2030, label = "Time for python")
	plt.xlabel('Fibonacci number (n)')
	plt.ylabel('Time (s)')
	plt.legend(loc = 'upper left')
	plt.savefig('fib_py_2030.png')	

	f = Person(20)
	print(f'Fibonacci when n is 47 with c++: {f.fibc()}')
	#It was 2971215073
	
	print(f'Fibonacci of 47 with numba: {fib_numba(20)}')
	#It was 2971215073
if __name__ == '__main__':

	main()

