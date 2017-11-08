class Gun:
    def __init__(self, gun_charger):
        self.bullet = 0
        self.number_of_bullet = gun_charger
        self.seguro = 0

    def charger(self, bulletscharged):
        if (bulletscharged + self.bullet) <= self.number_of_bullet:
            self.bullet += bulletscharged
            return 'cargada'
        else:
            self.bullet = self.number_of_bullet
            bullets_wasted = bulletscharged + self.bullet-self.number_of_bullet
            return bullets_wasted

    def quitar_seguro(self):
        self.seguro = 1

    def poner_seguro(self):
        self.seguro = 0

    def shoot(self):
        if self.bullet > 0 and self.seguro == 1:
            self.bullet -= 1
            return self.bullet
        else:
            return None