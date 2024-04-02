#Clase de base para las excepciones
class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje:str, dimension:int, maximo:int):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        #Si solo se ingresa el mensaje, retornara el metodo de la clase padre
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            mensaje_retorno = self.mensaje
            if self.dimension:
                mensaje_retorno += f"Se ingreso la dimension: {self.dimension}."
            if self.maximo:
                mensaje_retorno += f"Se agrego el maximo: {self.maximo}"
            return mensaje_retorno      