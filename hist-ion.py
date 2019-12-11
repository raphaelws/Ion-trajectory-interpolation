import numpy as np
import matplotlib.pyplot as plt


track=np.loadtxt("tracks.dat")

tempo = []
gem =[]
direto = []


ion1 = track[0,0]
ion2 = track[0,0]

add =[]

for linha in track[:]:
  add.append(linha)
  
  ion1 = linha[0]
  
  
  if (ion1!=ion2):
    if t<5000:
      np.savetxt("ion-gem.txt",add,delimiter=' ', newline='n')
      add=[]
      
      
    if t>500000:
      np.savetxt("ion-direto.txt",add=[],delimiter=' ', newline='n')
      add=[]

  t=linha[5]
  ion2=ion1
    
  

