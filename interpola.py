import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#inter=open("interpola-ion.txt", "a")
#track=open("tracks.dat", "w")

#track=np.loadtxt("tracks.dat")
#maior=0
#for t in track[:,5]:
#   if t>maior:
#     maior=t


maior=5000
track=np.loadtxt("tracks.dat")
divi=100
#dt=np.linspace(0,maior,divi)
dt=np.arange(0,maior,100)
tprint=np.arange(0,maior,0.1)

  
fig = plt.figure()
ax = fig.gca(projection='3d')

indice=0



for ion in [0,1,2]:
  x=[]
  y=[]
  z=[]
  t=[]

  i0=ion
  while i0==ion:

    if (i0==ion):
      x.append(track[indice][2])
      y.append(track[indice][3])
      z.append(track[indice][4])
      t.append(track[indice][5])
    i0=track[indice][0]

    indice+=1
  
 
  fx=interpolate.interp1d(t,x,fill_value= 'extrapolate')
  fy=interpolate.interp1d(t,y,fill_value= 'extrapolate')
  fz=interpolate.interp1d(t,z,fill_value= 'extrapolate')
  

  x=fx(dt)
  y=fy(dt)
  z=fz(dt)


  ax.plot(x, y, z,'.', label='parametric curve')
plt.show()


