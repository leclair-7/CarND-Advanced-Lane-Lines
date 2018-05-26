



def radiusOfCurvature(point):
	'''
	We know from math that the radius of curvature is:
	
		r = ( (1 + (dy/dx)**2 ) ** 1.5 )/ abs(y'')

		(Of course all evaluated at the same point, duh)
	'''

	y = lambda x: 2 * x ** 3 - x + 3
	y_prime = lambda x : 6*x**2 -1
	y_prime_prime = lambda x: 12 * x

	r = lambda x: ((1 + y_prime(x)**2)**1.5) /y_prime_prime(x)

	return r(point)

def getCenterPoint(point):


	m2 = -1. / y_prime


'''
print(radiusOfCurvature(1))

a = lambda x: -1* x / 5 + 21./5
print(a(-9.83))

print(a(11.84))
'''

from sympy import *
import numpy as np
x = Symbol('x')
y = 2 * x**3 - x + 3
y_prime = diff(y,x)
y_2prime = diff(y,x,2)

print(y_prime)
print(y_2prime)
print(y_prime.subs(x,1) )
print(y_2prime.subs(x,2))