###  METODO DE EULER PARA ECUACIONES DIFERENCIALES DE PRIMER ORDEN ###


# LIBRERIAS:
    
    
    
# ECUACION DIFERENCIAL:
    
def f(t, x): 
        return x + 1.2*t*x - 2.4*t**2

    
# FUNCION:
    
def euler(t, x, dt, tmax):
        
    #Definir valores iniciales:
    t_n = t
    x_n = x
        
    #Imprimir valores iniciales:
    print('t', '\t','x')
    print(t_n, '\t', x_n)
        
    #Iteraciones:
    while t_n < tmax:
        x_n1 = x_n + f(t_n, x_n)*dt
        t_n1 = t_n +dt
        
        print(t_n1, '\t',  x_n1)
        
        x_n = x_n1
        t_n = t_n1


# VALORES INICIALES:
t = float(input("Ingrese el tiempo inicial: "))
x = float(input("Ingrese la posicion inicial: "))
dt = float(input("Ingrese el tamaño de paso: "))    
tmax =  float(input("Ingrese el tiempo final: "))


# USAR LA FUNCION:

euler(t, x, dt, tmax)
