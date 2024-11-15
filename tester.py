import geo.utils as utils
import sys

a,b = 3,4
a = int(sys.argv[1])
b = int(sys.argv[2])
c = utils.pythagoras(a,b)
print("c = ",c)

r = 10
r = int(sys.argv[3])
area = utils.circle(r)
print("area = ",area)

