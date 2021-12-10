n = (input("Digite um número inteiro:"))
l = len (n)
t = int (n)

i=1
s=1
p=1
S=0


while i <= l:
    s = t % 10
    p = t//10
    S += s
    t= p
    i = i + 1

print(S)
