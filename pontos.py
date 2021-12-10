#importa pacote
import math

#coordenadas
x1 = float(input('Digite o valor de x:'))
y1 = float(input('Digite o valor de y:'))
x2 = float(input('Digite o valor de x:'))
y2 = float(input('Digite o valor de y:'))

#formula da distancia dos pontos
d = math.sqrt (((x1 - x2)**2) + ((y1 - y2)**2))

#longe ou perto?
if d < 10:
    print ("perto")
else:
   print ("longe")
  
