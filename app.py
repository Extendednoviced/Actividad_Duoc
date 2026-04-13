#Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
#1
edad = int(input("Ingrese su edad para verificar si es mayor de edad o no: "))
if edad >= 50:
    print("Viejo")
else:
    print("Joven")
#Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
#User1: pedro   	Contraseña1: 1234
#User2: angel		Contraseña2: a4s1
#2
try:
    usuario = input("Ingrese su usuario: ").lower()
    contrasena = input("Ingrese contraseña: ").lower()
    if usuario == "pedro" and contrasena == "1234":
        print("Hola Pedro.")
    elif usuario == "angel" and contrasena == "a4s1":
        print("Hola Angel.")
    else:
        print("Usuario no encontrado")
except:
    print("Error")
#Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación),
#finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0
#3
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3
print(f"Promedio: {promedio}")
if promedio >= 4:
    print("Aprobado")
else:
    print("Desaprobado")