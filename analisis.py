notas = [] #Esto es para inicializar una lista vacia
           #funciona como un recipiente que uno va llenado 
print("Ingresa las notas de los alumnos")

#El bucle for se repetira 5 veces (de 0 a 4)
for i in range(5):
    #Usamos i + 1 para que en pantalla aparezca nota1, nota2, nota3....nota5
    entrada = input(f"Ingrese la nota{i + 1}: ")
    nota = float(entrada)
    notas.append(nota)

#Calculamos las notas maximas y minimas
nota_maxima = max(notas)
nota_minima = min(notas)

#Contamos cuantas veces se repiten
cantidad_maxima = notas.count(nota_maxima)
cantidad_minima = notas.count(nota_minima)

#Contamos cuantas notas estan por debajo y por encima de 85
menores_a_85 = 0
mayores_a_85 = 0

#Es un bucle (for) que sirve para recorrer uno por uno los elementos que se
#guardo dentro de la lista notas
#in signigica "en"(dentro de) le indica a python que busque dentro de 
#donde tiene que sacar los elementos.
for nota in notas:
    if nota < 85:
        menores_a_85 += 1
    elif nota > 85: 
        mayores_a_85 += 1
    #Se usa elif para que si no se cumple la primera pregunta
    #pase a la siguiente y la evalue
print(f"\n----RESULTADOS----")
print(f"Las 5 notas ingresadas son: {notas}")
print(f"Notas maxima: {nota_maxima}")
print(f"Notas minima: {nota_minima}")
print(f"\n Cantidad de notas minimas: {menores_a_85}")
print(f"Cantidad de notas maximas: {mayores_a_85}")
