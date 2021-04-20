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
    """holds game data"""

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
        print(sel, x, y)
        x = int(x)
        y = 3 - int(y)
        sel = int(sel)
        self.evaluate_move(player, sel, x, y)
        if sel < 5:
            self.p[int(player)].totems[x].append(self.draft.pop(sel))
            self.draft.append(self.deck.pop(0))
        else:
            self.p[int(player)].totems[x].append(self.deck.pop())


    def connected(self):
        return self.ready

    def evaluate_move(self, player, sel, x, y):
        if sel < 5:
            card = self.draft[sel]
        else:
            card = self.deck.pop()
        p_totems = self.p[int(player)].totems

        if card.type == 'instant':
            instant_points = card.get_instant_points(p_totems, x, y)
            points = instant_points
            self.p[int(player)].points += points
            print('player:', player, "instant points:", self.p[int(player)].points)

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
        a = np.array(
            [EagleCard(), CraneCard(), OwlCard(), HummingbirdCard(), MagpieCard(), BearCard(), FoxCard(),
             LynxCard(), WolfCard(), MouseCard(), SnakeCard(), ChameleonCard(), CrocodileCard(), TortoiseCard(),
             GecoCard(), SharkCard(), CrabCard(), OctopusCard(), FishCard(), JellyfishCard()])  # All card types

        s = np.array([4] * len(a))
        deck = np.repeat(a, s)

        random.shuffle(deck)
        main_deck = deck.tolist()

        for x in range(16 * len(self.p)):
            draft_deck.append(main_deck.pop(0))

        return draft_deck

    def first_draft(self):
        """Appends first five cards to draft"""

        draft_row = []
        for x in range(5):
            draft_row.append(self.deck.pop(0))

        return draft_row

    def winner(self):
        if self.p1.points > self.p2.points:
            print("Player 1 wins!")
        elif self.p2.points > self.p1.points:
            print("Player 2 wins!")
        else:
            print("Remíza")
