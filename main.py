class Gun:
    def __init__(self, cartridge_size):
        self.__is_lock = False
        self.__cartridge_size = cartridge_size
        self.__ammunition = 0

    def lock(self):
        self.__is_lock = True

    def unlock(self):
        self.__is_lock = False

    @property
    def is_lock(self):
        return self.__is_lock

    def shoot(self):
        if self.__is_lock:
            return
        if self.__ammunition > 0:
            self.__ammunition -= 1
        else:
            return

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


