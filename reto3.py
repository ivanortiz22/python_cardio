
def conversion(eleccion,milla):
    if eleccion == 1:
        resultado= milla *  1.609344
        print("son "+str(resultado)+" km ")
    if eleccion== 2:
        resultado2= milla/ 1.609344
        print("son "+str(resultado2)+" millas ")







def run():
    print("""
    
    Bienvenidos a mi programita conversor millas a km  - 
    km a millas selecione la conversion conveniente:
    1:milas a km 
    2:km a millas
    
    
    """)
    eleccion=int(input(" escoja opcion : "))
    milla=int(input(" numero de milla o km "))
    conversion(eleccion,milla)









if __name__ == '__main__':
    run() 