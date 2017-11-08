class Gun:
    def __init__(self, cartridge_size):
        self.__isLock = False
        self.__cartridge_size = cartridge_size
        self.__ammunition = 0

    def lock(self):
        self.__isLock = True

    def unlock(self):
        self.__isLock = False

    @property
    def isLock(self):
        return self.__isLock

    def shoot(self):
        if self.__isLock:
            print("Gun is lock")
            return
        if self.__ammunition > 0:
            self.__ammunition -= 1
        else:
            print("Gun is empty")

    def reload(self, ammunition):
        if not isinstance(ammunition, int):
            return ammunition
        if ammunition <= 0:
            return
        ammunition_count = ammunition
        while self.__cartridge_size > self.__ammunition and ammunition_count > 0:
            self.__ammunition += 1
            ammunition_count -= 1
        return ammunition_count