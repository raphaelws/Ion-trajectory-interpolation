import numpy as np
import matplotlib.pyplot as plt


track=np.loadtxt("tracks.dat")




ion1 = track[0,0]
ion2 = track[0,0]

gem = open("ion-gem.txt", "w")
direto = open("ion-direto.txt", "w")

add =[]


for linha in track[:]:
  
  
  ion1 = linha[0]
  
  
 
  if (ion1!=ion2):
    t=tant
    
    if t<400:
      print(t)
      string = ''
      for escreve in add:
        string+=str(escreve[0])+' '+str(escreve[1])+' '+str(escreve[2])+' '+str(escreve[3])+' '+str(escreve[4])+' '+str(escreve[5])+' '"\n"
      gem.write(string)
      add=[]
      string=''
      
      
    if t>500000:
      string = ''
      for escreve in add:
        string+=str(escreve[0])+' '+str(escreve[1])+' '+str(escreve[2])+' '+str(escreve[3])+' '+str(escreve[4])+' '+str(escreve[5])+' '"\n"
      direto.write(string)
      add=[]
      string=''

  
  add.append(linha)
  tant=linha[5]
  ion2=ion1


gem.close()
direto.close()
