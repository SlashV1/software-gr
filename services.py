from abc import ABC, abstractmethod
from entities import EntidadBase
# Usamos el nombre en español para que coincida con tu archivo
from excepciones import DatosInvalidadosError, ReservaInvalidaError

class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre, costo_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.costo_base = costo_base

    # Implementación obligatoria para evitar el TypeError
    def obtener_detalles(self):
        return f"Servicio: {self.nombre} (ID: {self._id_entidad})"

    @abstractmethod
    def calcular_costo(self, cantidad=1, **kwargs):
        pass

class ReservasSalas(Servicio):
    def obtener_detalles(self):
        return f"Sala: {self.nombre} - Tarifa: {self.costo_base}"

    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            if cantidad <= 0:
                raise DatosInvalidadosError("La cantidad de horas debe ser mayor a cero.")
            return (self.costo_base * cantidad) - descuento
        except DatosInvalidadosError as e:
            print(f"⚠️ Error en ReservasSalas: {e}")
            return 0

class AlquilerEquipos(Servicio):
    def obtener_detalles(self):
        return f"Equipo: {self.nombre} - Tarifa: {self.costo_base}"

    def calcular_costo(self, cantidad=1, seguro=True):
        try:
            if cantidad <= 0:
                raise DatosInvalidadosError("Debe alquilar al menos un equipo.")
            adicional = 15.0 if seguro else 0.0
            return (self.costo_base * cantidad) + adicional
        except DatosInvalidadosError as e:
            print(f"⚠️ Error en AlquilerEquipos: {e}")
            return 0

class AsesoriaEspecializada(Servicio):
    def obtener_detalles(self):
        return f"Asesoría: {self.nombre} - Tarifa: {self.costo_base}"

    def calcular_costo(self, cantidad=1, es_urgente=False):
        try:
            if cantidad <= 0:
                raise DatosInvalidadosError("La duración debe ser positiva.")
            factor = 1.5 if es_urgente else 1.0
            return (self.costo_base * cantidad) * factor
        except DatosInvalidadosError as e:
            print(f"⚠️ Error en AsesoriaEspecializada: {e}")
            return 0