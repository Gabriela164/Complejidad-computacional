import random 

def conjetura(variables):
    asignaciones = {}
    #Asignamos valores de verdad a cada una de las literales de forma no determinista (aleatoria)
    for variable in variables:
        asignaciones[variable] = random.choice([True, False])
    return asignaciones

def verificacion(asignaciones, formula):
    #Funcion que se encarga de evaluar toda la formula, verifica si es V o F
    sustitucion_clausulas = []
    
    for clausula in formula:
        for literal, asignacion in asignaciones.items():
            # Sustituimos cada literal por su respectivo valor de verdad
            clausula = clausula.replace(literal, str(asignacion))
            clausula = clausula.replace('-', 'not ')
        clausula = clausula.replace('+', 'or')
        sustitucion_clausulas.append(clausula)
        
    #Almacenamos los valores de verdad de cada clausula
    valores_clausulas = []
    for clausula in sustitucion_clausulas:
        valores_clausulas.append(eval(clausula))
    
    #Ahora evaluamos si TODA la formula es V o F
    return all(valores_clausulas)


#Leemos un archivo .txt que contiene la formula FNC
#Recibimos un texto que contiene la formula en la primera linea
#(x + -y + z) * (x + y + z) * (-x + -y + -z) * (-x + y + -z)
try:
    archivo = open("3sat.txt", "r")
    clausulas = archivo.readline().strip()
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe")
    exit()
    

lista_clausulas = clausulas.split("*")

#Extraemos las literales de la formula
conjunto_literales = set()

for clausula in lista_clausulas:
    clausula = clausula.strip().replace("(", "").replace(")", "")
    literales = clausula.split("+")
    for literal in literales:
        literal = literal.strip().replace("-", "")
        conjunto_literales.add(literal)

conjunto_literales = sorted(conjunto_literales)
lista_literales = list(conjunto_literales)

asignaciones = conjetura(lista_literales)
valor_de_verdad_formula = verificacion(asignaciones, lista_clausulas)

print(f"\nFormula en FNC:{clausulas}")
print(f"Las literales de la formula: {lista_literales}")
print(f"Asignaciones de valores de verdad para las literales: {asignaciones}")
print(f"Con lo anterior, la formula en FNC es: {valor_de_verdad_formula}")

