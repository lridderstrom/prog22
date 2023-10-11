
import random
import math
import matplotlib.pyplot as plt

def piapprox(n):
    insidex = [] #creates empty lists
    insidey = []
    outsidex = []
    outsidey = []
    circlepoints = 0 #starts a counter for how many points are inside circle
    for _ in range(n): #starts for loop
        rand_x = random.uniform(-1, 1) #creates random number between -1 and 1
        rand_y = random.uniform(-1, 1)
        if rand_x**2 + rand_y**2 <= 1: #checks if point is inside circle (uses distance to middle)
            insidex.append(rand_x) #if it is, add to empty list
            insidey.append(rand_y)
            circlepoints += 1 #count the point
        else: 
            outsidex.append(rand_x) #if it's not, add to list for outside circle
            outsidey.append(rand_y)

    piresult = 4 * circlepoints / n #gives estimation for pi

    # creates scatter plot with red points for inside of circle and blue for outside
    plt.scatter(insidex, insidey, color = 'red') 
    plt.scatter(outsidex, outsidey, color = 'blue')
    plt.show()
    
    return piresult

#prints approximation and actual value of pi for each n
for n in [1000, 10000, 100000]:
    print(f"Final Estimation of Pi= {piapprox(n)}")
    print(f'Actual value of pi:{math.pi}')


def hypersphere(n, d): 
    spherepoints = 0 #adds counter

    for _ in range(n): #creates for loop
        lst = [random.uniform(-1,1) for _ in range(d)] #uses list comprehension to create a list with d random numbers between -1 and 1
        points = list(map(lambda x : x**2, lst)) #map repeats the function lambda on each x in the list, lambda creates the function (like f(x))
        summa = sum(x for x in points) #sums all values for x in the list
        if summa <= 1: #If the sum is less than one
            spherepoints += 1 #adds +1 to counter 
    
    volume = (spherepoints/n) * (2**d) #estimates volume
    return volume 


def exact_hypersphere(n, d): #calculates true volume
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

    
