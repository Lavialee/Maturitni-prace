import random
import numpy as np
from card_classes import *

ROWS = 4
COLS = 6


class Player:
    def __init__(self):
        self.totems = [[], [], [], [], [], []]
        self.points = []


def is_game_end(draft, deck):
    if len(draft) == 0 & len(deck) == 0:
        return True
    else:
        return False


class State:
    """stará se o vykreslení základní desky a možných míst kam """

    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.selected_draft = None
        self.selected_board = None
        self.hovered = None
        self.players = [self.p1, self.p2]
        self.current_player = random.choice(self.players)
        self.deck = self.deck_first_deal()
        self.draft = self.first_draft()
        self.button_pressed = False

    def get_valid_placements(self):
        """zjistí souřadnice, kam je možné dát do totemu karty"""

        possible_placements = []
        for col in range(COLS):
            if len(self.current_player.totems[col]) < 4:
                row = 3 - (len(self.current_player.totems[col]))
                possible_placements.append([col, row])
            else:
                pass

        return possible_placements

    def deck_first_deal(self):
        draft_deck = []

        a = np.array(
            [EagleCard(), CraneCard(), OwlCard(), HummingbirdCard(), MagpieCard(), BearCard(), WolfCard(), FoxCard(),
             LynxCard(), MouseCard(), SnakeCard(), ChameleonCard(), CrocodileCard(), LizardCard(), GecoCard(),
             SharkCard(), CrabCard(), OctopusCard(), FishCard(), JellyfishCard()])  # Všechny typy karet

        s = np.array([4] * 20)  # kolik má odpovídající typ mít počet v arrayi

        deck = np.repeat(a, s)

        random.shuffle(deck)
        main_deck = deck.tolist()

        for x in range(16 * len(self.players)):
            draft_deck.append(main_deck.pop(0))

        return draft_deck

    def first_draft(self):
        """appenduje prvních pět karet do draftu"""

        draft_row = []
        for x in range(5):
            draft_row.append(self.deck.pop(0))

        return draft_row

    def renew_draft_card(self, draft_row):
        """dá kartu z balíčku do draft row, pokud ji hráč sebere"""

        draft_row.append(self.deck.pop(0))

        return draft_row


"""while is_game_end() is False:
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

 while is_game_end == False:###zjistit jak dát aby to dělala pro aktuálního hráče???
            card = draft[ draft_pos ]
            totem_pos = get_user_action_totem_pick()
            player[ current_player ][ totem_no ].append (card)
            draft[ draft_pos ] = deck.pop()      
        ###CARD CLASSES###    """
