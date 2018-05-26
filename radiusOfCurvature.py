



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

print(radiusOfCurvature(1))
