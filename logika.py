import random
import numpy as np

###CARD CLASSES###

###AIR###
class EagleCard:
    """Orel(instant) - jeden bod instantní, plus 2 body za každý blok pod tímto"""
    def __repr__(self):
        return "Eagle"

    def getInstantPoints(self):
        pass
class CraneCard:
    """Jeřáb(EoG) - jeden bod plus dva body za jeřáby diagonálně"""
    def __repr__(self):
        return "Crane"
    
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class OwlCard:
    """Sova(passive) - všechny karty s instant efektem dávají +2 body"""
    def __repr__(self):
        return "Owl"

    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class HummingbirdCard:
    """Kolibřík(passive) - je-li v jeho totemu <= než 4 bloky, EoG efekty jsou dvojnásobné"""
    def __repr__(self):
        return "Hummingbird"    
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class XYZCard:
    """Nějaky zvire(instant) - můžeš prohodit tenhle a jiný totem, dostaneš + 1 bod za každé 2 bloky (zaokrouhleno dolů)"""
    def __repr__(self):
        return "XYZ"

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
    """Vlk(instant) -  +2 body za každého vlka"""
    def __repr__(self):
        return "Wolf"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class FoxCard:
    """"""
    def __repr__(self):
        return "Fox"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class LynxCard:
    """"""
    def __repr__(self):
        return "Lynx"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class MouseCard:
    """"""
    def __repr__(self):
        return "Mouse"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass

###FIRE###
class SnakeCard:
    def __repr__(self):
        return "Snake"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class ChameleonCard:
    def __repr__(self):
        return "Chameleon"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class CrocodileCard:
    def __repr__(self):
        return "Crocodile"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class LizardCard:
    def __repr__(self):
        return "Lizard"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class GecoCard:
    def __repr__(self):
        return "Geco"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass

###WATER###
class SharkCard:
    def __repr__(self):
        return "Shark"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass        
class CrabCard:
    def __repr__(self):
        return "Crab"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class OctopusCard:
    def __repr__(self):
        return "Octopus"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class FishCard:
    def __repr__(self):
        return "Fish"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
class ZYXCard:
    def __repr__(self):
        return "ZYX"
    def getInstantPoints(self):
        pass

    def getEndOfGamePoints(self):
        pass
###END OF CARD CLASSES###

###PLAYER CLASS###
class Player:
    def __init__(self):
        self.deck = []
        self.totems = []
        self.points = []
###END OF PLAYER CLASSES###


###MAIN GAME###

###DECK CREATION###

a = np.array([EagleCard(),CraneCard(), OwlCard(), HummingbirdCard(), XYZCard(), BearCard(), WolfCard(), FoxCard(), LynxCard(), MouseCard(),
    SnakeCard(), ChameleonCard(), CrocodileCard(), LizardCard(), GecoCard(), SharkCard(), CrabCard(), OctopusCard(), FishCard(), ZYXCard()]) #Všechny typy karet

s = np.array([4] * 20) #kolik má odpovídající typ mít počet v arrayi

deck = np.repeat(a, s)

random.shuffle(deck)

main_deck = deck.tolist()

###DECK CREATION END###

###DECK DEALING###
draft_row = []
P1 = Player()
P2 = Player()
players = [ P1, P2 ]

print ('Main deck:', main_deck, '\n')

for x in range(16):
    P1.deck.append (main_deck.pop(0))
    P2.deck.append (main_deck.pop(0))    
for x in range(5):
    draft_row.append (main_deck.pop(0))

print('Current player:', current_player, '\n')
print('P1 deck:', P1.deck, '\n')
print('P2 deck:', P2.deck, '\n')
print('Draft row:', draft_row, '\n')
print('Main deck:', main_deck, '\n')
###DECK DEALING END###

###GAME START###
current_player = random.randint(0, 1)


"""
while is_game_end() is False:
    user_action = get_user_action()

    card = None
    if user_action == DRAFT:
        draft_pos = get_user_action_draft_pos()
        card = draft[ draft_pos ]
        draft[ draft_pos ] = deck.pop()
        totem_no = get_user_action_totem_number()
        player[ current_player ][ totems ][ totem_no ].append( card )
    if user_action == USER_DECK:
        card = player[ current_player ][ deck ].pop()
        totem_no = get_user_action_totem_number()
        player[ current_player ][ totems ][ totem_no ].append( card )
    
    if has_instant_effect( card ):
        players[ current_player ][ instantPoints ] += solve_instant_effect( card )

    current_player = not current_player

player1Points = get_totem_points( player[ 0 ][ totems ] ) + player[ 0 ][ instantPoints ]
player2Points = get_totem_points( player[ 1 ][ totems ] ) + player[ 1 ][ instantPoints ]


if player1Points > player2Points:
    print( "Vyhrál hráč 1." );
elif player2Points > player1Points:
    print( "Vyhrál hráč 2.");
else:
    print( "Remíza." ); """