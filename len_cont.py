import timeit


def rec(cont, vals, value, tamanho = 0):
    try:
        return tamanho + rec(cont + 1, vals, vals[cont])            
    except:
        return cont
    

def time_len(vals:list):
    tamanho = rec(0, vals, 0)
    
    return tamanho
        
        
lista = [2,5,8,6,8,6,8,9, 8, 5, 5]

inicio = timeit.default_timer()
print(time_len(lista))
fim = timeit.default_timer()
print("sem len ", fim - inicio)

inicio = timeit.default_timer()
print(len(lista))
fim = timeit.default_timer()
print("com len ", fim - inicio)


