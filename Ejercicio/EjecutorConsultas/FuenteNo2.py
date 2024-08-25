from Entidades.DatosConsulta import DatosConsulta
from FuenteBase import FuenteBase

"""Fuente de información número 2."""
class FuenteNo2(FuenteBase):
    
    """Implementación de la propuedad que define el número de la fuente."""
    @property
    def NumeroFuente(self):
        return 2

"""Inicializa la ejecución de la fuente, activando la escucha de notificaciones."""
if __name__ == '__main__':
    ObjFuente = FuenteNo2()
    print(F' [*] {ObjFuente.ObtenerNombreFuente()} iniciada, se espera entrada de consultas.')
    ObjFuente.EscucharNotificación()