import pygame
import logic

WIDTH = 1280
HEIGHT = 960
WHITE = (255, 255, 255)
LIGHT_GREY = (245, 245, 245)
DARK_GREY = (210, 210, 210)
BLACK = (0, 0, 0)
CARD_SIZE = 140
DRAFT_CARD_SIZE = 175
PADDING = 25
MARGINS = 40
ROWS = 4
COLS = 6

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Totem")


def select_totem_placement(mx, my, rectangles):
    if rectangles.collidepoint(mx, my):
        col = (mx - MARGINS) // COLS
        row = (my - 770 + ROWS * 175) // ROWS

        print(col, row)


def get_image(type, size):
    name = ('assets/' + type + '.png')
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (size, size))
    return image


class SelectBoard:
    """stará se o vykreslování jednotlivých karet"""

    def __init__(self):
        self.selected_card = None

    def check_collision_board(self, state, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + 285
                rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    pos = col, row
                    state.selected_board = pos
                    return pos

    def check_collision_draft(self, state, mx, my):
        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                state.selected_draft = pos


class ViewBoard:
    """vykresluje vše"""

    def __init__(self):
        self.hovered = False

    def update_draft(self, state):
        """vykresluje draft"""

        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            image = get_image(str(state.draft[pos]), DRAFT_CARD_SIZE)
            window.blit(image, (x, y))
        a = state.selected_draft
        if a is not None:
            pygame.draw.rect(window, BLACK,
                             ((a * (DRAFT_CARD_SIZE + PADDING) + MARGINS), MARGINS, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE),
                             3, border_radius=1)

    def update_board(self, state):
        """vykresluje board"""

        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + 285
                pygame.draw.rect(window, LIGHT_GREY, (x, y, CARD_SIZE, CARD_SIZE))

            if len(state.current_player.totems[col]) > 0:
                for row in range(len(state.current_player.totems[col])):
                    y = HEIGHT - MARGINS - ((row + 1) * CARD_SIZE) - (row * PADDING)
                    image = get_image(str(state.current_player.totems[col][row]), CARD_SIZE)
                    window.blit(image, (x, y))

        valid = state.get_valid_placements()
        for pos in range(len(state.get_valid_placements())):
            col, row = valid[pos]
            a = col * (CARD_SIZE + PADDING) + MARGINS
            b = row * (CARD_SIZE + PADDING) + 285
            pygame.draw.rect(window, DARK_GREY, (a, b, CARD_SIZE, CARD_SIZE), 5, border_radius=1)

        if state.selected_board is not None:
            col, row = state.selected_board
            c = col * (CARD_SIZE + PADDING) + MARGINS
            d = row * (CARD_SIZE + PADDING) + 285
            pygame.draw.rect(window, BLACK, (c, d, CARD_SIZE, CARD_SIZE), 3, border_radius=1)



def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()

    state = logic.State()
    state.current_player.totems[0].append('Lynx')
    state.current_player.totems[0].append('Lynx')
    state.current_player.totems[0].append('Lynx')
    state.current_player.totems[1].append('Lynx')
    state.current_player.totems[1].append('Lynx')
    state.current_player.totems[2].append('Lynx')
    state.current_player.totems[2].append('Lynx')
    state.current_player.totems[2].append('Lynx')
    state.current_player.totems[5].append('Lynx')
    state.current_player.totems[5].append('Lynx')

    print(state.current_player.totems)
    print(state.get_valid_placements())

    board = ViewBoard()
    select = SelectBoard()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                select.check_collision_board(state, mx, my)
                select.check_collision_draft(state, mx, my)

                print('draft v logic:', state.selected_draft)
                print('board v logic:', state.selected_board)

        window.fill(WHITE)
        board.update_draft(state)
        board.update_board(state)
        pygame.display.flip()


main()
