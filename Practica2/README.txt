[Práctica 2 del Curso Complejidad Computacional 2024-2]
Profesora: María de Luz Gasca Soto
Ayudantes: Brenda Becerra, Malinali Gónzalez Lara
Alumna: López Diego Gabriela
Número de cuenta: 318243485

******Para ejecutar el script en SO Linux (se recomienda ejecutar desde terminal):******
->  Abrir terminal dentro de la carpeta donde se encuentre el .py y .txt

-> Ejecutar el comando python3 ProblemaNP.py

-> Cuando aparezca la instrucción "Ingrese el nombre del archivo que contiene 
el conjunto S (incluya la extension .txt):" 
    	- Escribir el nombre del archivo [ConjuntoS.txt] 
Dicho archivo contendra los elementos de un conjunto. Cada elemento del conjunto 
debe ser separado por una coma. 

-> Se solicitará algún numero entero t. Dicho número será el objetivo de la suma. 
(Se recomienda intentar con 307)

-> Se solicitará algún parámetro de aproximación epsilon.
(Se secomienda con 0.10)

SALIDA:
****************************************
El conjunto S dado es:  [104, 102, 201, 101]
El objetivo t dado es:  307
SI se ha encontrado un subconjunto de S cuya suma es igual al objetivo t
El valor exacto de la suma es: 307
Los elementos del subconjunto S que contribuyen a la suma EXACTA son: [104, 102, 101]
****************************************

NOTA IMPORTANTE:
La implementación del algoritmo de aproximación para el problema NP 
completo "la suma de subconjuntos" se obtuvo de los algoritmos proporcionados por el libro
“Introduction to Algorithms” de Thomas H. Cormen (Trim, Merge-list y APPROX-SUBSET-SUM) 
de las páginas 1128-1133 el cual anuncia con el Teorema 35.8 (ya demostrado) del mismo 
libro, que es un esquema de aproximación con complejidad de tiempo polinomial. 
Sin embargo, para la obtención del subconjunto del conjunto S que corresponde con 
contener los elementos que al sumarlos todos dan exactamente el valor t, utilizamos
programación dinámica. 
El método "encontrar_subconjunto_suma_exacta" también emplea tiempo de ejecución de tiempo 
polinomial. Primero se crea una matriz de n*objetivo, esto toma O(n*objetivo). Luego, tenemos un 
primer bucle for que toma tiempo O(n) para inicializar todas las filas en su primer columna con True.
Procedemos y observamos dos for anidados que en general toman tiempo O(n*objetivo). 
Finalmente, con el while como se inicializa a i y j igual a n y objetivo. En general, el objetivo es mayor
que n, entonces la complejidad de tiempo en esta ultima parte será simplemente de O(objetivo)
Por lo tanto, la complejidad de tiempo para todo el método esta determinada por
O(n*obj) + O(n) + O(n*obj) +O(objetivo) = O(2n*obj) = O(n*obj) que es fácil ver que cumple con ser
tiempo polinomial. 
