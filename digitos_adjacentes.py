x= input("Digite um número inteiro:")
l = len(x)
n = int (x)
i =1
z=1
y=1
a=1
repetição = True

while i <= l and repetição == True:
    z = n % 10
    n= n // 10
    a = n % 10
    if l==1:
        print ("não")
    break
    if a == z:
        repetição = True
        print("sim")
        break
    i = i + 1
else:
    repetição = False
    print("não")






