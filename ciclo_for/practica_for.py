lista = ["Banana", "Agua", "Queso" , 123, 5!=6]

# i recorre la lista y toma los valores de cada elemento
for i in lista:
    print(i)

# x recorre del 0 a n-1
for x in range(11):
    print(x)

# y toma el primer valor declarado e incrementa hasta el segundo -1
for y in range(1, 11):
    print(y)

# lo mismo que el anterior pero a la inversa
for j in range(11, -1, -1):
    print(j)

# avanza del 2 al 20 de 2 en 2
for z in range(2, 21, 2):
    print(z)

txt="analizar.txt"
with open(txt, "r") as archivo_txt:
    for numero_linea, linea in enumerate (archivo_txt, start=1):
        print(f"Análisis de linea {numero_linea}:")
        print(linea)