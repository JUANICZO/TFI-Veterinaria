#importaciones
from dataclasses import dataclass


#definicion de registros y datos a utilizar
registro_mascotas = []
registro_turnos = []
registro_atenciones = []


@dataclass
class mascota:
    nombre: str
    especie: str
    raza: str
    edad: str
    nombre_duenio: str
    telefono_duenio: str
    
@dataclass
class turno:
    nombre_mascota: str
    nombre_duenio: str
    especie: str
    fecha: str
    hora: str
    motivo: str

@dataclass
class atencion:
    nombre_mascota : str
    especie : str
    nombre_duenio : str
    fecha : str
    diagnostico : str
    motivo : str
    tratamiento : str
    veterinario : str

#funciones con sus procedimientos

#comienzo ingreso de mascota
def ingreso_datos_mascota():
    print("FORMULARIO DE INGRESO DE MASCOTA")
    nombre = input("\ningrese el nombre de la mascota: ")
    especie = input("\ningrese la especie(Perro, Gato; etc): ")
    raza = input("\nIngrese la raza: ")
    edad = input("\nIngrese su edad: ")
    nombre_duenio = input("\nIngrese el nombre del dueño: ")
    telefono_duenio = input("\nIngrese el numero de telefono del dueño: ")

    return mascota(nombre, especie, raza, edad, nombre_duenio, telefono_duenio)

#funcion que carga la mascota en el registro
def cargar_nueva_mascota_en_registro(nueva_mascota):
    registro_mascotas.append(nueva_mascota)
    print(f"¡{nueva_mascota.nombre} fue agregada/o con exito")

def cargar_mascota():
    decision_seguir = "S"
    while decision_seguir == "S":
        mascota_creada =  ingreso_datos_mascota()
        cargar_nueva_mascota_en_registro(mascota_creada)
        decision_seguir = input("\nDesea registrar otra mascota? (S/N): ").upper()
    print("\nVolviendo al menu inicial...")
#fin ingreso mascota

#inicio funcion de mostrar registro de mascota
def mostrar_mascotas(registro_mascotas): #aca acordate que cuando llames la funcion en el menu tenes que mandarle en el parentesis el registro para que trabaje con eso

    if not(registro_mascotas):
        print("No hay mascotas registradas.")

    else:

        print("\n========== MASCOTAS REGISTRADAS ==========\n")

        numero = 1

        for mascota in registro_mascotas:

            print(f"Mascota N° {numero}")

            print("Nombre:", mascota.nombre)
            print("Especie:", mascota.especie)
            print("Raza:", mascota.raza)
            print("Edad:", mascota.edad)
            print("Dueño:", mascota.nombre_duenio)
            print("Teléfono:", mascota.telefono_duenio)
            
            print("---------------------------------------")

            numero += 1
#fin de funcion de mostrar registro de mascota
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#inicio funcion registrar turno
def ingreso_datos_turno_mascota():
    print("=========================INGRESE LOS DATOS PARA EL REGISTRO DE TURNOS=========================")
    nombre_mascota = input("\ningrese el nombre de la mascota: ")
    nombre_duenio = input("\ningrese el nombre del dueño: ")
    especie = input("\ningrese la especie de la  mascota (perro, gato, conejo, etc): ")
    fecha = input("\ningrese la fecha asignada para el turno(DIA/MES/AÑO): ")
    hora = input("\ningrese el horario asignado (formato 24hs): ")
    motivo = input("\ningrese el motivo de la consulta (vacunación-castración-control-etc): ")

    return turno(nombre_mascota, nombre_duenio, especie, fecha, hora, motivo)
#fin funcion registrar turno

#inicio funcion agregar turno al registro
def cargar_turno_al_registro(nuevo_turno):
    registro_turnos.append(nuevo_turno)
    print(f"El turno de {nuevo_turno.nombre_mascota} fue agendado con exito!")
#fin funcion agregar turno al registro

#inicio funcion cargar turno
def cargar_turno():
    decision = "S"
    while decision == "S":
        turno_creado = ingreso_datos_turno_mascota()
        cargar_turno_al_registro(turno_creado)
        decision = input("\nDesea registrar otro turno? (S/N): ").upper()
    print("Volviendo al menu principal")
#fin funcion cargar turno

#inicio funcion mostrar turnos
def mostrar_turnos(registro_turnos):
    if not(registro_turnos):
        print("No hay mascotas con turnos asignados.")
    else:

        print("\n========== LISTA DE TURNOS ==========\n")

        numero = 1

        for turno in registro_turnos:

            print(f"Mascota N° {numero}")

            print("Nombre:", turno.nombre_mascota)
            print("Especie:", turno.especie)
            print("nombre del dueño:", turno.nombre_duenio)
            print("fecha:", turno.fecha)
            print("hora:", turno.hora)
            print("motivo:", turno.motivo)
            numero += 1
            print("---------------------------------------")
#fin funcion mostrar turnos
#------------------------------------------------------------------------------------------------------------------------
#inicio funcion ingresar datos de atencion

def ingresar_datos_atencion():
    print("=========================INGRESE LOS DATOS PARA EL REGISTRO DE ATENCIONES=========================")
    nombre_mascota = input("\ningrese el nombre de la mascota: ")
    especie = input("\ningrese la especie de la  mascota (perro, gato, conejo, etc): ")
    nombre_duenio = input("\ningrese el nombre del dueño: ")
    fecha = input("\ningrese la fecha asignada de la atencion(DIA/MES/AÑO): ")
    diagnostico = input("\ningrese el diagnostico (animal sano, etc): ")
    motivo = input("\ningrese el motivo(vacunacion, control, etc): ")
    tratamiento = input("\ningrese el tratamiento aplicado: ")
    veterinario = input("\ningrese el nombre del veterinario encargado: ")

    return atencion(nombre_mascota, especie, nombre_duenio, fecha, diagnostico, motivo, tratamiento, veterinario)
#fin funcion ingresar datos de atencion

#inicio funcion cargar atencion al registro
def cargar_atencion_al_registro(nueva_atencion):
    registro_atenciones.append(nueva_atencion)
    print(f"la atencion de {nueva_atencion.nombre_mascota} fue registrada con exito")
#fin funcion cargar atencion al registro

#inicio funcion cargar atencion

def cargar_atencion():
    decision = "S"
    while decision == "S":
        atencion_cargada = ingresar_datos_atencion()
        cargar_atencion_al_registro(atencion_cargada)
        decision = input("\nDesea registrar otro turno? (S/N): ").upper()
    print("Volviendo al menu principal")
#fin funcion cargar atencion

#inicio funcion mostrar atenciones

def mostrar_atenciones(registro_atenciones):
    if not(registro_atenciones):
        print("no hay atenciones registradas")
    else:
        print("=========================================LISTA DE ATENCIONES=========================================")
        numero = 1
        for atencion in registro_atenciones:
            print(f"Mascota N° {numero}")
            print("Nombre de la mascota: ",atencion.nombre_mascota)
            print("Especie de la mascota: ", atencion.especie)
            print("Nombre del dueño: ",atencion.nombre_duenio)
            print("Fecha de la atencion: ", atencion.fecha)
            print("diagnostico: ",atencion.diagnostico)
            print("motivo: ", atencion.motivo)
            print("tratamiento: ", atencion.tratamiento)
            print("veterinario encargado: ", atencion.veterinario)
            numero += 1
            print("----------------------------------------------------------------------------------------------------")


#fin funcion mostrar atenciones


#muestra menu
def menu_principal():
    while True:
        print()
        print("1 - Registrar una mascota")
        print("2 - Ver mascotas")
        print("3 - Registrar un turno")
        print("4 - Mostrar turnos")
        print("5 - Registrar atencion")
        print("6 - atenciones realizadas")
        print("0 - salir del menu")
        decision_menu = (int(input("ingrese una opcion: ")))
   
        match decision_menu:
            case 1:
                cargar_mascota()
            case 2:
                mostrar_mascotas(registro_mascotas)
            case 3:
                cargar_turno()
            case 4:
                mostrar_turnos(registro_turnos)
            case 5:
                cargar_atencion()
            case 6:
                mostrar_atenciones(registro_atenciones)
            case 7:
                pass
            case 0:
                print("gracias por usar el sistema hasta luego")
                break
    
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
