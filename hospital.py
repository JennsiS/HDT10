#Hoja 10
#Jennifer  Sandoval  18962
#Saul
#Michele Benevuto
#Algoritmos y estructura de datos 

from test import *

print ("Bienvenido")
print("A continuacion se le presentan las acciones que puede realizar")
print ("1. Ingresar Doctores")
print ("2. Ingresar pacientes")
print ("3. Ingresar visita de un paciente a un Doctor")
print ("4. Consultar Doctores por especialidad")
print ("5. Ingresar relacion entre pacientes")
print ("6. Recomendación a un paciente")
print ("7. Recomendación de Doctor")
print ("8. Salir")
opcion= input ("Ingrese  el numero de la opcion que desea realizar ")
while (opcion!="8"):
    if (opcion=="1"):
        nombredoc= input ("Ingrese el nombre del doctor ")
        especialidad= input ("Ingrese la especialidad del doctor ")
        contacto= input ("Ingrese el contacto del doctor ")
        colegiado= input ("Ingresar el numero de colegiado del doctor ")
        #ingresardoc=write(0,Doctor,nombre)
    if(opcion=="2"):
        nombrep= input ("Ingrese el nombre del paciente ")
        telefono= input ("Ingrese el telefono del paciente ")
        #ingresarpac=write(0,Paciente,nombre)
    if(opcion=="3"):
        paciente= input ("Ingrese el nombre del paciente ")
        doctorv= input ("Ingrese el nombre del doctor visitado ")
        fecha= input ("Ingrese la fecha de la visita ")
        medicina= input ("Ingrese la medicina recetada ")
        #link(Doctor,Paciente,doctorv,paciente,"visitó")
    if(opcion=="4"):
        espe= input ("Ingrese la especialidad que desea buscar ")
        #getNode(Doctor,espe)
    if(opcion=="5"):
        persona1= input ("Ingrese el nombre de la primera persona ")
        persona2= input ("Ingrese el nombre de la segunda persona ")
        #link(Paciente,Paciente,persona1,persona2,"conoce a")
    #if(opcion=="6"):
        #Mostrar recomendacion
    #if(opcion=="7"):
        #Mostrar recomendacion
    opcion= input ("Ingrese  el numero de la opcion que desea realizar ")
