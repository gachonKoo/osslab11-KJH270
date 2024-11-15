import geo.utils as utils
import sys


a,b,r = map(int,sys.stdin.readline().split())
c = utils.pythagoras(a,b)
print("c = ",c)

area = utils.circle(r)
print("area = ",area)

