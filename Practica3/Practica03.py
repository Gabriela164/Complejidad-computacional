
# SOLUCIÓN AL PROBLEMA DE LAS N REINAS DISTRUIBUIDAS 
# EN UN TABLERO DE AJEDREZ N X N SIN QUE SE AMENACEN ENTRE SI, 
# USANDO => ALGORITMOS GENÉTICOS.

# La solución se representa como un arreglo de N elementos. Cada elemento del
# arreglo representa el No. de fila en la que se encuentra la reina de la columna 
# correspondiente. Por ejemplo, si N = 8 en un tablero de 8x8, una solucion
# optima seria [4, 2, 7, 3, 6, 8, 1, 5] entonces la primer reina estara en la columna 1 fila 4, la
# segunda reina estara en la columna 2 fila 2, la tercera reina estara en la columna 3 fila 7, etc.

# Alumn@: Gabriela López Diego 
# Curso: Complejidad Computacional 2024-2
# Fecha: 9 de Junio del 2024
import random
import matplotlib.pyplot as plt

 
def individuoInicial(N_reinas):
    '''
    Metodo para generar el individuo inicial (parte de la población inicial)
    args: 
        N_reinas: numero de reinas
    return:
        individuo1: lista de tamaño N_reinas con valores aleatorios
    '''
    individuo1 = []
    for _ in range(N_reinas):
        individuo1.append(random.randint(1,N_reinas))
    return individuo1

def funcionAptitud(individuo):
    '''
    Metodo para calcular la aptitud de un individuo dado 
    args:
        individuo: lista de tamaño N_reinas con valores aleatorios
    return:
        aptitud: valor de la aptitud del individuo
    '''
    Num_reinas = len(individuo)
    aptitud = Num_reinas * (Num_reinas - 1) // 2  # Aptitud máxima si ninguna reina se ataca
 
    for i in range(Num_reinas - 1):
        for j in range(i + 1, Num_reinas):
            #Verifica si las reinas se atacan
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == abs(i - j):
                #Si se atacan, se disminuye la aptitud
                aptitud -= 1                
    return aptitud


def seleccionRuleta(poblacion, num_padres):
    '''
    Metodo que implementa seleccion por ruleta
    args:
        poblacion: lista de individuos
        num_padres: numero de padres a seleccionar
    return:
        seleccionIndividuos: lista de individuos seleccionados
    '''
    # Se calcula la aptitud total de la población
    aptitudTotal = sum(funcionAptitud(individuo) for individuo in poblacion)
    seleccionIndividuos = []
    
    # Se seleccionan los padres para la siguiente generación. Aquellos 
    # individuos con mayor aptitud tienen mayor probabilidad de ser seleccionados.
    for _ in range(num_padres):
        ruleta = random.uniform(0, aptitudTotal)
        suma_aptitud = 0
        for individuo in poblacion:
            suma_aptitud += funcionAptitud(individuo)
            if suma_aptitud >= ruleta:
                seleccionIndividuos.append(individuo)
                break
    return seleccionIndividuos


def corte(padres):
    '''
    Metodo que implementa el operador de corte de dos individuos (padres) 
    para generar dos hijos
    args:
        padres: lista de individuos
    return:
        hijos: lista de individuos generados
    '''
    hijos = []
    for i in range(0, len(padres), 2):
        padre1 = padres[i]
        padre2 = padres[i + 1]
        corte_punto = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:corte_punto] + padre2[corte_punto:]
        hijo2 = padre2[:corte_punto] + padre1[corte_punto:]
        hijos.extend([hijo1, hijo2])
    return hijos

def mutacion(hijos, probabilidad_mutacion): 
    '''
    Metodo que implementa la mutacion en los hijos generados. 
    Se verifica valor por valor del hijo si se muta o no. Se elige si
    se cambia o no a otra fila de manera aleatoria y con probabilidad 0.2
    args:
        hijos: lista de individuos
        probabilidad_mutacion: probabilidad de mutacion
    return:
        hijos_con_mutacion: lista de individuos con mutacion
    '''
    hijos_con_mutacion = []
    
    for hijo in hijos:
        nuevo_hijo = hijo[:] 
        for i in range(len(hijo)):
            if random.random() < probabilidad_mutacion:
                nuevo_valor = random.randint(1, len(hijo))
                nuevo_hijo[i] = nuevo_valor
        hijos_con_mutacion.append(nuevo_hijo)
    
    return hijos_con_mutacion

def proceso_Elitismo(poblacion, tamanio_mejoresIndividuos):
    '''
    Metodo que implementa el proceso de elitismo. 
    Se ordena la población por aptitud de manera descendente y se conservan
    a los mejores individuos  
    args:
        poblacion: lista de individuos
        tamanio_mejoresIndividuos: numero de mejores individuos a conservar
    '''
    # Ordenamos la población por aptitud de manera descendente
    poblacionOrdenada = sorted(poblacion, key=funcionAptitud, reverse=True)
    # Conservar a los mejores individuos (élite)
    mejores = poblacionOrdenada[:tamanio_mejoresIndividuos]
    return mejores


#Leer un archivo de texto que contiene el valor de las N reinas
try:
    nombre_archivo = input("***Implementacion del algoritmo Genetico para el problema de las N reinas***" +
                           "\nProporcione el nombre del archivo que contiene el numero de reinas: ")
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read().strip()
    archivo.close()
    try:
        if int(contenido) >= 4:
                N_de_reinas = int(contenido)
                int(N_de_reinas)
        else:
            print(f"\n=> El contenido del archivo debe ser un entero >= 4, modique el contenido del archivo: {nombre_archivo}")
            exit()
    except ValueError:
        print(f"\n=> El contenido del archivo debe ser un entero >= 4, modique el contenido del archivo: {nombre_archivo}")
        exit()

except FileNotFoundError:
    print(f"\nNo se encontró el archivo {nombre_archivo}. Intente de nuevo, incluya la extension .txt")
    exit()
    

tamanio_poblacion = 100 # Tamaño de la población, numero de individuos
probabilidad_de_mutacion = 0.2 
tamanio_mejoresIndividuos = 40 # Num de mejores individuos que se conservan en la población
max_Generaciones = 10000 
generaciones = 0

# Se genera la población inicial 
poblacion = [individuoInicial(N_de_reinas) for _ in range(tamanio_poblacion)]

# Se itera hasta que se encuentre una solución o se alcance el número máximo de generaciones
while generaciones < max_Generaciones:
    padres = seleccionRuleta(poblacion, tamanio_poblacion)
    hijos = corte(padres)
    hijos_mutados = mutacion(hijos, probabilidad_de_mutacion)
    
    # Seleccionamos los mejores individuos de la poblacion
    mejoresIndividuos = proceso_Elitismo(poblacion, tamanio_mejoresIndividuos)
    # y pasan a la siguiente generación sin alteraciones por recombinacion ni mutacion
    hijos_mutados.extend(mejoresIndividuos)
    poblacion = hijos_mutados
    generaciones += 1
    
    mejorIndividuo = max(poblacion, key=funcionAptitud)
    
    #Verifica si se encontro una solucion optima 
    if funcionAptitud(mejorIndividuo) == N_de_reinas * (N_de_reinas - 1) // 2:  
        costo = funcionAptitud(mejorIndividuo)      
        print(f"Solucion optima: {mejorIndividuo}")
        print(f"Costo de la solucion optima(Aptitud del mejor individuo): {costo}")
        #Ademas, mostramos el resultado en un tablero grafico
        x = []
        y = mejorIndividuo
        for i in range(1, len(y)+1):
            x.append(i)

        # Restamos 0.5 a las coordenadas para centrar los puntos en cada casilla del tablero
        x_c = [coord - 0.5 for coord in x]
        y_c = [coord - 0.5 for coord in y]

        plt.figure(figsize=(8, 8))  # Tamaño de la figura
        plt.scatter(x_c, y_c, color='red', label='Reinas', s=200, marker='D')  
        plt.xlim(0, len(x))  
        plt.ylim(0, len(y))  
        
        plt.title("Tablero de ajedrez con solución óptima para N = " + str(N_de_reinas))
        plt.xlabel("COLUMNAS")
        plt.ylabel("FILAS")
        plt.text(len(x) / 2, -0.88, "COSTO de la solucion optima(Aptitud del mejor individuo): "
                                    + str(costo), ha='center', fontsize=10)

        plt.grid(True)
        plt.show()
        exit()

print("No se encontró una solución después de", max_Generaciones, "generaciones. Intente de nuevo.")



