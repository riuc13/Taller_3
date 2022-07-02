import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from csv import reader

with open('Experimento_a.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
   
   
with open('Experimento_b.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows2 = list(csv_reader)
arr = np.array(list_of_rows)
arr2 = np.array(list_of_rows2)
suma=0;
contador=0;
Lista=[]
for i in list_of_rows:
    Lista.append(float(i[0]))
    suma= suma + float(i[0])
    contador= contador+1


print(Lista)
suma2=0;
contador2=0;
Lista2=[]
for i in list_of_rows2:
    Lista2.append(float(i[0]))
    suma2 = suma2 + float(i[0])
    contador2 = contador2+1

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
   
salir = False
opcion = 0

def opcion1():
    print("Promedio A " + str(suma/contador))
    print("Promedio B " + str(suma2/contador2))

def opcion2():
    r, p = stats.pearsonr(Lista, Lista2)
    print(f"Correlación Pearson: r={r}, p-value={p}")

    r, p = stats.spearmanr(Lista,Lista2)
    print(f"Correlación Spearman: r={r}, p-value={p}")
   
def opcion3():
    print('Has elegido la opción 3')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x = Lista, y = Lista2)
    z = np.polyfit(Lista, Lista2, 1)
    p = np.poly1d(z)
    plt.plot(Lista,p(Lista),"r--")
    plt.xlabel("Experimento A ")
    plt.ylabel("Experimento B ")

    plt.show()
   
   
while not salir:
        print ("1. Promedio de experimentos archibo 'A' y archivo 'B'")
        print ("2. Opcion 2")
        print ("3. Opcion 3")
        print ("4. Salir")
        print ("Elige una opcion")
 
        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
 
print ("Fin")