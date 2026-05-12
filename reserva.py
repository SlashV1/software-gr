# modelos/reserva.py

from excepciones.excepciones_personalizadas import ReservaError
from utilidades.logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor a 0"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # CONFIRMAR RESERVA

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError(
                    "El costo de la reserva es inválido"
                )

            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para "
                f"{self.cliente.nombre}"
            )

            print(
                f"Reserva confirmada: "
                f"{self.servicio.descripcion()}"
            )

        except Exception as e:

            registrar_log(
                f"Error al confirmar reserva: {e}"
            )

            print(f"Error: {e}")

    # CANCELAR RESERVA

    def cancelar(self):

        try:

            if self.estado == "Cancelada":

                raise ReservaError(
                    "La reserva ya está cancelada"
                )

            self.estado = "Cancelada"

            registrar_log(
                f"Reserva cancelada para "
                f"{self.cliente.nombre}"
            )

            print("Reserva cancelada correctamente")

        except Exception as e:

            registrar_log(
                f"Error al cancelar reserva: {e}"
            )

            print(f"Error: {e}")

        finally:

            print("Proceso de cancelación finalizado")

    # MOSTRAR INFORMACIÓN

    def mostrar_reserva(self):

        print("\n===== INFORMACIÓN RESERVA =====")

        print(f"Cliente: {self.cliente.nombre}")

        print(
            f"Servicio: "
            f"{self.servicio.descripcion()}"
        )

        print(f"Duración: {self.duracion}")

        print(f"Estado: {self.estado}")

        print(
            f"Costo total: "
            f"{self.servicio.calcular_costo()}"
        )
