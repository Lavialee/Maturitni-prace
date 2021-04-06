import pygame
from network import Network

pygame.font.init()

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
BOARD_MARGIN = 285
ROWS = 4
COLS = 6

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Totem")


def get_image(type, width, height):
    name = ('assets/' + type + '.png')
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (width, height))
    return image


class SelectBoard:
    """stará se o interaktivitu karet"""

    def __init__(self):
        self.selected_card = None

    def check_collision_board(self, state, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
                rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    pos = col, row
                    state.selected_board = pos

    def check_collision_draft(self, state, mx, my):
        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                state.selected_draft = pos

    def check_hovered(self, state, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
                rect = pygame.draw.rect(window, WHITE, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    pos = col, row
                    state.hovered = pos
        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, WHITE, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                state.hovered = pos

    def buttons(self, state, mx, my):
        butt = pygame.draw.rect(window, BLACK, ( 1030, 780, 210, 60))
        if butt.collidepoint(mx, my):
            state.button_pressed = True


class ViewBoard:
    """vykresluje vše"""

    def __init__(self, state):
        self.valid = state.get_valid_placements()

    def update_draft(self, state):
        """vykresluje draft"""

        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            image = get_image(str(state.draft[pos]), DRAFT_CARD_SIZE, DRAFT_CARD_SIZE)
            window.blit(image, (x, y))

        if state.selected_draft is not None:
            place = (state.selected_draft * (DRAFT_CARD_SIZE + PADDING) + MARGINS)
            pygame.draw.rect(window, BLACK, (place, MARGINS, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE), 3, border_radius=1)

    def update_board(self, state):
        """vykresluje board"""

        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            if len(state.current_player.totems[col]) > 0:
                for row in range(len(state.current_player.totems[col])):
                    y = HEIGHT - MARGINS - ((row + 1) * CARD_SIZE) - (row * PADDING)
                    image = get_image(str(state.current_player.totems[col][row]), CARD_SIZE, CARD_SIZE)
                    window.blit(image, (x, y))

        for pos in range(len(state.get_valid_placements())):
            self.valid = state.get_valid_placements()
            col, row = self.valid[pos]
            a = col * (CARD_SIZE + PADDING) + MARGINS
            b = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
            pygame.draw.rect(window, DARK_GREY, (a, b, CARD_SIZE, CARD_SIZE), 5, border_radius=1)

        if state.selected_board is not None:
            c, d = state.selected_board
            if [c, d] in self.valid:
                x = c * (CARD_SIZE + PADDING) + MARGINS
                y = d * (CARD_SIZE + PADDING) + BOARD_MARGIN
                pygame.draw.rect(window, BLACK, (x, y, CARD_SIZE, CARD_SIZE), 3, border_radius=1)
            else:
                pass

    def sidebar(self, state):
        """vykresluje info o kartách"""

        pygame.draw.rect(window, LIGHT_GREY, (1030, BOARD_MARGIN, 210, 470))

        if state.hovered is not None and len(str(state.hovered)) <= 2:  # draft hovered
            pos = state.hovered
            image = get_image(str(state.draft[pos]), 210, 210)
            window.blit(image, (1030, BOARD_MARGIN))

        elif state.hovered is not None:  # board hovered
            col, row = state.hovered
            row = 3 - row
            if row <= (len(state.current_player.totems[col]) - 1):
                image = get_image(str(state.current_player.totems[col][row]), 210, 210)
                window.blit(image, (1030, BOARD_MARGIN))

    def buttons(self, state):
        """vykresluje tlačítka"""
        image = pygame.image.load('assets/move.png')
        window.blit(image, (1030, 780))
        if state.button_pressed:
            state.turn_end()
            state.button_pressed = False


def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    select = SelectBoard()

    while run:
        clock.tick(60)
        try:
            state = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        board = ViewBoard(state)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                select.check_collision_board(state, mx, my)
                select.check_collision_draft(state, mx, my)
                select.buttons(state, mx, my)

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                select.check_hovered(state, mx, my)

            window.fill(WHITE)
            board.update_draft(state)
            board.update_board(state)
            board.sidebar(state)
            board.buttons(state)
            pygame.display.flip()


main()
