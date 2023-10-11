
import random
import math
import matplotlib.pyplot as plt

def piapprox(n):
    insidex = []
    insidey = []
    outsidex = []
    outsidey = []
    circlepoints = 0
    for _ in range(n):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        if rand_x**2 + rand_y**2 <= 1:
            insidex.append(rand_x)
            insidey.append(rand_y)
            circlepoints += 1
        else: 
            outsidex.append(rand_x)
            outsidey.append(rand_y)

    piresult = 4 * circlepoints / n

    plt.scatter(insidex, insidey, color = 'red')
    plt.scatter(outsidex, outsidey, color = 'blue')
    plt.show()
    
    return piresult
    
for n in [1000, 10000, 100000]:
    print(f"Final Estimation of Pi= {piapprox(n)}")
    print(f'Actual value of pi:{math.pi}')


# # Total Random numbers generated= possible x
# # values* possible y values

    # Randomly generated x and y values from a
    # uniform distribution
    # Range of x and y values is -1 to 1

 
    # Distance between (x, y) from the origin


 
    # Checking if (x, y) lies inside the circle
 
    # Estimating value of pi,
    # pi= 4*(no. of points generated inside the
    # circle)/ (no. of points generated inside the square)

 
##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
# print("\n")


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


def exact_hypersphere(n, d):
    r = 1
    Vd = (math.pi**(d/2)) / math.gamma((d/2)+1)*r**d
    return Vd

print(hypersphere(100000, 2))
print(exact_hypersphere(100000, 2))
print(hypersphere(100000, 11))
print(exact_hypersphere(100000, 11))

    
'list comprehension map lambda '

'skapa lista med random nummer mha list comp' 
'kolla villkoret, anävnd nån/ngra  nmetod'
'map applicera lambda funktionen på varje x' 
'sen summera '
'kolla om <= 1'
'isåfall plussa +1'

    
