def maximo(x,y,z):
    if y >= z and y>=x:
        return y
    if x >= z and x >= y:
        return x
    if z >= y and z>=x:
        return z
