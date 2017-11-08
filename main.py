class Gun:
    def __init__(self, cartridge_size):
        self.__isLock = False
        self.__cartridge_size = cartridge_size
        self.__ammunition = 0



    def lock(self):
        self.__isLock = True
        return self.__isLock

    def unlock(self):
        self.__isLock = False

    @property
    def isLock(self):
        return self.__isLock


    @property
    def shoot(self):
        if self.__isLock:
            print("Gun is lock")
            return ("Gun is lock")

        if self.__ammunition > 0:
            self.__ammunition -= 1
            print('PUM')
        else:
            print("Gun is empty")
            return ("Gun is empty")

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


newGun = Gun(10)
print(newGun.isLock)
print(newGun.reload(7))
newGun.shoot
newGun.shoot
newGun.shoot
print('\n')
