from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

opcion= int
def Menu():
   print("1. Graficar la función de densidad de una distribución uniforme.")
   print("2. Graficar la función de densidad de una distribución Bernoulli. ")
   print("3. Graficar la función de densidad de una distribución Poisson. ")
   print("4. Graficar la función de densidad de una distribución Exponencial. ")
   print("5. Salir")

def F_poisson ():
    x = np.arange(0, 100, 0.5) 
    y = poisson.pmf(x, mu=40, loc=10) 
    plt.plot(x, y) 
    plt.show() 
############### BERNUILLI 
def F_bernulli():
    from scipy.stats import binom 
    n = 6
    p = 0.6
    r_values = list(range(n + 1)) 
    dist = [binom.pmf(r, n, p) for r in r_values ] 
    plt.bar(r_values, dist) 
    plt.show() 
################ Exponencial
def F_exponencial():
    from scipy.stats import expon
    rv = expon.rvs(size=1000) # Genera números aleatorios
    cuenta, cajas, ignorar = plt.hist(rv, 20)
    plt.ylabel('Frecuencia')
    plt.xlabel('X')
    plt.title('Histograma Exponencial')
    plt.show()
######################### UNIFORME
def F_uniforme():
    import random
    plt.figure(figsize = (8, 4))
    plt.hist([random.uniform(10, 15) for i in range(10000)])
    plt.show()
    
while True:
    Menu()
    opcion=int(input("Ingrese la opcion deseada: "))
    
    if(opcion<1):
        print("ingrese una opcion correcta")
    if(opcion>5):
         print("ingrese una opcion correcta")
    if (opcion==1):
        F_uniforme()
    elif(opcion==2):
        F_bernulli()
    elif(opcion==3):
        F_poisson()
    elif(opcion==4):
        F_bernulli()
    elif(opcion==5):
        break
        
    
    
    
    
    
    