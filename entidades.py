from abc import ABC, abstractmethod

class EntidadSistema(ABC):
    """
    Clase abstracta base del sistema
    """

    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass
