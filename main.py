#definicion de registros y datos a utilizar
registro_mascotas = []
registro_turnos = []
registro_atenciones = []



#funciones con sus procedimientos

def menu_principal():
    print()
    print("1 - Registrar una mascota")
    print("2 - Ver mascotas")
    print("3 - Registrar un turno")
    print("4 - Mostrar turnos")
    print("5 - Registrar atencion")
    print("6 - atenciones realizadas")
    print("7 - estadisticas")
    print("0 - salir del menu")
    
#mensaje inicial
def cartel_veterinaria():
    print("============================================")
    print("     SISTEMA VETERINARIA     ")
    print("============================================")


#programa principal donde va todo
def main():
    cartel_veterinaria()
    menu_principal()

#Programa principal
main()
