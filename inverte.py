n=1
list = []
while n != 0:
    n = int(input("Digite um número:"))
    if n!=0:
        list.append(n)
list.reverse ()
for x in list:
    print(x)
