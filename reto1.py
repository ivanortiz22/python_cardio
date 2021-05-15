




def run (): 
    
    a =float(input("escribe valor cateto2 : "))
    b =float(input("escribe valor cateto2 : "))
    c =float(input("escribe valor base: "))
    altura =float(input("escribe valor de la altura : "))
    respuesta= c*altura/2
    print("El area del Triangulo es: " +str(respuesta)+ " m2 ")
    if a == c and a == b:
        print("vaya! todos los lados son iguales, se trata de un Equilatero")
    elif a != c and a != b:
        print("vaya! todos los lados son distintos, se trata de un Escaleno")
    else:
        print("vaya! por lo menos dos lados son iguales, se trata de un Isoceles")
  
    





if __name__ == '__main__':
    run() 


