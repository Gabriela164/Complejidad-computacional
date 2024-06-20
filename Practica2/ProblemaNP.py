'''
Script que brinda una solución implementando el algoritmo de aproximación
para el problema NP-completo de la suma de subconjuntos (The Subset Sum Problem).
Consiste en determinar si existe un subconjunto de números enteros S cuya suma sea
igual a un valor t dado. Descrito en el libro “Introduction to Algorithms” (pag 1128-1133)
de Thomas H. Cormen.

Alumna: López Diego Gabriela
Num de cuenta: 318243485
Curso: Complejidad Computacional 2024-2
'''
def trim(L, alpha):
    '''
    Filtra los elementos de una lista que son mayores a un valor de corte alpha
    Args:
            L: lista de numeros
            alpha: valor de corte
    Returns:
            Lp: lista de numeros sin elementos mayores a alpha
    '''
    m = len(L)
    y1 = L[0]   #Primer elemento de la lista L
    L1 = [y1]     
    last = y1   
      
    for i in range(1, m): #Iteramos desde 1 hasta m-1
        if L[i] > last*(1 + alpha): 
            L1.append(L[i])
            last = L[i]
    return L1


def merge_lists(L1, L2):
    '''
    Fusiona y ordena dos listas ordenadas y elimina duplicados
    Args:
            L1 y L2: listas de numeros enteros
    Returns:
            L: lista de numeros fusionada y ordenada sin duplicados
    '''
    L = L1 + L2 
    L = list(set(L))  #Lo convertimos a conjunto para eliminar duplicados
    L.sort()          #Toma tiempo O(nlogn)
    return L 


def approx_subset_sum(S, t, epsilon):
    '''
    Esquema de aproximación para el problema de la suma de subconjuntos
    Args:
            S: lista de numeros enteros
            t: valor objetivo
            epsilon: parametro de aproximación
    Returns:
            z_star: valor aproximado de la suma de subconjuntos
            elementos: lista de elementos que participan en la suma aproximada
    '''
    n = len(S)
    L1 = [0]
    elementos = []  # Lista para almacenar los elementos que participan en la suma aproximada
    for i in range(n):
        L2 = [x + S[i] for x in L1] #A cada elemento de L1 le sumamos el valor de S[i]
        Li = merge_lists(L1,L2)
        Li = trim(Li, epsilon/(2*n))
        L1 = [x for x in Li if x <= t]
    z_star = max(L1)
    return z_star


def encontrar_subconjunto_suma_exacta(conjunto, objetivo):
    n = len(conjunto)
    '''
    Nos da un subconjunto de un conjunto dado cuya suma es igual a un objetivo dado(Tenemos la certeza que lo encontraremos)
    Args:
            conjunto: lista de numeros enteros
            objetivo: valor objetivo
    Returns:
            subconjunto: lista de elementos que contribuyen a la suma exacta
    '''
    dp = [[False] * (objetivo + 1) for _ in range(n + 1)] #Creamos una matriz de valores booleanos
    
    for i in range(n + 1):
        dp[i][0] = True
    
    # Iteramos sobre los elementos del conjunto y llenamos la matriz dp
    for i in range(1, n + 1):
        for j in range(1, objetivo + 1):
            # Si el elemento actual es mayor que la suma que intentamos alcanzar, lo descartamos
            if conjunto[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - conjunto[i - 1]]
    
    # Reconstruimos el subconjunto 
    subconjunto = []
    i, j = n, objetivo
    while i > 0 and j > 0:
        # Si el elemento actual no contribuye a la suma, pasamos al siguiente elemento
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            # Si el elemento actual contribuye a la suma, lo agregamos al subconjunto y restamos su valor de la suma
            subconjunto.append(conjunto[i - 1])
            j -= conjunto[i - 1]
            i -= 1
    
    return subconjunto[::-1] if sum(subconjunto) == objetivo else None


def prueba():
    S = [104,102,201,101]
    t = 307
    epsilon = 0.10
    z = approx_subset_sum(S, t, epsilon)
    print(z) #Salida esperada: 307, [104 , 102 , 101]
    if t == z:
        print("Se ha encontrado un subconjunto de S cuya suma es igual al objetivo t")
        print("El subconjunto de S que contribuye a la suma EXACTA es:", encontrar_subconjunto_suma_exacta(S, t))
    else:
        print("No se ha encontrado un subconjunto de S cuya suma sea igual al objetivo t")
    
    
def archivo_entrada():
    print("Ingrese el nombre del archivo que contiene \nel conjunto S (incluya la extension .txt):")
    archivo = input()
    try:
        with open(archivo,"r") as archivotxt:
            elementos_S = archivotxt.read().split(",")
            lista_Conjunto_S = [int(x) for x in elementos_S]
            return lista_Conjunto_S
    except FileNotFoundError:
        print("No se encontro el archivo de entrada. Intentalo de nuevo :D")
        exit()

    
#Funcion principal 
if __name__ == "__main__":
    #prueba()
    conjuntoS = list(archivo_entrada())
    
    #Le solicitamos al usuario que ingrese el objetivo t (un entero mayor a 0)
    while True:
        try:
            t = int(input("Ingrese el objetivo t (un entero mayor a 0): "))
            if t > 0:
                break
            else:
                print("El valor de t debe ser mayor a 0")
        except ValueError:
            print("Por favor, ingresa un entero mayor a 0")
    
    #Le solicitamos al usuario que ingrese el valor de epsilon (un numero decimal entre 0 y 1)
    while True:
        try:
            epsilon = float(input("Ingrese el valor de epsilon (un numero decimal entre 0 y 1): "))
            if 0 < epsilon < 1:
                break
            else:
                print("El valor de epsilon debe ser un numero decimal entre 0 y 1")
        except ValueError:
            print("Por favor, ingresa un numero decimal entre 0 y 1")
            
    z = approx_subset_sum(conjuntoS, t, epsilon)
    
    
    print("\n****************************************") 
    print("El conjunto S dado es: ", conjuntoS)
    print("El objetivo t dado es: ", t)
    if z == t:
        print("SI se ha encontrado un subconjunto de S cuya suma es igual al objetivo t")
        print("El valor exacto de la suma es:", z)
        print("Los elementos del subconjunto S que contribuyen a la suma EXACTA son:", encontrar_subconjunto_suma_exacta(conjuntoS, t))
    else:
        print("NO se ha encontrado un subconjunto de S cuya suma sea igual al objetivo t")
        print("Pero hemos logrado un valor APROXIMADO a t:", z) 
    print("****************************************") 
    