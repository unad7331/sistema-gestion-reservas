from excepciones import ErrorReserva
from logger import registrar_log


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ErrorReserva("La reserva debe tener un cliente válido.")
        if servicio is None:
            raise ErrorReserva("La reserva debe tener un servicio válido.")
        if duracion <= 0:
            raise ErrorReserva("La duración de la reserva debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if not self.servicio.disponible:
                raise ErrorReserva("No se puede confirmar. El servicio no está disponible.")

            self.estado = "Confirmada"
            registrar_log("Reserva confirmada correctamente.")

        except ErrorReserva as error:
            registrar_log(f"Error al confirmar reserva: {error}")
            raise

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva("La reserva ya se encuentra cancelada.")

            self.estado = "Cancelada"
            registrar_log("Reserva cancelada correctamente.")

        except ErrorReserva as error:
            registrar_log(f"Error al cancelar reserva: {error}")
            raise

        finally:
            registrar_log("Proceso de cancelación finalizado.")

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as error:
            registrar_log(f"Error al procesar reserva: {error}")
            raise ErrorReserva("No fue posible procesar la reserva.") from error

        else:
            registrar_log("Reserva procesada exitosamente.")
            return costo

    def mostrar_reserva(self):
        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.describir_servicio()} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado}"
        )
