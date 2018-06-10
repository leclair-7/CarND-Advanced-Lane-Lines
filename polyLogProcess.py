from scipy import stats
import numpy as np

s = np.genfromtxt('Brrrr.log',dtype='float')
#print(s)
s2 = np.array(s)

x2,x1,b = s2[:,0],s2[:,1],s2[:,2]

'''
print(x2)
print()
print(b)
'''
print(stats.describe(x2))
print()
print(stats.describe(x1))
print()
print(stats.describe(b))

print()
from math import sqrt
a = -.00256515 + sqrt(.00069877876)
b = 3.805212 + sqrt(1338.377)
c = -242.17783 + sqrt(160203168.52084109)
print("a:",a)
print("b:",b)
print("c:",c)