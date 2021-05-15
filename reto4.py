import math

def volumen_esfera (d):
	volumen = (math.pi * ((d/2)**3))* (4/3)
	print ("El volumen de la esfera es: -->",volumen, "<--[m^3]")
	run()


def volumen_cono (b,h):
	volumen = (math.pi * ((b/2)**2) * h)/3
	print ("El volumen del cono es: -->",volumen, "<--[m^3]")
	run()


def volumen_piramide (b,h):
	volumen = (1/3) * b * h
	print ("El volumen de la pirámide es: -->",volumen, "<--[m^3]")
	run()


def volumen_parale (a,b,c):
	volumen = a * b * c
	print ("El volumen del Paralepípedo es: -->",volumen, "<--[m^3]")
	run()


def volumen_cubo(l):
	volumen = l** 3
	print ("El volumen del cubo es: -->",volumen, "<--[m^3]")
	run()


def volumen_cilindro(b,h):
	volumen = math.pi * ((b/2)**2) * h
	print ("El volumen del cilindro es: -->",volumen, "<--[m^3]")
	run()


def run():
	dato = int(input("""
Bienvenido al programa que te calcula el volumen de una figura

Para el volumen de un:
- Cilindro (1)
- Cubo (2)
- Paralepípedo o Ortoedro (3)
- Pirámide (4)
- Cono (5)
- Esfera (6)
- Ninguna (0)
--->> """))

	if dato == 1 :
		base = float(input("Ingresa la base del cilindro (diametro): "))
		altura = float(input("Ingresa la altura del cilindro: "))
		volumen_cilindro(base,altura)
	elif dato == 2:
		lado = float(input("Ingresa un lado del cubo: "))
		volumen_cubo(lado)
	elif dato == 3:
		base = float(input("Ingresa un base del Paralepípedo: "))
		altura = float(input("Ingresa un altura del Paralepípedo: "))
		pronfundidad = float(input("Ingresa un pronfundidad del Paralepípedo: "))
		volumen_parale(base,altura,pronfundidad)
	elif dato == 4:
		base = float(input("Ingresa la base de la Pirámide: "))
		altura = float(input("Ingresa la altura de la Pirámide: "))
		volumen_piramide(base,altura)
	elif dato == 5:
		base = float(input("Ingresa la base del cono (diametro): "))
		altura = float(input("Ingresa la altura del cono: "))
		volumen_cono(base,altura)
	elif dato == 6:
		diametro = float(input("Ingresa el diametro de la esfera: "))
		volumen_esfera(diametro)
	elif dato == 0:
		print("Gracias por pasar por acá")
	else:
		prin("Escogio una opcción no valida")

if __name__ == "__main__":
	run()