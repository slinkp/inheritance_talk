class Animal(object):
    pass


class Shark(Animal):
    pass


class Weapon(object):
    pass


class LaserMixin(Weapon):
    pass


class SharkWithLasers(LaserMixin, Shark):
    pass


class Orca(Animal):
    pass


class NunchuckMixin(Weapon):
    pass


class OrcaWithNunchucks(NunchuckMixin, Orca):
    pass


class SharkWithNunchucks(NunchuckMixin, Shark):
    pass


class OrcaWithLasers(LaserMixin, Orca):
    pass


class ArmorMixin(object):
    pass


class ArmoredSharkWithLasers(ArmorMixin, SharkWithLasers):
    pass


class ArmoredSharkWithNunchucks(ArmorMixin, SharkWithNunchucks):
    pass


class ArmoredOrcaWithLasers(ArmorMixin, OrcaWithLasers):
    pass


class ArmoredOrcaWithNunchucks(ArmorMixin, OrcaWithNunchucks):
    pass
