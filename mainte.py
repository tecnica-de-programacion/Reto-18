class Gun:
    #  This is a representation for a gun's class

    def __init__(self, safe, sizeLoader):
        self.__safe = safe
        self.__size_Loader = sizeLoader
        self.__shelter = sizeLoader

    def safe_Gun(self):
        if self.__safe:
            self.__safe = False
        else:
            self.__safe = True
        return self.__safe

    def shoot(self):
        if self.__safe:
            if self.__size_loader > 0:
                self.__size_loader -= 1
                return "BUM!"
            else:
                return "No hay balas"
        else:
            return "Esta el seguro de la pistola"

    def loader(self):
        if self.__safe == False:
            if self.__size_loader < self.__shelter:
                self.__size_loader += 1
                return self.__size_loader
            else:
                return "No se pueden meter más balas"
        else:
            return "Por su seguridad ponga el seguro"

person = Gun(False,10)
print(person.shoot())