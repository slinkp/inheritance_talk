class Shark(object):
    pass

class LaserMixin(object):
    pass


class SharkWithLasers(Shark, LaserMixin):
    pass

class Orca(object):
    pass


class NunchuckMixin(object):
    pass

class OrcaWithNunchucks(Orca, NunchuckMixin):
    pass

class SharkWithNunchucks(Shark, NunchuckMixin):
    pass

class OrcaWithLasers(Orca, LaserMixin):
    pass

