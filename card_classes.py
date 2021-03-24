###CARD CLASSES###
###AIR###
class EagleCard:
    """Orel (instant) - jeden bod instantní, plus 2 body za každý blok pod tímto"""
    def __repr__(self):
        return "Eagle"

    def getInstantPoints(self):
        pass
class CraneCard:
    """Jeřáb (EoG) - jeden bod plus dva body za jeřáby diagonálně"""
    def __repr__(self):
        return "Crane"
    
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class OwlCard:
    """Sova (passive) - všechny karty s instant efektem dávají +2 body"""
    def __repr__(self):
        return "Owl"

    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class HummingbirdCard:
    """Kolibřík (passive) - je-li v jeho totemu <= než 4 bloky, EoG efekty jsou dvojnásobné"""
    def __repr__(self):
        return "Hummingbird"    
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class MagpieCard:
    """Straka (instant) - můžeš prohodit tenhle a jiný totem, dostaneš + 1 bod za každé 2 bloky (zaokrouhleno dolů)"""
    def __repr__(self):
        return "Magpie"

    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
###EARTH###
class BearCard:
    """Medvěd (passive) - je-li v totemu >=4, instant efekty jsou o 1,5 rounded down"""
    def __repr__(self):
        return "Bear"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class WolfCard:
    """Vlk (instant) -  +2 body za každého vlka"""
    def __repr__(self):
        return "Wolf"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class FoxCard:
    """Liška (EoG) - pokud je v totemu alespoň dvakrát +4 body, jinak -3"""
    def __repr__(self):
        return "Fox"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class LynxCard:
    """Rys (Instant) - za prvního u hráče 6b, za každého dalšího -2 body"""
    def __repr__(self):
        return "Lynx"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class MouseCard:
    """Myš (EoG) - jeden bod, pokud je v okolí další myš +1 bod za každou"""
    def __repr__(self):
        return "Mouse"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
###FIRE###
class SnakeCard:
    """Had (instant) - dva body, může se dát kamkoliv do totemu"""
    def __repr__(self):
        return "Snake"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class ChameleonCard:
    """Chameleon (instant) - jeden bod, zároveň jako "žolík", může nahradit jakékoliv zvíře """
    def __repr__(self):
        return "Chameleon"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class CrocodileCard:
    """Krokodýl (instant) - jeden bod, +1 bod za každé další vodní zvíře v totemu """
    def __repr__(self):
        return "Crocodile"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class LizardCard:
    """Ještěrka (instant) - jeden bod, +1 bod za každé další ještěrky ve stejném řádku a sloupci"""
    def __repr__(self):
        return "Lizard"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class GecoCard:
    """Gekon (EoG) - jeden bod za každý živel v totemu (max tedy 4 body)"""
    def __repr__(self):
        return "Geco"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
###WATER###
class SharkCard:
    """Žralok (EoG) - jeden bod, +1 bod za každý blok nad tímto"""
    def __repr__(self):
        return "Shark"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass        
class CrabCard:
    """Krab () -  jeden bod, +2 body za kraby ve stejném řádku """
    def __repr__(self):
        return "Crab"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class OctopusCard:
    """Chobotnice (EoG) - zkopíruj jakýkoliv EoG efekt z jiného bloku totemu"""
    def __repr__(self):
        return "Octopus"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class FishCard:
    """Ryba (instant) - 5 bodů, ale -2 za každý jiný živel v totemu"""
    def __repr__(self):
        return "Fish"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class JellyfishCard:
    """Medúza (instant) - prohoď 2 bloky, jsou-li stejný živel +2 body"""
    def __repr__(self):
        return "Jellyfish"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
###END OF CARD CLASSES###