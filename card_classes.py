# CARD CLASSES #
# AIR #
class EagleCard:
    """Eagle (air, instant) - gain one point instantly, plus 2 points for each totem block under it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Eagle"

    def get_instant_points(self):
        pass


class CraneCard:
    """Crane (air, EoG) - gain one point, and additional 2 points for every crane in a diagonal from it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'EoG'

    def __repr__(self):
        return "Crane"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class OwlCard:
    """Owl (air, passive) - all instant cards placed in it's totem after, give aditional 3 points"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'passive'

    def __repr__(self):
        return "Owl"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class HummingbirdCard:
    """Hummingbird (air, passive) - if there's less than three totem blocks in it's totem, EoG effects are double"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'passive'

    def __repr__(self):
        return "Hummingbird"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class MagpieCard:
    """Magpie (air, instant) - get 1 point, and 1 additional point for all air types on your board"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Magpie"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# EARTH #
class BearCard:
    """Bear (earth, passive) - if his totem has more than 2 blocks, instant effects get a 1,5 multiplyer"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'passive'

    def __repr__(self):
        return "Bear"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class WolfCard:
    """Vlk (earth, instant) -  get points: amount of wolves on board x2"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'instant'

    def __repr__(self):
        return "Wolf"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class FoxCard:
    """Liška (earth, EoG) - if it's in your totem at least twice +4 points (for each), otherwise -3"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Fox"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class LynxCard:
    """Lynx (earth, EoG) - get half a point for any mice, fish, foxes and magpies in a one block radius of it"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Lynx"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class MouseCard:
    """Mouse (earth, EoG) - one point, +1 point for any mice in a one block radius of it"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Mouse"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# FIRE #
class SnakeCard:
    """Snake (fire, instant) - two points, additional one point for any mice in its totem"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Snake"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class ChameleonCard:
    """Chameleon (fire, instant) - one point, is counted as an appropriate animal in further instant effects"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Chameleon"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class CrocodileCard:
    """Crocodile (fire, instant) - one point, add one point for every water animal in its row"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Crocodile"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class LizardCard:
    """Lizard (fire, instant) - one point, plus one point for any other lizards in its totem or row"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Lizard"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class GecoCard:
    """Geco (fire, EoG) - one point for every represented element in its totem, six if all are represented"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'EoG'

    def __repr__(self):
        return "Geco"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# WATER #
class SharkCard:
    """Shark (water, EoG) - one point, plus one point for every totem block under it"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'EoG'

    def __repr__(self):
        return "Shark"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class CrabCard:
    """Crab (water, EoG) - one point, additional 2 points for any crab in the same row"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'EoG'

    def __repr__(self):
        return "Crab"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class OctopusCard:
    """Octopus (water, EoG) -  copies an EoG card from its totem which yields the most points"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'EoG'

    def __repr__(self):
        return "Octopus"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class FishCard:
    """Fish (water, instant) - five points, but two deducted for any other element in this totem"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'instant'

    def __repr__(self):
        return "Fish"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class JellyfishCard:
    """Jellyfish (water, instant) - one point, plus one point for every totem block above it"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'instant'

    def __repr__(self):
        return "Jellyfish"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass
# END OF CARD CLASSES #
