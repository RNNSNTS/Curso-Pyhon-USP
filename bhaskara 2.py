import math

a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

delta = b**2 - 4*a*c

if delta < 0:
  print ("esta equação não possui raízes reais")
if delta == 0:
    r1 = (-b + math.sqrt(delta))/(2*a)
    print ("a raiz dupla desta equação é",r1 )
if delta > 0 :
  r1 = (-b + math.sqrt(delta))/(2*a)
  r2 = (-b - math.sqrt(delta))/(2*a)
  if r1> r2 :
    print ("as raízes da equação são",r2,"e",r1 )
  if r2>r1 :
    print ("as raízes da equação são",r1,"e",r2 )

