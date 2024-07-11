trabajadores = ["Juan Perez","Maria Garcia",
                "Carlos Lopez","Ana Martinez",
                "Pedro Rodriguez","Laura Hernandez",
                "Miguel Sanchez","Isabel Gomez",
                "Fracisco Dias","Elena Fernandez"]


sueldo=0

def sueldos_alea():
    print("Generando sueldos...")
    if sueldo>=300000 and sueldo<=2500000:
            print(f"Juan Perez:      {sueldo}")
            print(f"Maria Garcia:    {sueldo}")
            print(f"Carlos Lopez:    {sueldo}")
            print(f"Ana Martinez:    {sueldo}")
            print(f"Pedro Rodriguez: {sueldo}")
            print(f"Laura Hernandez: {sueldo}")
            print(f"Miguel Sanchez:  {sueldo}")
            print(f"Isabel Gomez:    {sueldo}")
            print(f"Francisco Dias:  {sueldo}")
            print(f"Elena Fernandez: {sueldo}")

def clas_sueldos():
    print("")








def menu():
    while True:
        print("""
            ~~~~~~~~~~~~~~~
               EMPLEADOS
            ~~~~~~~~~~~~~~~
              
            1.- Asignar sueldos aleatorios
            2.- Clasificar sueldos
            3.- Ver estadisticas
            4.- Reporte de sueldos
            5.- Salir del programa
              """)
        try:
            opciones = int(input("Ingrese la opcion: "))
            if opciones>=1 and opciones<=5:
                if opciones==1:
                    sueldos_alea()
                elif opciones==2:
                    print("no")
                elif opciones==3:
                    print("quizas")
                elif opciones==4:
                    print("meh")
                elif opciones==5:
                    print("Finalizado programa...")
                    print("Desarrollado por Rodolfo Arellano")
                    print("RUT 21.701.819-6")
                    break
        except ValueError:
            print("INGRESE UNA OPCION DISPONIBLE!!!")
menu()