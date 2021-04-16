class Autentificacion:
    
    def leerTarjeta(self) -> str:
        return "Autentificaion: leer tarjeta"    

    def introducirClave(self)-> str:
        return "Autentificaion: introducir clave"

    def comprobarClave(self)-> str:
        return "Autentificaion: leer comprobar clave"

    def obtenerCuenta(self)-> str:
        return "Autentificaion: obetener cuenta"

    def alFallar(self)-> str:
        return "Autentificaion: al fallar"




class Cajero:
    def introducirCantidad(self):
        return "Cajero: introducir cantidad"
    def tieneSaldo(self):
        return "Cajero: tiene saldo"
    def expedirDinero(self):
        return "Cajero: expedir dinero"
    def imprimirTicket(self):
        return "Cajero: imprimir ticket"


class Cuenta:


    def comprobarSaldoDisponible(self):
        return "Cuenta: comprobar saldo disponible"

    def bloquearCuenta(self):
        return "Cuenta: bloquear cuenta"

    def desbloquearCuenta(self):
        return "Cuenta: desbloquear cuenta"

    def retirarSaldo(self):
        return "Cuenta: retirar saldo"

    def actualizarCuenta(self):
        return "Cuenta: actualizar cuenta"

    def alFallar(self):
        return "Cuenta: al fallar"


class Facade:

    def __init__(self, 
        autentificacion: Autentificacion,
        cajero: Cajero,
        cuenta: Cuenta    
    ) -> None:
        self._autentificacion = autentificacion or Autentificacion()
        self._cajero = cajero or Cajero()
        self._cuenta = cuenta or Cuenta()

    def operation(self) -> str:


        results = []
        results.append("Fachada inicializa los subsistemas:")
        results.append(self._autentificacion.leerTarjeta())
        results.append(self._autentificacion.introducirClave())
        results.append(self._autentificacion.comprobarClave())
        results.append(self._autentificacion.obtenerCuenta())
        results.append(self._autentificacion.alFallar())
        results.append(self._cajero.introducirCantidad())
        results.append(self._cajero.tieneSaldo())
        results.append(self._cajero.expedirDinero())
        results.append(self._cajero.imprimirTicket())
        results.append(self._cuenta.comprobarSaldoDisponible())
        results.append(self._cuenta.bloquearCuenta())
        results.append(self._cuenta.desbloquearCuenta())
        results.append(self._cuenta.retirarSaldo())
        results.append(self._cuenta.actualizarCuenta())
        results.append(self._cuenta.alFallar())
        return "\n".join(results)


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    autentificacion = Autentificacion()
    cajero = Cajero()
    cuenta = Cuenta()
    
    facade = Facade(autentificacion, cajero,cuenta)
    client_code(facade)
