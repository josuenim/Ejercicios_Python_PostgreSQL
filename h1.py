import psycopg2
import msvcrt

#-------------CONEXION CON POSTGRESQL -----------
try:
    conexion= psycopg2.connect(
        host ="localhost",
        port ="5432 ",
        user = "postgres",
        password ="1812",
        dbname = "Parcial1"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Error en la conexion")
    print("Parametros incorrectos")

 
 #########-------PROGRAMA DE REGISTRO DE ESTUDIANTES ------#########

def opcion_1():
    while True:
        try:
            idregistro=int(input("Ingrese ID del registro = "))
            break
        except ValueError:
            print('Ingrese un valor numerico')

    nombreEstu =str(input("Ingrese su nombre del estudiante: "))

    while True:
        try:
            edad =int(input("Ingrese edad del estudiante: "))
            break
        except ValueError:
            print('Ingrese un valor numerico')

    genero =str(input("Ingrese su genero: "))
    direccion =str(input("Ingrese su direccion: "))
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO RE(idregistro,nombre,edad,genero,direccion) VALUES(%s,%s,%s,%s,%s)",(idregistro,nombreEstu,edad,genero,direccion))
    conexion.commit()
    cursor.close()

def opcion_2():
    print(" ")
    print(" UPDATE ")
    print(" 1. Nombre ")
    print(" 2. Edad ")
    print(" 3. Genero")
    print(" 4. Direccion")
    print(' ')

    opcion1= int(input( 'Eliga el indice de la opcion que desea realizar: '))
    print(' ')
    if opcion1 == 1:
        while True:
            try:
                idregistro=int(input("Ingrese ID del registro = "))
                nombre = input('Ingrese el nombre: ')  
                break
            except ValueError:
                print('Ingrese un valor numerico')
        print("update")        
        cursor = conexion.cursor()
        cursor.execute(" UPDATE RE SET nombre = %s WHERE idregistro = %s", (nombre, idregistro))
        conexion.commit()
        cursor.close()      
    elif opcion1 == 2:
        while True:
            try:
                idregistro=int(input("Ingrese ID del registro = "))
                edad=int(input("Ingrese la nueva EDAD: "))
                break
            except ValueError:
                print('Ingrese un valor numerico')
        print("update")
        cursor = conexion.cursor()
        cursor.execute(" UPDATE RE SET edad = %s WHERE idregistro = %s", (edad, idregistro))
        conexion.commit()
        cursor.close()
    elif opcion1 == 3:
        while True:
            try:
                idregistro=int(input("Ingrese ID del registro = "))
                genero = input('Ingrese genero: ')  
                break
            except ValueError:
                print('Ingrese un valor numerico para ID')
        print("update")        
        cursor = conexion.cursor()
        cursor.execute(" UPDATE RE SET genero = %s WHERE idregistro = %s", (genero, idregistro))
        conexion.commit()
        cursor.close()
    elif opcion1 == 4:
        while True:
            try:
                idregistro=int(input("Ingrese ID del registro = "))
                direccion = input('Ingrese direccion: ')  
                break
            except ValueError:
                print('Ingrese un valor numerico para ID')
        print("update")        
        cursor = conexion.cursor()
        cursor.execute(" UPDATE RE SET direccion = %s WHERE idregistro = %s", (direccion, idregistro))
        conexion.commit()
        cursor.close()

def opcion_3():
    while True:
        try:
            valor=int(input("Ingrese el ID a eliminar: "))
            break
        except ValueError:
            print("Ingrese un valor Numerico")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM RE WHERE idregistro = %s", (valor,))
    conexion.commit()
    cursor.close()
    

def opcion_4():
    print(" Registro de estudiantes ")
    cursor = conexion.cursor()
    SQL= 'SELECT*FROM RE'
    cursor.execute(SQL)
    valores = cursor.fetchall()
    print('id     Nombre   Edad     Genero         direccion')
    for valores in valores:
        print(f"{valores[0]}", ' | ' ,f"{valores[1]}",' | ' ,f"{valores[2]}",' | ' ,f" {valores[3]}",' | ' ,f" {valores[4]}" )
    #print(valores)
    cursor.close()




print(' ')
print("  -----REGISTRO DE ESTUDIANTES-----")
print(' ')


while True:
    try:
        print(' ')
        print(' 1. ¿Desea AGREGAR un nuevo estudiante a la BD? ')
        print(' 2. ¿Desea EDITAR la informacion de un estudiante de la BD? ')   
        print(' 3. ¿Desea ELIMINAR  un  estudiante de la BD? ')
        print(' 4. ¿Desea VER la informacion de los estudiantes de la BD? ')
        print(' ')
        opcion1= int(input( 'Eliga el indice de la opcion que desea realizar: '))
        print(' ')
        if opcion1 == 1:
            opcion_1()
        elif opcion1 == 2:
            opcion_2()
        elif opcion1 == 3:
            opcion_3()
        elif opcion1 == 4:
            opcion_4()
        else:
            break  
               
    except ValueError:
            print('Valores introducidos no son correctos')

conexion.close()    







