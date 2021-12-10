a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

import math

delta = b**2 - 4*a*c

if delta < 0:
  print ("Essa equação não tem raízes.")
else:
  if delta == 0:
      r1 = (-b + math.sqrt(delta))/(2*a)
      print ("A raíz é:",r1 )
  if delta > 0:
    r1 = (-b + math.sqrt(delta))/(2*a)
    r2 = (-b - math.sqrt(delta))/(2*a)
    print ("As raízes são:",r1,"e",r2 )


