from time import perf_counter as pc
import concurrent.futures as futures
import random

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

def runner():
    hypersphere(10000000, 11) #ska va 10 milj


if __name__ == "__main__":
    start = pc()
    runner() #without parallell
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    
    start = pc()
    with futures.ProcessPoolExecutor() as ex: #with parallell    
        results = ex.map(hypersphere, [(1000000, 11) for _ in range(10)])
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")