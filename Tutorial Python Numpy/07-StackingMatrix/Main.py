import numpy as np

a=np.array([1,2,3])
b=np.array([4, 5, 6])

aMat=np.zeros((2,3))
bMat=np.ones((2,3))

print("Menumpuk serara horizontal")
c=np.hstack((a,b))
print(c)
print()
print("Menumpuk serara Vertikal")
d=np.vstack((a,b))
print(d)
print()
cMat=np.hstack((aMat, bMat))
dMat=np.vstack((aMat, bMat))
print(cMat,'\n\n',dMat)