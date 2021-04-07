import random
import numpy as np

ROWS = 4
COLS = 6


class Player:
    def __init__(self):
        self.totems = [[], [], [], [], [], []]
        self.points = 0
        self.num = self


class Game:
    """stará se o vykreslení základní desky a možných míst kam """

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
            self.evaluate_move(sel, x, player)
            self.p[int(player)].totems[x].append(self.deck.pop())

    def evaluate_move(self, player, sel, x):
        card = self.draft[sel]
        if card.type == 'instant':
            points = card.get_instant_points(player, sel, x)
            self.p[int(player)].points = self.p[int(player)].points + points
            print(player, self.p[int(player)].points)
        print(card.type)

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


# CARD CLASSES #
# AIR #
class EagleCard:
    """Eagle (air, instant) - gain one point instantly, plus 2 points for each totem block under it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Eagle"

    def get_instant_points(self, Player, sel, x):
        points = 1
        return points


class CraneCard:
    """Crane (air, EoG) - gain one point, and additional 2 points for every crane in a diagonal from it"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'EoG'

    def __repr__(self):
        return "Crane"

    def get_eog_points(self):
        pass


class OwlCard:
    """Owl (air, passive) - all instant cards placed in it's totem after, give aditional 3 points"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'passive'

    def __repr__(self):
        return "Owl"

    def get_eog_points(self):
        pass


class HummingbirdCard:
    """Hummingbird (air, passive) - if there's less than three totem blocks in it's totem, EoG effects are double"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'passive'

    def __repr__(self):
        return "Hummingbird"

    def get_eog_points(self):
        pass


class MagpieCard:
    """Magpie (air, instant) - get 1 point, and 1 additional point for all air types on your board"""

    def __init__(self):
        self.element = 'Air'
        self.type = 'instant'

    def __repr__(self):
        return "Magpie"

    def get_instant_points(self, player, sel, x):
        points = 10
        return points

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

    def get_eog_points(self):
        pass


class WolfCard:
    """Vlk (earth, instant) -  get points: amount of wolves on board x2"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'instant'

    def __repr__(self):
        return "Wolf"

    def get_instant_points(self, player, sel, x):
        points = 10
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

    def get_instant_points(self, player, sel, x):
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

    def get_eog_points(self):
        pass


class MouseCard:
    """Mouse (earth, EoG) - one point, +1 point for any mice in a one block radius of it"""

    def __init__(self):
        self.element = 'Earth'
        self.type = 'EoG'

    def __repr__(self):
        return "Mouse"

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

    def get_instant_points(self, player, sel, x):
        points = 10
        return points

    def get_eog_points(self):
        pass


class ChameleonCard:
    """Chameleon (fire, instant) - one point, is counted as an appropriate animal in further instant effects"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Chameleon"

    def get_instant_points(self, player, sel, x):
        points = 10
        return points

    def get_eog_points(self):
        pass


class CrocodileCard:
    """Crocodile (fire, instant) - one point, add one point for every water animal in its row"""

    def __init__(self):
        self.element = 'Fire'
        self.type = 'instant'

    def __repr__(self):
        return "Crocodile"

    def get_instant_points(self, player, sel, x):
        points = 10
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

    def get_instant_points(self, player, sel, x):
        points = 10
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

    def get_instant_points(self, player, sel, x):
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

    def get_instant_points(self, player, sel, x):
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

    def get_instant_points(self, player, sel, x):
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

    def get_instant_points(self, player, sel, x):
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

    def get_instant_points(self, player, sel, x):
        points = 10
        return points

    def get_eog_points(self):
        pass


class JellyfishCard:
    """Jellyfish (water, instant) - one point, plus one point for every totem block next to it"""

    def __init__(self):
        self.element = 'Water'
        self.type = 'instant'

    def __repr__(self):
        return "Jellyfish"

    def get_instant_points(self, player, sel, x):
        points = 10
        return points

    def get_eog_points(self):
        pass
# END OF CARD CLASSES #
