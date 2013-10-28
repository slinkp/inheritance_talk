class Animal(object):
    pass

class Shark(Animal):
    pass

class Weapon(object):
    pass

class LaserMixin(Weapon):
    pass


class SharkWithLasers(Shark, LaserMixin):
    pass

class Orca(Animal):
    pass


class NunchuckMixin(Weapon):
    pass

class OrcaWithNunchucks(Orca, NunchuckMixin):
    pass

class SharkWithNunchucks(Shark, NunchuckMixin):
    pass

class OrcaWithLasers(Orca, LaserMixin):
    pass

