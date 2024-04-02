from error import DimensionError

class Foto():
    #maximo de la foto (ancho y alto) px
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        #Valido que el ancho maximo no sobrepase el limite
        if ancho > Foto.MAX:
            #Levanto un error personalizado para este caso
            raise DimensionError("Ancho no permitido.", ancho, Foto.MAX)
        #Valido que el ancho no sea menor a 1
        elif ancho < 1:
            #Levanto un error personalizado para este caso
            raise DimensionError("Ancho debe ser mayor a 0.", ancho)
        else:
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > Foto.MAX:
            raise DimensionError("Alto no permitido.", alto, Foto.MAX)
        elif alto < 1:
            raise DimensionError("Alto debe ser mayor a 0.", alto)
        else:
            self.__alto = alto