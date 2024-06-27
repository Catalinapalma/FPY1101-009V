
import os

libros=[]
lib=["alas de hierro", "la sombra de sirena"]

def registro():
    try: 
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el Autor del libro: ")
        ano= int(input("Ingrese el año de Publicación:  "))
        sku= int(input("Ingrese el SKU:  "))

        if titulo  or autor  or ano or sku <=0:
            print("Faltan datos por ingresar")
        else:
            libro= {
            'titulo':titulo,
            'auto': autor,
            'Año' : ano,
            'SKU': sku
            }
            libros.append(libro)
            print("El registro se realizo correctamente")
    
    except ValueError:
        print("Dato erroneo. Intente nuevamente")

def prestar():

    try: 
        nombre= input("Ingrese el nombre de usuario: ")
        sku =int(input("Ingrese el SKU del libro"))
    except ValueError:
        print("Dato erroneo. Intentelo nuevamente")




def listar():
    print("titulo\t\t Autor\t\tAño \t\t SKU\n")
    for libro in libros:
        print(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['Año']}\t\t{libro['SKU']}\n")

def imprimir():
    try:
        op = int("¿Desea imprimir el reporte de los libros prestados? \n 1.todos \n2.Libro solicitado")

        if op ==1:
            with open("planilla_libro.txt", "w") as archivo:
                archivo.write("titulo\t\t Autor\t\tAño \t\t SKU\n")
            for libro in libros:
                archivo.write(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['Año']}\t\t{libro['SKU']}\n")
                print ("Planilla registrada exitosamente en: ", os.getcwd())
        elif op ==2:
            lib =input("Ingrese el libro:").lower()
            if not lib in libros:
                print("El libro no existe")
            else:
                with open(f'planilla_{libro}.txt', 'w') as archivo:
                    archivo.write("titulo\t\t Autor\t\tAño\t\tSKU")
                    for libro in libros:
                        if libro['lib'].lower()==lib:
                            archivo.write(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['Año']}\t\t{libro['SKU']}\n")
                
                print("Planilla creada exitosamente en: ", os.getcwd ())
    except ValueError:
        print("Dato erroneo. Intentelo nuevamente")                    

    
def menu():
    while True:
        print("***MENU  BIBLIOTECARIO***")
        print("Ingrese una opcion valida: ")
        op = int(input("Ingrese una opcion: "))

        if op ==1:
            registro()
        elif op==2:
            prestar()
        elif op==3:
            listar()
        elif op ==4:
            imprimir()
        elif op ==5:
            salir()
        else:
            print("La opcion ingresada no es valida")    



        
