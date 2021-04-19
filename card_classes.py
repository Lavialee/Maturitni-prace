# CARD CLASSES #
# AIR #
class EagleCard:
    """Eagle (air, instant) - gain one point instantly, plus two points for each totem block under it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Eagle"

    def get_instant_points(self, p_totems, x, y):
        points = 1 + (2 * len(p_totems[x]))
        return points


class CraneCard:
    """Crane (air, EoG) - gain one point, and additional two points for every crane in a diagonal from it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'EoG'

    def __repr__(self):
        return "Crane"

    def get_eog_points(self):
        pass


class OwlCard:
    """Owl (air, instant) - one point, aditional 2 points for every mouse, snake or lizard in this totem"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Owl"

    def get_instant_points(self, p_totems, x, y):
        prey_bonus = 0
        for prey in range(len(p_totems[x])):
            if isinstance(p_totems[x][prey], (MouseCard, SnakeCard, LizardCard, ChameleonCard)):
                prey_bonus += 2
        points = 1 + prey_bonus
        return points


class HummingbirdCard:
    """Hummingbird (air, instant) - 4 points if placed second in a totem, otherwise just one"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Hummingbird"

    def get_instant_points(self, p_totems, x, y):
        if len(p_totems[x]) == 1:
            points = 4
        else:
            points = 1
        return points


class MagpieCard:
    """Magpie (air, instant) - get one point, and one additional point for all air types on your board"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Magpie"

    def get_instant_points(self, p_totems, x, y):
        air_bonus = 0
        for col in range(len(p_totems)):
            for row in range(len(p_totems[col])):
                try:
                    if p_totems[col][row].element == 'Air' or isinstance(p_totems[col][row], ChameleonCard):
                        air_bonus += 1
                except IndexError:
                    pass

        points = 1 + air_bonus
        return points

    def get_eog_points(self):
        pass


# EARTH #
class BearCard:
    """Bear (earth, EoG) - if its alone in its totem at the end, get 5 points, otherwise two points"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Bear"

    def get_eog_points(self):
        pass


class WolfCard:
    """Vlk (earth, instant) -  get points: amount of wolves on board x2"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'instant'

    def __repr__(self):
        return "Wolf"

    def get_instant_points(self, p_totems, x, y):
        pack = 0

        for col in range(len(p_totems)):
            for row in range(len(p_totems[col])):
                try:
                    if isinstance(p_totems[col][row], (WolfCard, ChameleonCard)):
                        pack += 1
                except IndexError:
                    pass
        pack_bonus = 2 * pack
        points = 2 + pack_bonus
        return points

    def get_eog_points(self):
        pass


class FoxCard:
    """Liška (earth, EoG) - if it's in your totem at least twice +4 points (for each), otherwise -3"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Fox"

    def get_eog_points(self):
        pass


class LynxCard:
    """Lynx (earth, EoG) - get half a point for any mice, fish, foxes and magpies in a one block radius of it"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Lynx"

    def get_eog_points(self):
        pass


class MouseCard:
    """Mouse (earth, EoG) - one point, plus one point for any mice in a one block radius of it"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Mouse"

    def get_eog_points(self):
        pass


# FIRE #
class SnakeCard:
    """Snake (fire, instant) - one point, additional three points for any mice in its totem"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Snake"

    def get_instant_points(self, p_totems, x, y):
        prey_bonus = 0
        for prey in range(len(p_totems[x])):
            if isinstance(p_totems[x][prey], (MouseCard, ChameleonCard)):
                prey_bonus += 3
        points = 1 + prey_bonus
        return points


class ChameleonCard:
    """Chameleon (fire, instant) - one point, is counted as an appropriate animal in further instant effects"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Chameleon"

    def get_instant_points(self, p_totems, x, y):
        points = 1
        return points

    def get_eog_points(self):
        pass


class CrocodileCard:
    """Crocodile (fire, instant) - one point, add two points for every water animal in its row"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Crocodile"

    def get_instant_points(self, p_totems, x, y):
        water_bonus = 0
        for water in range(len(p_totems)):
            try:
                if p_totems[water][y].element == 'Water':
                    water_bonus += 2

            except IndexError:
                pass

        points = 1 + water_bonus
        return points

    def get_eog_points(self):
        pass


class LizardCard:
    """Lizard (fire, instant) - one point, plus one point for any other lizards in its totem or row"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Lizard"

    def get_instant_points(self, p_totems, x, y):
        lizard_bonus = 0
        for col in range(len(p_totems)):
            try:
                if isinstance(p_totems[col][x], (LizardCard, ChameleonCard)):
                    lizard_bonus += 1
            except IndexError:
                pass

        for row in range(len(p_totems)):
            try:
                if isinstance(p_totems[x][row], (LizardCard, ChameleonCard)):
                    lizard_bonus += 1
            except IndexError:
                pass
        points = 1 + lizard_bonus
        return points

    def get_eog_points(self):
        pass


class GecoCard:
    """Geco (fire, EoG) - one point for every represented element in its totem, six if all are represented"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'EoG'

    def __repr__(self):
        return "Geco"

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

    def get_eog_points(self):
        pass


class CrabCard:
    """Crab (water, EoG) - one point, additional 2 points for any crab in the same row"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'EoG'

    def __repr__(self):
        return "Crab"

    def get_eog_points(self):
        pass


class OctopusCard:
    """Octopus (water, EoG) -  copies an EoG card from its totem which yields the most points"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'EoG'

    def __repr__(self):
        return "Octopus"

    def get_eog_points(self):
        pass


class FishCard:
    """Fish (water, instant) - five points, but two deducted for any other element in this totem"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'instant'

    def __repr__(self):
        return "Fish"

    def get_instant_points(self, p_totems, x, y):
        element_penalty = 0
        for y in range(len(p_totems[x])):
            if p_totems[x][y].element != 'Water' or isinstance(p_totems[x][y], ChameleonCard):
                element_penalty += 2
        points = 5 - element_penalty
        return points

    def get_eog_points(self):
        pass


class JellyfishCard:
    """Jellyfish (water, instant) - one point, plus one point for every empty space above it"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'instant'

    def __repr__(self):
        return "Jellyfish"

    def get_instant_points(self, p_totems, x, y):
        space_bonus = 3 - len((p_totems[x]))
        points = 1 + space_bonus
        return points

    def get_eog_points(self):
        pass
# END OF CARD CLASSES #
