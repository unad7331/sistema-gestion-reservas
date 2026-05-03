from abc import ABC, abstractmethod
from excepciones import ErrorServicio


class Servicio(ABC):
    def __init__(self, nombre, precio_base, disponible=True):
        if not nombre or not nombre.strip():
            raise ErrorServicio("El nombre del servicio no puede estar vacío.")
        if precio_base <= 0:
            raise ErrorServicio("El precio base debe ser mayor que cero.")

        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero.")
        subtotal = self.precio_base * duracion
        return subtotal - descuento + impuesto

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero.")
        subtotal = self.precio_base * duracion
        return subtotal - descuento + impuesto

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero.")
        subtotal = self.precio_base * duracion
        return subtotal - descuento + impuesto

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"
