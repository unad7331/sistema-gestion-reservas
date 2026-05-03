from entidades import EntidadSistema
from excepciones import ErrorCliente

class Cliente(EntidadSistema):
    """
    Clase Cliente con encapsulación y validaciones.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.__nombre = None
        self.__correo = None
        self.__telefono = None

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ErrorCliente("El nombre del cliente no puede estar vacío.")
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            raise ErrorCliente("El correo electrónico no es válido.")
        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise ErrorCliente("El teléfono debe ser numérico y tener mínimo 7 dígitos.")
        self.__telefono = valor

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo} | Teléfono: {self.__telefono}"
