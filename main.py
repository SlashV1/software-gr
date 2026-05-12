from entities import Cliente, Reserva
from services import ReservasSalas, AlquilerEquipos, AsesoriaEspecializada
from excepciones import SoftwareFJError, ServicioNoDisponibleError, DatosInvalidadosError
import logging

def ejecutar_simulacion():
    clientes = []
    servicios = {
        "S1": ReservasSalas("S1", "Sala Creativa", 50.0),
        "S2": AlquilerEquipos("S2", "Laptop Gamer", 40.0),
        "S3": AsesoriaEspecializada("S3", "Consultoría Software", 100.0)
    }

    print("\n" + "="*40)
    print("=== SOFTWARE FJ: SIMULACIÓN FASE 4 ===")
    print("="*40 + "\n")

    operaciones = [
        ("REG_CLIENTE", "C1", "Ana Garcia", "ana@mail.com"),
        ("REG_CLIENTE", "C2", "", "error_sin_nombre"),
        ("RESERVA", "R1", "C1", "S1", 3),
        ("RESERVA", "R2", "C1", "S1", -2),
        ("REG_CLIENTE", "C3", "Pedro Picapiedra", "p@mail.com"),
        ("RESERVA", "R3", "C3", "S99", 2),
        ("RESERVA", "R4", "C3", "S3", 1),
        ("REG_CLIENTE", "C4", "Luis Perez", "luis@mail.com"),
        ("RESERVA", "R5", "C4", "S2", 2),
        ("RESERVA", "R6", "C1", "S1", 0)
    ]

    for i, op in enumerate(operaciones, 1):
        print(f"OPERACIÓN #{i} ({op[0]}):")
        try:
            if op[0] == "REG_CLIENTE":
                nuevo_cli = Cliente(op[1], op[2], op[3])
                clientes.append(nuevo_cli)
                print(f"   ✅ Cliente {op[2]} registrado.")
            elif op[0] == "RESERVA":
                cli_obj = next((c for c in clientes if c._id_entidad == op[2]), None)
                if not cli_obj: raise DatosInvalidadosError(f"ID {op[2]} no existe.")
                ser_obj = servicios.get(op[3])
                if not ser_obj: raise ServicioNoDisponibleError(f"Servicio {op[3]} no existe.")
                res = Reserva(op[1], cli_obj, ser_obj, op[4])
                res.confirmar()
                print(f"   ✅ Reserva {op[1]} exitosa.")
        except (SoftwareFJError, Exception) as e:
            print(f"   ❌ ERROR: {e}")
        print("-" * 40)

if __name__ == "__main__":
    ejecutar_simulacion()