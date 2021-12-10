def remove_repetidos(list):
    list.sort()
    list0 = []
    for n in list:
        if n not in list0:
            list0.append(n)
            list0.sort()
    return list0



