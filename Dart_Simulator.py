

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###
def for_pi(n):
    '''Shows the number of 'hits' out of the number of throws and returns
    the 'pi' and then returns the end estimate of pi'''
    acc = 0
    for i in range(1, n+1):
        if throw_dart() == True:
            acc += 1
            result = (acc * 4) / i
            print(acc, 'out of', i, 'is', result)
        else:
            result = (acc * 4) / i
            acc += 0
            print(acc, 'out of', i, 'is', result)
    return print(result)

def while_pi(error):
    acc = 0
    i = 0
    pi = 0
    while abs(math.pi - pi) > error:
        if throw_dart() == True:
            acc += 1
            i +=  1
            pi = (acc * 4) / i
            print(acc, 'out of', i, 'is', pi)
        else:
            i += 1
            pi = (acc * 4) / i
            print(acc, 'out of', i, 'is', pi)
    print(i)
        


            
    
            
