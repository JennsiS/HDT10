#Hoja 10
#Jennifer  Sandoval  18962
#Saul Contreras
#Michele Benevuto
#Algoritmos y estructura de datos 

from Database import *

db = Database("bolt://localhost:7687", "Default","password") 
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
        db.write("id","Doctor",{"nombre":nombredoc,"especialidad":especialidad,"contacto":contacto,"colegiado":colegiado})
    if(opcion=="2"):
        nombrep= input ("Ingrese el nombre del paciente ")
        telefono= input ("Ingrese el telefono del paciente ")
        db.write("id","Paciente",{"nombre":nombrep,"telefono":telefono})
    if(opcion=="3"):
        paciente= input ("Ingrese el nombre del paciente ")
        doctorv= input ("Ingrese el nombre del doctor visitado ")
        fecha= input ("Ingrese la fecha de la visita ")
        medicina= input ("Ingrese la medicina recetada ")
        db.link("Doctor","Paciente","nombre",doctorv,"nombre",paciente,"visited")
    if(opcion=="4"):
        espe= input ("Ingrese la especialidad que desea buscar ")
        retorno = db.getNode(Doctor,"especialidad",espe)
        for node in retorno:#Print nodes in the result
            print(node[0]["nombre"]) #The name of the atribute is setted in the second []
    if(opcion=="5"):
        persona1= input ("Ingrese el nombre de la primera persona ")
        persona2= input ("Ingrese el nombre de la segunda persona ")
        db.link("Paciente","Paciente","nombre",persona1,"nombre",persona2,"is_friend_with")
    if(opcion=="6"):
        recomendaciones = [] 
        paciente = input ("Ingrese el nombre de un paciente de referencia")
        retorno1 = db.getNodesByLink("Paciente","nombre",paciente,"is_friend_with")
        for node in retorno1:#Print nodes in the result
            recomendaciones.append(node[0]["nombre"]) #The name of the atribute is setted in the second []
        retorno2 = db.getNodesByOther("Paciente","nombre",paciente,"visited")
        for node in retorno2:#Print nodes in the result
            recomendaciones.append(node[0]["nombre"]) #The name of the atribute is setted in the second []
        for paciente in recomendaciones:#Print nodes in the result
            print(paciente)
    if(opcion=="7"):
        doctor = input ("Ingrese el nombre de un doctor de referencia")
        retorno = db.getNodesByOther("Doctor","nombre",doctor,"visited")
        for node in retorno:#Print nodes in the result
            print(node[0]["nombre"])
    opcion= input ("Ingrese  el numero de la opcion que desea realizar ")
