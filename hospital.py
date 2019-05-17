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
print ("6. Ingresar relacion entre doctores")
print ("7. Recomendación a un paciente")
print ("8. Recomendación de Doctor")
print ("9. Salir")
opcion= input ("Ingrese  el numero de la opcion que desea realizar ")
while (opcion!="9"):
    if (opcion=="1"):
        nombredoc= input ("Ingrese el nombre del doctor ")
        especialidad= input ("Ingrese la especialidad del doctor ")
        contacto= input ("Ingrese el contacto del doctor ")
        colegiado= input ("Ingresar el numero de colegiado del doctor ")
        db.write("id","Doctor",{"nombre":nombredoc,"especialidad":especialidad,"contacto":contacto,"colegiado":colegiado})
        print ("El doctor se ha ingresado exitosamente")
        print ("--------------------------------------")
    if(opcion=="2"):
        nombrep= input ("Ingrese el nombre del paciente ")
        telefono= input ("Ingrese el telefono del paciente ")
        db.write("id","Paciente",{"nombre":nombrep,"telefono":telefono})
        print ("El paciente se ha ingresado exitosamente")
        print ("--------------------------------------")
    if(opcion=="3"):
        paciente= input ("Ingrese el nombre del paciente ")
        doctorv= input ("Ingrese el nombre del doctor visitado ")
        fecha= input ("Ingrese la fecha de la visita ")
        medicina= input ("Ingrese la medicina recetada ")
        db.link("Paciente","Doctor","nombre",paciente,"nombre",doctorv,"visited")
        print ("La visita se ha ingresado exitosamente")
        print ("--------------------------------------")
    if(opcion=="4"):
        espe= input ("Ingrese la especialidad que desea buscar ")
        retorno = db.getNode("Doctor","especialidad",espe)
        print ("Doctores encontrados: ")
        for node in retorno:#Print nodes in the result
            print(node[0]["nombre"]) #The name of the atribute is setted in the second []
            print ("--------------------------------------")
    if(opcion=="5"):
        persona1= input ("Ingrese el nombre de la primera persona ")
        persona2= input ("Ingrese el nombre de la segunda persona ")
        db.link("Paciente","Paciente","nombre",persona1,"nombre",persona2,"is_friend_with")
        db.link("Paciente","Paciente","nombre",persona2,"nombre",persona1,"is_friend_with")
        print ("La relacion se ha ingresado exitosamente")
        print ("--------------------------------------")
    if (opcion=="6"):
        doctor1=input ("Ingrese el nombre del primer doctor ")
        doctor2=input("Ingrese el nombre del segundo doctor ")
        db.link("Doctor","Doctor","nombre",doctor1,"nombre",doctor2,"is_friend_with")
        db.link("Doctor","Doctor","nombre",doctor2,"nombre",doctor1,"is_friend_with")
        print ("La relacion se ha ingresado exitosamente")
        print ("--------------------------------------")
    if(opcion=="7"):
        recomendaciones = [] 
        paciente = input ("Ingrese el nombre de un paciente de referencia ")
        especialidad= input ("Ingrese la especialidad que desea ")
        retorno = db.getNodesByLink("Paciente","nombre",paciente,"is_friend_with")
        print ("Doctores encontrados: ")
        for friend in retorno:
            retorno1 = db.getNodesByLink("Paciente","nombre",friend[0]["nombre"],"visited")    
            for node in retorno1:#Print nodes in the result
                if(node[0]["especialidad"]==especialidad):
                    recomendaciones.append(node[0]["nombre"]) #The name of the atribute is setted in the second []
        retorno2 = db.getNodesByOther("Paciente","nombre",paciente,"visited")
        for paciente in recomendaciones:#Print nodes in the result
            print(paciente)
        print ("--------------------------------------")
    if(opcion=="8"):
        recomendaciones = [] 
        doctor = input ("Ingrese el nombre de un doctor de referencia ")
        especialidad= input ("Ingrese la especialidad que desea ")
        retorno = db.getNodesByLink("Doctor","nombre",doctor,"is_friend_with")
        print ("Doctores encontrados: ")
        for node in retorno:
            if(node[0]["especialidad"]==especialidad):
                recomendaciones.append(node[0]["nombre"]) #The name of the atribute is setted in the second []
        for node in recomendaciones:#Print nodes in the result
            print(node)
            print ("--------------------------------------")
    print ("Bienvenido")
    print("A continuacion se le presentan las acciones que puede realizar")
    print ("1. Ingresar Doctores")
    print ("2. Ingresar pacientes")
    print ("3. Ingresar visita de un paciente a un Doctor")
    print ("4. Consultar Doctores por especialidad")
    print ("5. Ingresar relacion entre pacientes")
    print ("6. Ingresar relacion entre doctores")
    print ("7. Recomendación a un paciente")
    print ("8. Recomendación de Doctor")
    print ("9. Salir")
    opcion= input ("Ingrese  el numero de la opcion que desea realizar ")
