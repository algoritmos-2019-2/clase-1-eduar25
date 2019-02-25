print("Los dos valores del tipo booleano son Verdadero y Falso, se escribe como True y False respectivamente")
print("Los tres operadores booleanos son AND, OR, NOT")

print("Operador NOT")
verdad = [True,False]
for n in verdad:
	print(n,not(n))

print("Operador AND")

sverdad = [True,False]
nverdad = [True,False]

for i in sverdad:
	for s in nverdad:
		print(i,s,i and s)
print("Operador OR")

for i in sverdad:
	for s in nverdad:
		print(i,s,i or s)
print("Los seis operadores de comparación son: <,>,==,<=, >=, !=")

print("La diferencia entre el operador igual y el de asignación es que uno sirve para darle el valor a una variable, mientras que el operador igual nos ayuda a visualizar la relación que existe entre dos variable")

print("Una condición es un estado que debe cumplirse para que una serie de comandos se realice, o para que no se realice, según sea el caso. Todo depende de cómo configuremos el condicional. Lo podemos usar en un ciclo for o un ciclo while")                              
print("Pulsamos Control+C")

print("El comando romper indica que se frena toda el condicional, es decir, si estamos realizando una iteración de 1 al 5, y rompemos en 2, entonces el condicional ya no realiza la iteración para 3,4, o 5; si por otro lado, realizamos el comando continuar, entonces al realizar continuar en una iteración que va de 1 a 5, en los valores 3 y 4, saltara la iteración en esos valores, y unicamente lo va a realizar para 1,2, y 5.")

print("La diferencia está en que rango (10) te genera una toda la serie de números entre 0 a 10, mientras que en rango (1,10) especificas que quieres unicamente los valores en el intervalo entre estos dos valores, y por último, rango (1,10,1) te da los valores en el intervalo entre esos dos números, pero además te los da de 1 en 1, si fuera rango (1,10,2) iría como (1,3,5,7,9), es decir, de dos en dos.")

print("Primeros N números y su suma")

print("Inserte un número")
suma=0
m=int(input())
while(i<=m):      
	suma=suma+i 
	print(i)
	i=i+1
print(f"La suma es {suma}")   
w=0
suma2=0  
suma3=0
print("Primeros N números y su suma")   
for w in range(1,m+1):   
	suma2=suma2+w      
	print(w)   

print(f"La suma es {suma2}")   

print("m números impares")
h=0 
print("Inserte un número")
y=int(input())
print("Los n números impares hasta el valor insertado son:")
while(h<=y):
	r=h%2
	if r==1:
		print(h)
	h=h+1


print("Serie de fibonacci")
print("inserte el número de términos deseados")
o=int(input())
print("Los términos de la serie de Fibonacci son:")
count=0
n1=0
n2=1     
while (count<=o):
	print(n1)
	nh=n1+n2
	n1=n2
	n2=nh
	count=count+1

print("Factorial de un número")
c=int(input())
factorial=1  
if c==0:
	print("0")
elif c==1:
	print("1")
else:   
	for i in range(1,c+1):
		factorial = factorial*i
	print(f"El factorial es {factorial}")



 
