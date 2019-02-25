print("Proyecto 2, sección de preguntas")
print("Detector de números primos:")
print("Inserte un número, si es un número primo no recibirá mayor información, si no se trata de un número primo, nosotros se lo haremos saber")

numeroprimo = int(input())
a=2
b=9

if numeroprimo == 0:
	print("No es primo")
elif numeroprimo == 1:
	print("No es primo")
elif numeroprimo == 2:
	print()
elif numeroprimo > 2:
	while a <= (numeroprimo-1): 
		primo=numeroprimo%a
		if primo == 0: 
			print("No es primo")
			b=0  
			a=numeroprimo
		elif primo !=0:
			b=1 
			a=a+1
print("Hasta la próxima")

print("Generador de números primos") 
print("Inserte el número hasta el cual desea que generemos los números primos")   
r=int(input())
for i in range(r):
	a=2
	b=2  
	primos=0 
	if i==0:       
		b=0
	elif i==1:
		b=0
	elif i==2: 
		b=1 
	elif i>2: 
		while a <= (i-1):
			primos=i%a
			if primos == 0:
				b=0
				a=i
			elif primos != 0:
				b=1
				a=a+1  
	if b == 1: 
		print(i)


print("Generación de una tupla con los primos gemelos menores a un número dado")
print("Inserte un número hasta el cual desea generar los primos gemelos menores") 
u=int(input())
w=0 
T = []  
for y in range(u):
	a=2
	b=2
	if y==0:
		b=0
	elif y==1:
		b=0
	elif y==2:
		b=1
	elif y>2:
		while a <= (y-1):
			primoss=y%a
			if primoss == 0:
				b=0
				a=y
			elif primoss != 0:
				b=1 
				a=a+1
	if b == 1:
		T.append(y)
print(f"{T}")
for w in range(len(T)): 
	if T[w]-T[w-1] == 2:
		continue 
	elif T[w]-T[w-1] != 2:
		break 	
		           
print(f"{T}")  

