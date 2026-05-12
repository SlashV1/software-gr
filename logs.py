from datetime import datetime
def registrar_log(mensaje):
   try:
     with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:
          fecha = datetime.now()
          archivo.write(
                f"{fecha} - {mensaje}\n"
            )
except Exception as e:

        print(
            f"Error al escribir en el log: {e}"
        )

def log_evento(evento):

    registrar_log(
        f"EVENTO: {evento}"
    )
  
  def log_error(error):

    registrar_log(
        f"ERROR: {error}"
    )
    def log_reserva(cliente, servicio):

    registrar_log(
        f"RESERVA -> Cliente: {cliente} | "
        f"Servicio: {servicio}"
    )
