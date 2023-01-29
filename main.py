import numpy as np 
from itertools import combinations
import math 

class Point:
    def __init__(self,name:str, x_value:float, y_value:float,z_value:float):
        self._name = name
        self._x_value = x_value
        self._y_value = y_value
        self._z_value = z_value

    @property
    def name(self):
        return self._name
    @property
    def x(self):
        return self._x_value
    @property
    def y(self):
        return self._y_value
    @property
    def z(self):
        return self._z_value
   
    def __str__(self) -> str:
        return self.name +' => ('+ str(self.x)+', '+str(self.y) +', '+ str(self.z)+')'




a = Point(name='a',x_value=1,y_value=0,z_value=0)
b = Point(name='b',x_value=-1,y_value=0,z_value=0)
c = Point(name='c',x_value=0,y_value=1,z_value=0)
d = Point(name='d',x_value=0,y_value=-1,z_value=0)

e = Point(name='e',x_value=0,y_value=0,z_value=1)
f = Point(name='f',x_value=0,y_value=0,z_value=-1)

g = Point(name='g',x_value=1/3,y_value=1/3,z_value=1/3)
h = Point(name='h',x_value=-1/3,y_value=1/3,z_value=1/3)
i = Point(name='i',x_value=1/3,y_value=-1/3,z_value=1/3)
j = Point(name='j',x_value=1/3,y_value=1/3,z_value=-1/3)

k = Point(name='k',x_value=-1/3,y_value=-1/3,z_value=1/3)
l = Point(name='l',x_value=1/3,y_value=-1/3,z_value=-1/3)
m = Point(name='m',x_value=-1/3,y_value=1/3,z_value=-1/3)
n = Point(name='n',x_value=-1/3,y_value=-1/3,z_value=-1/3)

points = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]


def get_combinations(lst):
    return list(combinations(lst, 4))

combinations = get_combinations(points)
print('combinations',len(combinations)) 




def same_plane(p0:Point, p1:Point, p2:Point, p3:Point):
    if p0 ==p1 or p1 == p2 or p2 == p3:
        raise Exception('Same points passed!')

    #Vector
    v1 =[p1.x-p0.x, p1.y-p0.y, p1.z-p0.z]
    v2 = [p2.x-p0.x, p2.y-p0.y, p2.z-p0.z]
    v3 = [p3.x-p0.x, p3.y-p0.y, p3.z-p0.z]
    mtx =[v1,v2,v3]
    det = np.linalg.det(mtx)
    if round(det, 1)==0:
        return True
    return False

tets =[]
for comb in combinations:
    p0 = comb[0]
    p1 = comb[1]
    p2 = comb[2]
    p3 = comb[3]
    if not same_plane(p0=p0,p1=p1,p2=p2,p3=p3): 
        tets.append(comb)
        
print(len(tets))
