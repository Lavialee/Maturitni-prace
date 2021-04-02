import pygame
import logic

WIDTH = 1280
HEIGHT = 960
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
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

    def __init__(self, state):
        self.state = state
        self.selected_card = None

    def check_collision_board(self, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + 285
                rect = pygame.draw.rect(window, GREY, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    pos = row, col
                    logic.State.selected_board = pos
                    return pos

    def check_collision_draft(self, mx, my):
        for pos in range(len(self.state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                logic.State.selected_draft = pos
                return pos


class ViewBoard:
    """vykresluje board"""

    def __init__(self, state):
        self.state = state
        self.hovered = False

    def update_draft(self, state):
        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            image = get_image(str(self.state.draft[pos]), DRAFT_CARD_SIZE)
            window.blit(image, (x, y))
        a = state.selected_draft
        print(a)
        if len(a)>0:
            print('workin')
            pygame.draw.rect(window, BLACK, (a, MARGINS, DRAFT_CARD_SIZE + 2, DRAFT_CARD_SIZE + 2), 3, border_radius=1)

    def update_board(self, state):
        for col in range(COLS):
            if len(state.current_player.totems[col]) > 0:
                x = col * (CARD_SIZE + PADDING) + MARGINS
                for row in range(len(state.current_player.totems[col])):
                    y = HEIGHT - MARGINS - (row + 1 * CARD_SIZE) - (row * PADDING)
                    image = get_image(str(self.state.current_player.totems[col][row]), CARD_SIZE)
                    window.blit(image, (x, y))


def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()

    board = ViewBoard(logic.State())
    pokus = SelectBoard(logic.State())

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                pokus.check_collision_board(mx, my)
                pokus.check_collision_draft(mx, my)
                print('selected:', logic.State.selected_draft)

        window.fill(WHITE)
        board.update_draft(logic.State())
        board.update_board(logic.State())
        pygame.display.flip()


main()
