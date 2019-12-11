import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib



x=np.loadtxt("xt-gem.txt")
y=np.loadtxt("yt-gem.txt")
z=np.loadtxt("zt-gem.txt")

tamanho = len(x[0])-1
print(tamanho)


for i in range (tamanho):
  xt=x[:,i]
  yt=y[:,i]
  zt=z[:,i]

#3d
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.set_xlim3d([-0.025, 0.025])
  ax.set_ylim3d([-0.02, 0.02])
  ax.set_zlim3d([0, 0.025])

  ax.plot(xt, yt, zt,'.', label='parametric curve')
  fig.savefig("/home/wiky/projetos/interpola-ion/gif-ion/gem-plots3d/"+str(i)+'direto-plot''.png')
#/////////////////////////////////

#2d

  #fig = plt.figure()
  #plt.plot(yt, zt,'.')
  #plt.axis([-0.025, 0.025,0, 0.04])

  #plt.xlabel("y")
  #plt.ylabel("z")

  #fig.savefig("/home/wiky/projetos/interpola-ion/gif-ion/gem-plots/"+str(i)+'gem-plot''.png')

  


#plt.show()


