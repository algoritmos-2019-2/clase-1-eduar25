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
