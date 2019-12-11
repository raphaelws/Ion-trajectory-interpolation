import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#inter=open("interpola-ion.txt", "a")
#track=open("tracks.dat", "w")
xt = []
yt = []
zt = []


track=np.loadtxt("ion-gem.txt")
maior=0
for t in track[:,5]:
   if t>maior:
     maior=t
print(maior)



tamanho = len(track)-1

divi=20
dt=np.linspace(0.001,maior,divi)
tprint=np.arange(0,maior,0.1)

  
fig = plt.figure()
ax = fig.gca(projection='3d')

indice=0
ionlista=[]

while tamanho>=0:
  ion1 = track[tamanho,0]
  ionlista.append(track[tamanho,0])	
  novoion = True
  while novoion:
    tamanho-=1
    if (ion1!=track[tamanho,0]):
      novoion = False

ionlista=list(reversed(ionlista))
ionlista = np.array(ionlista)


for ion in ionlista[0:5]:
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
  print(z)  

  xt.append(x)
  yt.append(y)
  zt.append(z)
  
  
np.savetxt('xt-gem.txt',xt)
np.savetxt('yt-gem.txt',yt)
np.savetxt('zt-gem.txt',zt)
  
  




