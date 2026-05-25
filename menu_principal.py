import os
import time

def limpiar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

practicas = {
    "1": {
        "titulo": "MENU PRACTICA 1: ARREGLOS",
        "items": {
            "1": ("Abecedario arreglos", 'python "Practica 1/abecedario arreglos.py"'),
            "2": ("Abecedario normal",  'python "Practica 1/abecedario.py"'),
            "3": ("Calificaciones",     'python "Practica 1/calificaciones.py"'),
            "4": ("Calificaciones 2",   'python "Practica 1/calificaciones 2.py"'),
            "5": ("Toneladas",          'python "Practica 1/toneladas.py"')
        }
    },
    "2": {
        "titulo": "MENU PRACTICA 2: MATRICES Y DATOS",
        "items": {
            "1": ("Asientos",                   'python "Practica 2/Asientos.py"'),
            "2": ("Coordenadas",                'python "Practica 2/Coordenadas.py"'),
            "3": ("Dataframe (Housing)",        'python "Practica 2/dataframe.py"'),
            "4": ("Multiplicacion de matrices", 'python "Practica 2/Multiplicacion matrices.py"')
        }
    },
    "3": {
        "titulo": "MENU PRACTICA 3: COLAS",
        "items": {
            "1": ("Bicolas",            'python "Practica 3/bicolas.py"'),
            "2": ("Colas",              'python "Practica 3/colas.py"'),
            "3": ("Terminal Banco (V1)", 'python "Practica 3/terminal_banco.py"'),
            "4": ("Terminal Banco (V2)", 'python "Practica 3/terminal_bancoV2.py"')
        }
    },
    "4": {
        "titulo": "MENU PRACTICA 4: BICOLAS AVANZADAS",
        "items": {
            "1": ("Bicolas circulares", 'python "Practica 4/bicolas circulares.py"'),
            "2": ("Solicitudes",        'python "Practica 4/Solicitudes.py"'),
            "3": ("Tareas",             'python "Practica 4/Tareas.py"')
        }
    },
    "5": {
        "titulo": "MENU PRACTICA 5: PILAS",
        "items": {
            "1": ("Clase Pila",         'python "Practica 5/Pila.py"'),
            "2": ("Menor a mayor",      'python "Practica 5/menor a mayor.py"')
        }
    },
    "6": {
        "titulo": "MENU PRACTICA 6: ARBOLES BINARIOS",
        "items": {
            "1": ("Árbol base",                  'python "Practica 6/arbol.py"'),
            "2": ("Construcción de árbol binario", 'python "Practica 6/Construccion de arbol binario.py"')
        }
    },
    "7": {
        "titulo": "MENU PRACTICA 7: GRAFOS Y RECURSIVIDAD",
        "items": {
            "1": ("Algoritmo de Dijkstra", 'python "Practica 7/dijkstra.py"'),
            "2": ("Recorrido BFS Grafos",  'python "Practica 7/grafos.py"'),
            "3": ("Torres de Hanoi",       'python "Practica 7/torres de hanoi.py"')
        }
    }
}

def mostrar_sub_menu(num_p):
    while True:
        limpiar()
        p_info = practicas[num_p]
        print(f"--- {p_info['titulo']} ---")
        
        for opcion, datos in p_info["items"].items():
            print(f"{opcion}. {datos[0]}")
        
        opcion_volver = len(p_info["items"]) + 1
        print(f"{opcion_volver}. Volver")
        print("-" * len(p_info['titulo']))
        
        opc = input("Selecciona una opcion: ").strip()
        
        if opc in p_info["items"]:
            limpiar()
            os.system(p_info["items"][opc][1])
            print("\n---------------------------------")
            input("Presiona Enter para continuar...")
        elif opc == str(opcion_volver):
            break
        else:
            print("Opcion incorrecta, intenta de nuevo...")
            time.sleep(1)

def main():
    while True:
        limpiar()
        print("====================================")
        print("   MENU PRINCIPAL - PRACTICAS ED    ")
        print("====================================")
        print("1. Practica 1")
        print("2. Practica 2")
        print("3. Practica 3")
        print("4. Practica 4")
        print("5. Practica 5")
        print("6. Practica 6")
        print("7. Practica 7")
        print("8. Salir del programa")
        print("====================================")
        
        opcion = input("Elige el numero de practica: ").strip()
        
        if opcion in practicas:
            mostrar_sub_menu(opcion)
        elif opcion == "8":
            limpiar()
            print("Saliendo del menu... ¡Adios!")
            break
        else:
            print("Opcion no valida o inexistente.")
            time.sleep(1)

main()