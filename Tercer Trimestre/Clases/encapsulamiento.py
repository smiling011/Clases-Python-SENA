#atributos y metodos
    # los tres principales son:
    # publicos: no tiene simbolo q lo identifique
    # protegidos: simbolo que lo identifique _
    # privados: simbolo que lo identifiquen __
"""
publicos y atributos esta visibles esta visible en cualquier momento del codigo.
----------------------------------------------------------------------------------------
protegido solo se puede acceder a usu  metodos y atribngutos dentro de la clase y subclases.
        padre y sus hijos
        
privado solo es de uso de su propia clase
"""
#endregion
#region: ejemplo de protegido atributo
class Persona():
    def__init__(self, nombre, apellido):
        self._nombre=nombre
        self._apellido=apellido
        endregion