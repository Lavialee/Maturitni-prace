import random
import numpy as np
import pygame
pygame.font.init()

###CONSTANTS###
width = 1280 
height = 960  
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
CARD_SIZE = 150
DRAFT_CARD_SIZE = 175
PADDING = 25
MARGINS = 40
ROWS = 4
COLS = 6
###END OF CONSTANTS###

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Totem")

###GUI FUNCTIONS###
class Cards:
    """stará se o vykreslování jednotlivých karet"""
    def __init__(self, col, row, card_type):
        self.col = col
        self.row = row
        self.x = 0
        self.y = 0
        self.card_type = card_type
        self.image_load(card_type)
        self.calculate_pos()
        self.selected_card = None

    def calculate_pos(self):
        self.x = (CARD_SIZE+PADDING) * self.col + 40
        self.y = (CARD_SIZE+PADDING) * self.row + 240
        image = self.image_load(self.card_type)
        window.blit(image, (self.x,self.y))

    def select_totem_placement(mx, my, rectangles):
        if rectangles.collidepoint(mx, my):
            col = (mx - 40) // COLS
            row = (my - 770 + ROWS*175) // ROWS

            print(col, row)

    def image_load(self, card_type):
        name = ('assets/'+ card_type + '.png')
        image = pygame.image.load(name)
        return image

class Board:
    """stará se o vykreslení základní desky a možných míst kam """
    def __init__(self):
        self.visible_draft = []
        self.placed_totems_P1 = [[]]
        self.placed_totems_P2 = [[]]

    def draw_card_base(self, window):
        window.fill(WHITE)
        for col in range(COLS):
            x = col*(CARD_SIZE+PADDING) + MARGINS
            for row in range(ROWS):
                y = row*(CARD_SIZE+PADDING) + 240
                rectangles = pygame.draw.rect(window, GREY, (x, y, CARD_SIZE, CARD_SIZE))
        
    def draw_draft_base(self, window, draft):
        for col in range(len(draft)+1):
            x = col*(DRAFT_CARD_SIZE+PADDING) + MARGINS
            y = 40
            rectangles = pygame.draw.rect(window, GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))

    def get_valid_placements(totems):
        pass


    def move_card(self):
        pass
###END OF GUI FUNCTIONS###

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

###PLAYER CLASS###
class Player:
    def __init__(self):
        self.totems = []
        self.points = []
###END OF PLAYER CLASSES###

###DECK FUNCTIONS###
def deck_first_deal(players):

    draft_deck = []
    
    a = np.array([EagleCard(),CraneCard(), OwlCard(), HummingbirdCard(), MagpieCard(), BearCard(), WolfCard(), FoxCard(), LynxCard(), MouseCard(),
        SnakeCard(), ChameleonCard(), CrocodileCard(), LizardCard(), GecoCard(), SharkCard(), CrabCard(), OctopusCard(), FishCard(), JellyfishCard()]) #Všechny typy karet

    s = np.array([4] * 20) #kolik má odpovídající typ mít počet v arrayi

    deck = np.repeat(a, s)

    random.shuffle(deck)
    main_deck = deck.tolist()

    for x in range(16*len(players)):
        draft_deck.append (main_deck.pop(0))
    return draft_deck
def first_draft(deck):
    draft_row = []
    for x in range(5):
        draft_row.append (deck.pop(0))
        
    return draft_row
def renew_draft_card(deck):
    """dá kartu z balíčku do draft row, pokud ji hráč sebere"""
    pass
###END OF DECK FUNCTIONS###

###GAME FUNCTIONS###
def is_game_end(draft, deck):

    if len(draft)==0 & len(deck)==0:
        return True
    else:
        return False
def get_user_action_card_pick():
    ###return column and row###
    pass

def solve_effect(card):
   pass
def has_instant_effect(card):
    pass
### END OF GAME FUNCTIONS###

###MAIN GAME###
def main():
    """main pygame loop"""
    run = True
    P1 = Player()
    P2 = Player()
    Players = [P1, P2]
    current_player = random.randint(0, 1) ###generuje náhodně prvního hráče
    clock = pygame.time.Clock()

    deck = deck_first_deal(Players)
    draft = first_draft(deck)
    board = Board()
    print(deck)
    zkouska = Cards(0,3, 'Fish')
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                draft_pos = get_user_action_card_pick()


        board.draw_card_base(window)
        board.draw_draft_base(window, draft)
        zkouska.calculate_pos()
        pygame.display.flip()

        while is_game_end == False:###zjistit jak dát aby to dělala pro aktuálního hráče???

            card = draft[ draft_pos ]
            totem_pos = get_user_action_totem_pick()
            player[ current_player ][ totem_no ].append (card)
            draft[ draft_pos ] = deck.pop()      
        ###CARD CLASSES###


main ()








###GAME START###
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
    print( "Remíza." );
"""