

def operacion(limite_inferior,limite_superior,numero_a_comparar):
    # arreglo =[]
    # for i in range (limite_inferior,limite_superior+1,1):
    #     arreglo.append(i)
    # print(arreglo)
    
    while True:
        if numero_a_comparar >= limite_inferior and numero_a_comparar <= limite_superior:
            print("esta dentro del rango el numero :" + str(numero_a_comparar))
            break
        else:
            print("esta fuera del rango el numero :" + str(numero_a_comparar))
            return run()
            






def run():
    limite_inferior=int(input("ingrese el limite inferior :"))
    limite_superior=int(input("ingrese el limite superior:"))
    numero_a_comparar=int(input("ingrese el valor a comparar:"))
    operacion(limite_inferior,limite_superior,numero_a_comparar)









if __name__ == '__main__':
    run() 