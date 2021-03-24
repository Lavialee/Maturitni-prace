import pygame
import logic

width = 1280
height = 960
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
CARD_SIZE = 140
DRAFT_CARD_SIZE = 175
PADDING = 25
MARGINS = 40
ROWS = 4
COLS = 6

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Totem")


def draft_image_load(card_type):
    name = ('assets/' + card_type + '.png')
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
    return image


def totem_image_load(card_type):
    name = ('assets/' + card_type + '.png')
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (CARD_SIZE, CARD_SIZE))
    return image


def select_totem_placement(mx, my, rectangles):
    if rectangles.collidepoint(mx, my):
        col = (mx - MARGINS) // COLS
        row = (my - 770 + ROWS * 175) // ROWS

        print(col, row)


class ViewCard:
    """stará se o vykreslování jednotlivých karet"""

    def __init__(self, col, row, card_type, state):
        self.state = state
        self.col = col
        self.row = row
        self.x = 0
        self.y = 0
        self.card_type = card_type
        totem_image_load(card_type)
        draft_image_load(card_type)
        self.calculate_totem_pos()
        self.selected_card = None

    def calculate_totem_pos(self):
        self.x = (CARD_SIZE + PADDING) * self.col + MARGINS
        self.y = (CARD_SIZE + PADDING) * self.row + 280
        image = totem_image_load(self.card_type)
        window.blit(image, (self.x, self.y))



def draw_card_base(window):
    window.fill(WHITE)
    for col in range(COLS):
        x = col * (CARD_SIZE + PADDING) + MARGINS
        for row in range(ROWS):
            y = row * (CARD_SIZE + PADDING) + 280
            pygame.draw.rect(window, GREY, (x, y, CARD_SIZE, CARD_SIZE))


class ViewBoard:
    """vykresluje board"""

    def __init__(self, state):
        self.state = state
        self.hovered = False

    def update_draft(self):
        for pos in range(len(self.state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            card_type = str(self.state.draft[pos])
            name = ('assets/' + card_type + '.png')
            image = pygame.image.load(name)
            image = pygame.transform.scale(image, (DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            window.blit(image, (x, y))

    def draw_card_description(self):
        pass


def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()

    board = ViewBoard(logic.State())

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)

        draw_card_base(window)
        board.update_draft()
        pygame.display.flip()
        """ while is_game_end == False:###zjistit jak dát aby to dělala pro aktuálního hráče???
            card = draft[ draft_pos ]
            totem_pos = get_user_action_totem_pick()
            player[ current_player ][ totem_no ].append (card)
            draft[ draft_pos ] = deck.pop()      
        ###CARD CLASSES### """


main()
