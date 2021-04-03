# CARD CLASSES #
# AIR #
class EagleCard:
    """Orel (instant) - jeden bod instantní, plus 2 body za každý blok pod tímto"""

    def __repr__(self):
        return "Eagle"

    def get_instant_points(self):
        pass


class CraneCard:
    """Jeřáb (EoG) - jeden bod plus dva body za jeřáby diagonálně"""

    def __repr__(self):
        return "Crane"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class OwlCard:
    """Sova (passive) - všechny karty s instant efektem dávají +2 body"""

    def __repr__(self):
        return "Owl"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class HummingbirdCard:
    """Kolibřík (passive) - je-li v jeho totemu <= než 2 bloky, EoG efekty jsou dvojnásobné"""

    def __repr__(self):
        return "Hummingbird"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class MagpieCard:
    """Straka (instant) - můžeš prohodit tenhle a jiný totem, dostaneš + 1 bod za každé 2 bloky (zaokrouhleno dolů)"""

    def __repr__(self):
        return "Magpie"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# EARTH #
class BearCard:
    """Medvěd (passive) - je-li v totemu >=2, instant efekty jsou o 1,5 rounded down"""

    def __repr__(self):
        return "Bear"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class WolfCard:
    """Vlk (instant) -  +2 body za každého vlka"""

    def __repr__(self):
        return "Wolf"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class FoxCard:
    """Liška (EoG) - pokud je v totemu alespoň dvakrát +4 body, jinak -3"""

    def __repr__(self):
        return "Fox"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class LynxCard:
    """Rys (Instant) - za prvního u hráče 6b, za každého dalšího -2 body"""

    def __repr__(self):
        return "Lynx"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class MouseCard:
    """Myš (EoG) - jeden bod, pokud je v okolí další myš +1 bod za každou"""

    def __repr__(self):
        return "Mouse"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# FIRE #
class SnakeCard:
    """Had (instant) - dva body, může se dát kamkoliv do totemu"""

    def __repr__(self):
        return "Snake"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class ChameleonCard:
    """Chameleon (instant) - jeden bod, zároveň jako "žolík", může nahradit jakékoliv zvíře """

    def __repr__(self):
        return "Chameleon"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class CrocodileCard:
    """Krokodýl (instant) - jeden bod, +1 bod za vodní zvířata v totemu """

    def __repr__(self):
        return "Crocodile"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class LizardCard:
    """Ještěrka (instant) - jeden bod, +1 bod za každé další ještěrky ve stejném řádku a sloupci"""

    def __repr__(self):
        return "Lizard"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class GecoCard:
    """Gekon (EoG) - jeden bod za každý živel v totemu (max tedy 4 body)"""

    def __repr__(self):
        return "Geco"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


# WATER #
class SharkCard:
    """Žralok (EoG) - jeden bod, +1 bod za každý blok nad tímto"""

    def __repr__(self):
        return "Shark"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class CrabCard:
    """Krab () -  jeden bod, +2 body za kraby ve stejném řádku """

    def __repr__(self):
        return "Crab"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class OctopusCard:
    """Chobotnice (EoG) - zkopíruj jakýkoliv EoG efekt z jiného bloku totemu"""

    def __repr__(self):
        return "Octopus"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class FishCard:
    """Ryba (instant) - 5 bodů, ale -2 za každý jiný živel v totemu"""

    def __repr__(self):
        return "Fish"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass


class JellyfishCard:
    """Medúza (instant) - prohoď 2 bloky, jsou-li stejný živel +2 body"""

    def __repr__(self):
        return "Jellyfish"

    def get_instant_points(self):
        pass

    def get_eog_points(self):
        pass
# END OF CARD CLASSES #
