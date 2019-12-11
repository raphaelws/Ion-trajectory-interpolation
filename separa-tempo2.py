import numpy as np
import matplotlib.pyplot as plt


track=np.loadtxt("tracks.dat")

tamanho = len(track)-1
iontempo = []

gem = open("ion-gem.txt", "w")
direto = open("ion-direto.txt", "w")



while tamanho>=0:
  ion = track[tamanho,0]
  iontempo.append([track[tamanho,0],track[tamanho,5]])	
  novoion = True
  while novoion:
    tamanho-=1
    if (ion!=track[tamanho,0]):
      novoion = False

print(iontempo[1])
print(iontempo[-2])

iontempo=list(reversed(iontempo))


for linha in track:
  ion = linha[0]
  ionind = int(linha[0])
  if ion==iontempo[ionind][0]:
    if iontempo[ionind][1]<500:
      gem.write(str(linha[0])+' '+str(linha[1])+' '+str(linha[2])+' '+str(linha[3])+' '+str(linha[4])+' '+str(linha[5])+'\n')

    if iontempo[ionind][1]>50000:
      direto.write(str(linha[0])+' '+str(linha[1])+' '+str(linha[2])+' '+str(linha[3])+' '+str(linha[4])+' '+str(linha[5])+'\n')
