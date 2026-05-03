from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva
from logger import registrar_log


def ejecutar_operacion(numero, descripcion, funcion):
    print(f"\nOperación {numero}: {descripcion}")

    try:
        resultado = funcion()

    except (ErrorCliente, ErrorServicio, ErrorReserva) as error:
        print(f"Error controlado: {error}")
        registrar_log(f"Operación {numero} fallida: {error}")

    except Exception as error:
        print(f"Error inesperado: {error}")
        registrar_log(f"Operación {numero} con error inesperado: {error}")

    else:
        print("Operación exitosa.")
        if resultado is not None:
            print(resultado)

    finally:
        print("Operación finalizada.")


def main():
    clientes = []
    servicios = []
    reservas = []

    ejecutar_operacion(1, "Registrar cliente válido", lambda: clientes.append(
        Cliente(1, "Ana Pérez", "ana@email.com", "3124567890")
    ))

    ejecutar_operacion(2, "Registrar cliente inválido", lambda: clientes.append(
        Cliente(2, "", "correo_malo", "123")
    ))

    ejecutar_operacion(3, "Crear servicio reserva de sala", lambda: servicios.append(
        ReservaSala("Sala de reuniones", 50000)
    ))

    ejecutar_operacion(4, "Crear servicio alquiler de equipo", lambda: servicios.append(
        AlquilerEquipo("Computador portátil", 30000)
    ))

    ejecutar_operacion(5, "Crear asesoría especializada", lambda: servicios.append(
        AsesoriaEspecializada("Asesoría Python", 80000)
    ))

    ejecutar_operacion(6, "Crear servicio inválido", lambda: servicios.append(
        ReservaSala("", -1000)
    ))

    ejecutar_operacion(7, "Crear reserva exitosa", lambda: reservas.append(
        Reserva(clientes[0], servicios[0], 2)
    ))

    ejecutar_operacion(8, "Procesar reserva exitosa", lambda: reservas[0].procesar())

    ejecutar_operacion(9, "Confirmar reserva exitosa", lambda: reservas[0].confirmar())

    ejecutar_operacion(10, "Crear reserva inválida", lambda: reservas.append(
        Reserva(clientes[0], servicios[0], -5)
    ))

    ejecutar_operacion(11, "Cancelar reserva", lambda: reservas[0].cancelar())

    print("\nSistema finalizado sin interrupciones.")


if __name__ == "__main__":
    main()
