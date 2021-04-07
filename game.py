import random
import numpy as np
from card_classes import *


ROWS = 4
COLS = 6


class Player:
    def __init__(self):
        self.totems = [[], [], [], [], [], []]
        self.points = 0
        self.num = self


class Game:

    def __init__(self, id):
        self.p1 = Player()
        self.p2 = Player()
        self.id = id
        self.p = [self.p1, self.p2]
        self.deck = self.deck_first_deal()
        self.draft = self.first_draft()
        self.current_player = 1
        self.ready = False

    def play(self, player, move):
        self.current_player = 2 - player
        sel, x, y = move.split(",")
        x = int(x)
        sel = int(sel)
        self.evaluate_move(player, sel, x)
        if sel < 5:
            self.p[int(player)].totems[x].append(self.draft.pop(sel))
            self.draft.append(self.deck.pop(0))
        else:
            self.p[int(player)].totems[x].append(self.deck.pop())

    def evaluate_move(self, player, sel, x):
        if sel < 5:
            card = self.draft[sel]
        else:
            card = self.deck.pop()
        p_totems = self.p[int(player)].totems

        if card.type == 'instant':
            instant_points = card.get_instant_points(p_totems, sel, x)
            points = instant_points
            self.p[int(player)].points += points
            print(player, self.p[int(player)].points)

    def evaluate_final(self, player, sel, x):

        pass

    def reset(self):
        self.p1 = Player()
        self.p2 = Player()
        self.id = id
        self.p = [self.p1, self.p2]
        self.deck = self.deck_first_deal()
        self.draft = self.first_draft()
        self.current_player = 1
        self.ready = False

    def deck_first_deal(self):
        draft_deck = []
        print('first')
        a = np.array(
            [EagleCard(), CraneCard(), OwlCard(), HummingbirdCard(), MagpieCard(), BearCard(), WolfCard(), FoxCard(),
             LynxCard(), MouseCard(), SnakeCard(), ChameleonCard(), CrocodileCard(), LizardCard(), GecoCard(),
             SharkCard(), CrabCard(), OctopusCard(), FishCard(), JellyfishCard()])  # Všechny typy karet

        s = np.array([4] * 20)  # kolik má odpovídající typ mít počet v arrayi

        deck = np.repeat(a, s)

        random.shuffle(deck)
        main_deck = deck.tolist()

        for x in range(16 * len(self.p)):
            draft_deck.append(main_deck.pop(0))

        return draft_deck

    def first_draft(self):
        """appenduje prvních pět karet do draftu"""

        draft_row = []
        for x in range(5):
            draft_row.append(self.deck.pop(0))

        return draft_row


"""
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
"""

