n = int(input("Digite um número inteiro:"))

if n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0 or n == 1  or n == 3 or n == 5 or n == 7 :
    print("primo")
else:
    print ("não primo")
