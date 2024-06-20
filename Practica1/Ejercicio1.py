import random

def crear_trayectoria(grafica, u, v):
    #Verificamos que u y v pertenezcan al conjunto de vertices de la grafica
    if u not in grafica:
        print(f"El vertice de inicio {u} no existe en la grafica. Intente con un vertice valido.")
        exit()
    elif v not in grafica:
        print(f"El vertice final {v} no existe en la grafica. Intente con un vertice valido.")
        exit()
    
    #FASE 1 CONJETURA : Creamos una trayectoria del vertice u al vertice v, de forma no determinista.
    trayectoria = [u]  # La trayectoria comienza en el vértice de inicio
    vertice_actual = u
    
    while vertice_actual != v:      
        #Obtenemos las claves del diccionario del elemento [vertice actual] que son los vecinos
        #del vertice actual y lo convertimos a tipo lista 
        vecinos = list(grafica[vertice_actual].keys()) 
        #Elegimos un vertice aleatorio de los vecinos
        vertice_aleatorio = random.choice(vecinos)
        trayectoria.append(vertice_aleatorio)
        vertice_actual = vertice_aleatorio # Nos movemos al siguiente vértice

    return trayectoria


def verificar(grafica, k, trayectoria):
    # Fase 2 VERIFICACION :Verificamos si la trayectoria dada cumple con tener peso menor a k 
    peso_trayectoria = 0
    num_aristas = len(trayectoria)
    
    for i in range(num_aristas - 1):
        #Obtenemos el peso de la arista que conecta el vertice i con el vertice i+1
        peso_arista = grafica[trayectoria[i]][trayectoria[i+1]]
        peso_trayectoria += peso_arista
    
    if peso_trayectoria < k:
        print("La trayectoria dada >>SI<< tiene peso menor a k. El peso de la trayectoria es", peso_trayectoria)
    else:
        print("La trayectoria dada >>NO<< tiene peso menor a k. El peso de la trayectoria es", peso_trayectoria)


#Leemos un archivo .txt donde contendra los vertices en la primera linea
#y las aristas en las siguientes lineas (cada arista en cada linea)
try:
    archivo = open("Grafo1.txt", "r")
    vertices = archivo.readline().strip().split(',') #Leemos la primera linea y la separamos por comas
    vertices = [str(i) for i in vertices] #Convertimos los vertices a string
    aristas = []
    
    for linea in archivo: #Continuamos con el resto del archivo, leemos las aristas y las separamos por comas
        arista = tuple(linea.strip().split(','))
        aristas.append(arista) 
    
    archivo.close()
except FileNotFoundError:
    print("No se encontró el archivo Grafo1.txt")
    exit()
    

# Creamos un diccionario para representar la grafica 
grafica = {}

for vertice in vertices:
    grafica[vertice] = {}

# Asignamos aleatoriamente un peso entre 1 y 5 a cada arista de G
for arista in aristas:
    vertice1, vertice2 = arista
    peso = random.randint(1, 5)
    grafica[vertice1][vertice2] = peso
    grafica[vertice2][vertice1] = peso  # Por tratarse de una grafica no dirigida, la arista (v1, v2) es la misma que (v2, v1)

aleatorio1 = random.randint(0, len(vertices)-1)
inicio_u = vertices[aleatorio1]  #Vértice de inicio aleatorio
aleatorio2 = random.randint(0, len(vertices)-1)

#Nos aseguramos que el vertice final sea diferente al vertice de inicio
while aleatorio2 == aleatorio1:
    aleatorio2 = random.randint(0, len(vertices)-1)
    
final_v = vertices[aleatorio2]  #Vértice final aleatorio
peso_k = 20   #Peso. Queremos ver si existe una uv-trayectoria que cumpla con un peso menor a k

print("\nLa grafica G es " , grafica
        , "\nEl vertice de inicio es ", inicio_u
        , "\nEl vertice final es ", final_v
        , "\nEl peso k es: ", peso_k)

trayectoria_adivinadora = crear_trayectoria(grafica, inicio_u, final_v)
print("La uv-trayectoria es: ", trayectoria_adivinadora)
verificar(grafica, peso_k, trayectoria_adivinadora)

