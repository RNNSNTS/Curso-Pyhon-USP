def primo(x):
    fator =2
    while x% fator != 0 and fator <= x/2:
        fator = fator +1
    if x % fator == 0:
        return 0
    else :
        return 1


def n_primos(x):
    i=1
    while x>=2:
        i += primo(x)
        x += -1
    return i
        
    
