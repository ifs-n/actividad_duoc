import os
os.system("cls")

# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# try:
#     edad = int(input("Ingrese su edad: \n"))
#     if edad >= 18:
#         print("es mayor de edad")
#     else:
#         print("es menor de edad")
# except:
#     print("el valor ingresado no es un numero")
    
# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

# try:
#     usuario1 = "pedro"
#     passwd1 = "1234"
#     usuario2 = "angel"
#     passwd2 = "a4s1"
    
#     usuario = input("Ingrese su usuario: \n")
#     passwd = input("Ingrese su contraseña: \n")
    
#     if usuario == usuario1 and passwd == passwd1:
#         print(f"Hola {usuario}, has iniciado sesión correctamente")
#     elif usuario == usuario2 and passwd == passwd2:
#         print(f"Hola {usuario}, has iniciado sesión correctamente")
#     else:
#         print("usuario o contraseña inválidos")
# except:
#     print("datos ingresados invalidos")

# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

try:
    cantidad = 3
    acum_nota = 0
    for x in range(cantidad):
        nota = int(input(f"Ingrese nota {x+1}:\n"))
        acum_nota = acum_nota + nota
    promedio = acum_nota / cantidad
    if promedio >= 4:
        print(f"aprobado con nota {promedio}")
    else:
        print(f"reprobado con nota {promedio}")
except:
    print("el valor ingresado no es una nota")
# Crear una salida por pantalla con la siguiente información:

# ¿Cuál de los siguientes animales vive en el agua?
# Perro
# Cocodrilo
# Conejo
# Tiburón

# Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la respuesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por pantalla para mostrar el puntaje obtenido.

# De la misma forma del ejercicio anterior, debes crear un formulario con 3 preguntas (4 respuestas por cada pregunta) de un tema a elección, ya sea películas, series, caricaturas, entre otras.

# Asignar puntaje a cada pregunta y dependiendo del puntaje generar una escala de notas, así cuando los usuarios respondan las 3 preguntas se les muestra mediante una salida por pantalla su puntaje obtenido y la nota que equivale.


