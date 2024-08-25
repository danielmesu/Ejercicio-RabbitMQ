from Entidades.DatosConsulta import DatosConsulta
from FuenteBase import FuenteBase

"""Fuente de información número 1."""
class FuenteNo1(FuenteBase):
    
    """Implementación de la propuedad que define el número de la fuente."""
    @property
    def NumeroFuente(self):
        return 1

"""Inicializa la ejecución de la fuente, activando la escucha de notificaciones."""
if __name__ == '__main__':
    ObjFuente = FuenteNo1()
    print(F' [*] {ObjFuente.ObtenerNombreFuente()} iniciada, se espera entrada de consultas.')
    ObjFuente.EscucharNotificación()