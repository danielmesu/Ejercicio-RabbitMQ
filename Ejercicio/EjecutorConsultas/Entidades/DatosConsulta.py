import json

"""Clase que define los datos de una consulta."""
class DatosConsulta:

    """Inicializador de la clase."""
    def __init__(self, numero_documento: str, tipo_documento: int, pais_consulta: str):
        self.NumeroDocumento = numero_documento
        self.TipoDocumento = tipo_documento
        self.PaisConsulta = pais_consulta

    """Convierte un string tipo json en una instancia de este objeto."""
    @classmethod
    def ConvertirDesdeJson(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            numero_documento=data['NumeroDocumento'],
            tipo_documento=data['TipoDocumento'],
            pais_consulta=data['PaisConsulta']
        )
    
    """Retorna en formato json los valores de una instancia de este objeto."""
    def to_dict(self):
        return {
            'NumeroDocumento': self.NumeroDocumento,
            'TipoDocumento': self.TipoDocumento,
            'PaisConsulta': self.PaisConsulta
        }

    """Convierte en formato json la instancia de la clase."""
    def SerializarAJson(self):
        return json.dumps(self.to_dict(), indent=4)