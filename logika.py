import random
import numpy as np
import pygame
from card_classes import *

pygame.font.init()


###CONSTANTS###
###END OF CONSTANTS###


###GUI FUNCTIONS###
class State:
    """stará se o vykreslení základní desky a možných míst kam """

    def __init__(self):
        P1 = Player()
        P2 = Player()
        self.players = [P1, P2]
        self.current_player = random.randint(0, 1)
        self.deck = deck_first_deal(self.players)
        self.draft = first_draft(self.deck)

    def get_valid_placements(totems):
        pass

    def move_card(self):
        pass


###END OF GUI FUNCTIONS###

###PLAYER CLASS###
class Player:
    def __init__(self):
        self.totems = []
        self.points = []


###END OF PLAYER CLASSES###

###DECK FUNCTIONS###
def deck_first_deal(players):
    draft_deck = []

    a = np.array(
        [EagleCard(), CraneCard(), OwlCard(), HummingbirdCard(), MagpieCard(), BearCard(), WolfCard(), FoxCard(),
         LynxCard(), MouseCard(), SnakeCard(), ChameleonCard(), CrocodileCard(), LizardCard(), GecoCard(), SharkCard(),
         CrabCard(), OctopusCard(), FishCard(), JellyfishCard()])  # Všechny typy karet

    s = np.array([4] * 20)  # kolik má odpovídající typ mít počet v arrayi

    deck = np.repeat(a, s)

    random.shuffle(deck)
    main_deck = deck.tolist()

    for x in range(16 * len(players)):
        draft_deck.append(main_deck.pop(0))
    return draft_deck


def first_draft(deck):
    draft_row = []
    for x in range(5):
        draft_row.append(deck.pop(0))

    return draft_row


def renew_draft_card(deck):
    """dá kartu z balíčku do draft row, pokud ji hráč sebere"""
    pass


###END OF DECK FUNCTIONS###

###GAME FUNCTIONS###
def is_game_end(draft, deck):
    if len(draft) == 0 & len(deck) == 0:
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
