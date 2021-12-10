def primo(k):
    i = 1
    cont = 0
    while i <= k:
        if k % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True

def maior_primo (x):
    primo(x)
    while x>0:
        if primo (x) == True :
            return x
        if primo (x) == False :
            x += -1

         
         






