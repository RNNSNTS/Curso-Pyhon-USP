number = input ("Digite um número inteiro:")
n = int(number)

# Extraindo a unidade
unidade = n % 10

# Eliminando a unidade de nosso número
numero = (n - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Fazendo ser inteiros
dezena = int(dezena)

print("O dígito das dezenas é",dezena)
