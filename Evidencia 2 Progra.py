import pandas as pd
import os
import numpy as np
import json

nombres_alumnos = []

asignatura_progra = []
asignatura_basedatos = []
asignatura_conta = []
asignatura_estadistica = []
asignatura_macro = []

Separador = ("-" * 80) + "\n"


def reporte_materias_estudiantes():
    alumnos_asignaturas= {nombres_alumnos[0]:[asignatura_progra[0], asignatura_basedatos[0], asignatura_conta[0], asignatura_estadistica[0],
asignatura_macro[0]], nombres_alumnos[1]:[asignatura_progra[1], asignatura_basedatos[1], asignatura_conta[1], asignatura_estadistica[1],
asignatura_macro[1]], nombres_alumnos[2]:[asignatura_progra[2], asignatura_basedatos[2], asignatura_conta[2], asignatura_estadistica[2],
asignatura_macro[2]], nombres_alumnos[3]:[asignatura_progra[3], asignatura_basedatos[3], asignatura_conta[3], asignatura_estadistica[3],
asignatura_macro[3]], nombres_alumnos[4]:[asignatura_progra[4], asignatura_basedatos[4], asignatura_conta[4], asignatura_estadistica[4],
asignatura_macro[4]], nombres_alumnos[5]:[asignatura_progra[5], asignatura_basedatos[5], asignatura_conta[5], asignatura_estadistica[5],
asignatura_macro[5]], nombres_alumnos[6]:[asignatura_progra[6], asignatura_basedatos[6], asignatura_conta[6], asignatura_estadistica[6],
asignatura_macro[6]], nombres_alumnos[7]:[asignatura_progra[7], asignatura_basedatos[7], asignatura_conta[7], asignatura_estadistica[7],
asignatura_macro[7]], nombres_alumnos[8]:[asignatura_progra[8], asignatura_basedatos[8], asignatura_conta[8], asignatura_estadistica[8],
asignatura_macro[8]], nombres_alumnos[9]:[asignatura_progra[9], asignatura_basedatos[9], asignatura_conta[9], asignatura_estadistica[9],
asignatura_macro[9]], nombres_alumnos[10]:[asignatura_progra[10], asignatura_basedatos[10], asignatura_conta[10], asignatura_estadistica[10],
asignatura_macro[10]], nombres_alumnos[11]:[asignatura_progra[11], asignatura_basedatos[11], asignatura_conta[11], asignatura_estadistica[11],
asignatura_macro[11]], nombres_alumnos[12]:[asignatura_progra[12], asignatura_basedatos[12], asignatura_conta[12], asignatura_estadistica[12],
asignatura_macro[12]], nombres_alumnos[13]:[asignatura_progra[13], asignatura_basedatos[13], asignatura_conta[13], asignatura_estadistica[13],
asignatura_macro[13]], nombres_alumnos[14]:[asignatura_progra[14], asignatura_basedatos[14], asignatura_conta[14], asignatura_estadistica[14],
asignatura_macro[14]], nombres_alumnos[15]:[asignatura_progra[15], asignatura_basedatos[15], asignatura_conta[15], asignatura_estadistica[15],
asignatura_macro[15]], nombres_alumnos[16]:[asignatura_progra[16], asignatura_basedatos[16], asignatura_conta[16], asignatura_estadistica[16],
asignatura_macro[16]], nombres_alumnos[17]:[asignatura_progra[17], asignatura_basedatos[17], asignatura_conta[17], asignatura_estadistica[17],
asignatura_macro[17]], nombres_alumnos[18]:[asignatura_progra[18], asignatura_basedatos[18], asignatura_conta[18], asignatura_estadistica[18],
asignatura_macro[18]], nombres_alumnos[19]:[asignatura_progra[19], asignatura_basedatos[19], asignatura_conta[19], asignatura_estadistica[19],
asignatura_macro[19]], nombres_alumnos[20]:[asignatura_progra[20], asignatura_basedatos[20], asignatura_conta[20], asignatura_estadistica[20],
asignatura_macro[20]], nombres_alumnos[21]:[asignatura_progra[21], asignatura_basedatos[21], asignatura_conta[21], asignatura_estadistica[21],
asignatura_macro[21]], nombres_alumnos[22]:[asignatura_progra[22], asignatura_basedatos[22], asignatura_conta[22], asignatura_estadistica[22],
asignatura_macro[22]], nombres_alumnos[23]:[asignatura_progra[23], asignatura_basedatos[23], asignatura_conta[23], asignatura_estadistica[23],
asignatura_macro[23]], nombres_alumnos[24]:[asignatura_progra[24], asignatura_basedatos[24], asignatura_conta[24], asignatura_estadistica[24],
asignatura_macro[24]], nombres_alumnos[25]:[asignatura_progra[25], asignatura_basedatos[25], asignatura_conta[25], asignatura_estadistica[25],
asignatura_macro[25]], nombres_alumnos[26]:[asignatura_progra[26], asignatura_basedatos[26], asignatura_conta[26], asignatura_estadistica[26],
asignatura_macro[26]], nombres_alumnos[27]:[asignatura_progra[27], asignatura_basedatos[27], asignatura_conta[27], asignatura_estadistica[27],
asignatura_macro[27]], nombres_alumnos[28]:[asignatura_progra[28], asignatura_basedatos[28], asignatura_conta[28], asignatura_estadistica[28],
asignatura_macro[28]], nombres_alumnos[29]:[asignatura_progra[29], asignatura_basedatos[29], asignatura_conta[29], asignatura_estadistica[29],
asignatura_macro[29]]}
    frame_totales = pd.DataFrame(alumnos_asignaturas)
    frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
    estadisticos_descriptivos_estudiantes= frame_totales.T.describe()
    opciones=0
    while opciones != 5:
        print(Separador)
        print("----- Reporte Estadistico Descriptivo por materia y por estudiante -----")
        print("[1] Mostrar reporte estadístico descriptivo por materia")
        print("[2] Mostrar reporte estadístico descriptivo por estudiante")
        print("[3] Exportar reporte estadístico descriptivo por materia")
        print("[4] Exportar reporte estadístico descriptivo por estudiante")
        print("[5] Regresar al menú principal")
        i= input("Selecciona una opción del menú: ")
        if i =="1":
            print("Reporte Estadístico Descriptivo por materia")
            print(estadisticos_descriptivos_estudiantes)
        elif i =="2":
            
            for est in alumnos_asignaturas:
                print("\nReporte Estadistico Descriptivo por estudiante:")
                print(" ")
                print("Alumno:",est)
                reportes_calf = frame_totales[est].describe()
                print(reportes_calf)
                reporte_estudiante= frame_totales.describe()
        elif i =="3":
            print("Exportar reporte por materia a txt")
            estadisticos_descriptivos_estudiantes.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_materia.txt')
        elif i =="4":
            print("Exportar reporte por estudiante a txt")
            reporte_estudiante.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_estudiante.txt')
        elif i =="5":
            opciones= 5
        else:
            print("Selecciona una opción del menú: ")


def menu():
    OpcionMenu = 0
    salir = 10
    
    while OpcionMenu != salir:
        print("---MENU--- Seleccione la opcion deseada: \n [1] Ingresar Alumnos \n [2] Ingresar Calificaciones de Estructuras de datos y su procesamiento \n [3] Ingresar Calificaciones de Programación de bases de datos \n [4] Ingresar Calificaciones de Contabilidad Administrativa \n [5] Ingresar Calificaciones de Estadística descriptiva \n [6] Ingresar Calificaciones de Macroeconomía \n [7] Mostrar todas las calificaciones del alumnado \n [8] Asignaturas con el desempeño más bajo \n [9] Alumnos que reprobaron dos o más asignaturas \n [10] Exportar a disco el listado de las Calif. de estudiantes en formato CSV \n [11] Exportar a disco el listado de las Calif. de estudiantes en formato JSON \n [12] Reporte Estadistico Descriptivo por materia y por estudiante \n [13] Cerrar programa")
        opcion = input()
        
        if opcion == "1":
            print (" ---- Has seleccionado ingresar los nombres de 30 alumnos ---- ")
            for nombres in range(30):
                nombres_alumnos.append(input("Nombres de los Alumnos iniciando por su apellido paterno: " ))
                #nombres_alumnos.sort()
                print(nombres_alumnos)
                os.system('cls')
        
        if opcion == "2":
            for calif_progra in range(30):
                asignatura_progra.append(int(input("Dime la calificación de la asignatura Estructuras de datos y su procesamiento: ")))
                print(asignatura_progra)
                os.system('cls')
        
        if opcion == "3":
            for calif_basedatos in range(30):
                asignatura_basedatos.append(int(input("Dime la calificación de la asignatura Programación de bases de datos: ")))
                print(asignatura_basedatos)
                os.system('cls')
    
        if opcion == "4":
            for calif_conta in range(30):
                asignatura_conta.append(int(input("Dime la calificación de la asignatura Contabilidad Administrativa: ")))
                print(asignatura_conta)
                os.system('cls')

        if opcion == "5":
            for calif_estadistica in range(30):
                asignatura_estadistica.append(int(input("Dime la calificación de la asignatura Estadística descriptiva: ")))
                print(asignatura_estadistica)
                os.system('cls')

        if opcion == "6":
            for calif_macro in range(30):
                asignatura_macro.append(int(input("Dime la calificación de la asignatura Macroeconomía: ")))
                print(asignatura_macro)
                os.system('cls')
        
        if opcion == "7":
            alumnos_asignaturas= {nombres_alumnos[0]:[asignatura_progra[0], asignatura_basedatos[0], asignatura_conta[0], asignatura_estadistica[0],
asignatura_macro[0]], nombres_alumnos[1]:[asignatura_progra[1], asignatura_basedatos[1], asignatura_conta[1], asignatura_estadistica[1],
asignatura_macro[1]], nombres_alumnos[2]:[asignatura_progra[2], asignatura_basedatos[2], asignatura_conta[2], asignatura_estadistica[2],
asignatura_macro[2]], nombres_alumnos[3]:[asignatura_progra[3], asignatura_basedatos[3], asignatura_conta[3], asignatura_estadistica[3],
asignatura_macro[3]], nombres_alumnos[4]:[asignatura_progra[4], asignatura_basedatos[4], asignatura_conta[4], asignatura_estadistica[4],
asignatura_macro[4]], nombres_alumnos[5]:[asignatura_progra[5], asignatura_basedatos[5], asignatura_conta[5], asignatura_estadistica[5],
asignatura_macro[5]], nombres_alumnos[6]:[asignatura_progra[6], asignatura_basedatos[6], asignatura_conta[6], asignatura_estadistica[6],
asignatura_macro[6]], nombres_alumnos[7]:[asignatura_progra[7], asignatura_basedatos[7], asignatura_conta[7], asignatura_estadistica[7],
asignatura_macro[7]], nombres_alumnos[8]:[asignatura_progra[8], asignatura_basedatos[8], asignatura_conta[8], asignatura_estadistica[8],
asignatura_macro[8]], nombres_alumnos[9]:[asignatura_progra[9], asignatura_basedatos[9], asignatura_conta[9], asignatura_estadistica[9],
asignatura_macro[9]], nombres_alumnos[10]:[asignatura_progra[10], asignatura_basedatos[10], asignatura_conta[10], asignatura_estadistica[10],
asignatura_macro[10]], nombres_alumnos[11]:[asignatura_progra[11], asignatura_basedatos[11], asignatura_conta[11], asignatura_estadistica[11],
asignatura_macro[11]], nombres_alumnos[12]:[asignatura_progra[12], asignatura_basedatos[12], asignatura_conta[12], asignatura_estadistica[12],
asignatura_macro[12]], nombres_alumnos[13]:[asignatura_progra[13], asignatura_basedatos[13], asignatura_conta[13], asignatura_estadistica[13],
asignatura_macro[13]], nombres_alumnos[14]:[asignatura_progra[14], asignatura_basedatos[14], asignatura_conta[14], asignatura_estadistica[14],
asignatura_macro[14]], nombres_alumnos[15]:[asignatura_progra[15], asignatura_basedatos[15], asignatura_conta[15], asignatura_estadistica[15],
asignatura_macro[15]], nombres_alumnos[16]:[asignatura_progra[16], asignatura_basedatos[16], asignatura_conta[16], asignatura_estadistica[16],
asignatura_macro[16]], nombres_alumnos[17]:[asignatura_progra[17], asignatura_basedatos[17], asignatura_conta[17], asignatura_estadistica[17],
asignatura_macro[17]], nombres_alumnos[18]:[asignatura_progra[18], asignatura_basedatos[18], asignatura_conta[18], asignatura_estadistica[18],
asignatura_macro[18]], nombres_alumnos[19]:[asignatura_progra[19], asignatura_basedatos[19], asignatura_conta[19], asignatura_estadistica[19],
asignatura_macro[19]], nombres_alumnos[20]:[asignatura_progra[20], asignatura_basedatos[20], asignatura_conta[20], asignatura_estadistica[20],
asignatura_macro[20]], nombres_alumnos[21]:[asignatura_progra[21], asignatura_basedatos[21], asignatura_conta[21], asignatura_estadistica[21],
asignatura_macro[21]], nombres_alumnos[22]:[asignatura_progra[22], asignatura_basedatos[22], asignatura_conta[22], asignatura_estadistica[22],
asignatura_macro[22]], nombres_alumnos[23]:[asignatura_progra[23], asignatura_basedatos[23], asignatura_conta[23], asignatura_estadistica[23],
asignatura_macro[23]], nombres_alumnos[24]:[asignatura_progra[24], asignatura_basedatos[24], asignatura_conta[24], asignatura_estadistica[24],
asignatura_macro[24]], nombres_alumnos[25]:[asignatura_progra[25], asignatura_basedatos[25], asignatura_conta[25], asignatura_estadistica[25],
asignatura_macro[25]], nombres_alumnos[26]:[asignatura_progra[26], asignatura_basedatos[26], asignatura_conta[26], asignatura_estadistica[26],
asignatura_macro[26]], nombres_alumnos[27]:[asignatura_progra[27], asignatura_basedatos[27], asignatura_conta[27], asignatura_estadistica[27],
asignatura_macro[27]], nombres_alumnos[28]:[asignatura_progra[28], asignatura_basedatos[28], asignatura_conta[28], asignatura_estadistica[28],
asignatura_macro[28]], nombres_alumnos[29]:[asignatura_progra[29], asignatura_basedatos[29], asignatura_conta[29], asignatura_estadistica[29],
asignatura_macro[29]]}
            
            frame_totales = pd.DataFrame(alumnos_asignaturas)
            frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
            print(Separador)
            print(frame_totales.T)
            os.system('cls')
            
 
        if opcion == "8":
            print(Separador)
            print("Estas son las asignaturas con sus estadísticos descriptivos:")
            frame_totales = pd.DataFrame(alumnos_asignaturas)
            frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
            estadisticos_descriptivos = frame_totales.T.describe()
            print(estadisticos_descriptivos)
            
            print(Separador)
            print("Estos son los promedios finales de las asignaturas:")
            promedio_asignaturas= frame_totales.T.mean()
            print(promedio_asignaturas)
            
            print(Separador)
            print("Este fue el promedio más bajo de las asignaturas:")
            promedio_bajo= promedio_asignaturas.min()
            print(promedio_bajo)
            #promedio_asignaturas= frame_totales.mean()
            #print(promedio_asignaturas)
            
            #print("Este fue el promedio más bajo de las materias:")
            #promedio_bajo= promedio_asignaturas.min()
            #print(promedio_bajo)
            os.system('cls')
            
        if opcion == "9":
            print(Separador)
            print("Estos son los alumnos que no acreditaron:")
            reprobados=frame_totales[frame_totales <= 69]
            print(reprobados.T)
            os.system('cls')
        
        if opcion == "10":
            print(Separador)
            print("Se ha exportado a disco el listado de las calificaciones obtenidas por los estudiantes en formato CSV, favor de verificar su escritorio.")
            frame_totales.T.to_csv(r'C:\Users\TortillaCaliente\Desktop\export_dataframe.csv')
            print(Separador)
            
        if opcion == "11":
            print(Separador)
            print("Se ha exportado a disco el listado de las calificaciones obtenidas por los estudiantes en formato JSON, favor de verificar su escritorio.")
            frame_totales.T.to_json(r'C:\Users\TortillaCaliente\Desktop\export_dataframe.json')
            print(Separador)
            
        if opcion =="12":
            reporte_materias_estudiantes()
            
            #alumnos_asignaturas= {nombres_alumnos[0]:[asignatura_progra[0], asignatura_basedatos[0], asignatura_conta[0], asignatura_estadistica[0],
#asignatura_macro[0]], nombres_alumnos[1]:[asignatura_progra[1], asignatura_basedatos[1], asignatura_conta[1], asignatura_estadistica[1],
#asignatura_macro[1]], nombres_alumnos[2]:[asignatura_progra[2], asignatura_basedatos[2], asignatura_conta[2], asignatura_estadistica[2],
#asignatura_macro[2]]}
 #           print(Separador)
  #          frame_totales = pd.DataFrame(alumnos_asignaturas)
   #         frame_totales.index=["Progra", "Base", "Conta ", "Estadística ", "Macro"]
    #        print(Separador)
     #       print("\nReporte Estadistico Descriptivo por materia:")
      #      estadisticos_descriptivos_estudiantes= frame_totales.T.describe()
       #     print(estadisticos_descriptivos_estudiantes)
        #    estadisticos_descriptivos_estudiantes.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_materia.txt')
            
            
         #   for est in alumnos_asignaturas:
               # print("\nReporte Estadistico Descriptivo por estudiante:")
              #  print(" ")
            #    print("Alumno:",est)
             #   reportes_calf = frame_totales[est].describe()
           #     print(reportes_calf)
                #frame_totales.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_estudiante.txt')
          #      reporte_estudiante= frame_totales.describe()
                #reporte_estudiante.to_csv(r'C:\Users\TortillaCaliente\Desktop\reporte_estudiante.txt')
                
            #os.system('cls')
            
        
        if opcion == "13":
            print("Se ha cerrado el programa...")
            os.system('cls')
            break

menu()
