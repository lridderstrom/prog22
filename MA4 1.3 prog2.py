from time import perf_counter as pc
import concurrent.futures as futures
import random

#same as in 1.2
def hypersphere(n, d): 
    spherepoints = 0

    for _ in range(n):
        lst = [random.uniform(-1,1) for _ in range(d)]
        points = list(map(lambda x : x**2, lst))
        summa = sum(x for x in points)
        if summa <= 1:
            spherepoints += 1
    
    volume = (spherepoints/n) * (2**d)
    return volume

#creates function that calls on hypersphere and calculates volume
def runner():
    hypersphere(10000000, 11) #ska va 10 milj


if __name__ == "__main__":
    #Measures how long it takes to calculate without multiprocessing
    start = pc()
    runner() #without parallell
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    
    #Measures time for how long it takes to calculate with multiprocessing
    start = pc()
    with futures.ProcessPoolExecutor() as ex: #with parallell    
        results = ex.map(hypersphere, [(1000000, 11) for _ in range(10)]) #does it ten times 
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

    #Multiprocessing is faster since it uses the computers cores at the same time