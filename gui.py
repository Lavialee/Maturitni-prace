import pygame
import logic

WIDTH = 1280
HEIGHT = 960
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
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

class selectBoard:
    """stará se o vykreslování jednotlivých karet"""

    def __init__(self):
        self.state = state
        self.calculate_totem_pos()
        self.selected_card = None

    def calculate_totem_pos(self):
        self.x = (CARD_SIZE + PADDING) * self.col + MARGINS
        self.y = (CARD_SIZE + PADDING) * self.row + 280
        image = totem_image_load(self.card_type)
        window.blit(image, (self.x, self.y))

    def draw_card_base(self):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + 285
                pygame.draw.rect(window, WHITE, (x, y, CARD_SIZE, CARD_SIZE))



class ViewBoard:
    """vykresluje board"""

    def __init__(self, state):
        self.state = state
        self.hovered = False

    def update_draft(self):
        for pos in range(len(self.state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            image = get_image(str(self.state.draft[pos]), DRAFT_CARD_SIZE)
            window.blit(image, (x, y))

    def update_board(self):
        for col in range(COLS):
            if len(self.state.current_player.totems[col]) > 0:
                x = col * (CARD_SIZE + PADDING) + MARGINS
                for row in range(len(self.state.current_player.totems[col])):
                    y = HEIGHT - MARGINS - (row + 1 * CARD_SIZE) - (row * PADDING)
                    image = get_image(str(self.state.current_player.totems[col][row]), CARD_SIZE)
                    window.blit(image, (x, y))
            else:
                pass

    def draw_card_description(self):
        pass


def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()

    board = ViewBoard(logic.State())
    board.state.current_player.totems[0].append('Eagle')
    print(board.state.get_valid_placements())
    print(board.state.current_player.totems)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)

        window.fill(WHITE)
        draw_card_base()
        board.update_draft()
        board.update_board()
        pygame.display.flip()


main()
