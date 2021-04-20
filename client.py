import pygame
import pygame.freetype
from network import Network
from card_classes import *

pygame.init()
pygame.font.init()
pygame.freetype.init()
infoObject = pygame.display.Info()

WIDTH_OBJECTS = infoObject.current_w - 200

CARD_SIZE = WIDTH_OBJECTS//11
DRAFT_CARD_SIZE = WIDTH_OBJECTS//8
SIDEBAR_WIDTH = WIDTH_OBJECTS//6
SIDEBAR_HEIGHT = WIDTH_OBJECTS//3
PADDING = 25
MARGINS = 40
BOARD_MARGIN = DRAFT_CARD_SIZE + PADDING + MARGINS
ROWS = 4
COLS = 6

WIDTH = (DRAFT_CARD_SIZE + PADDING) * COLS + MARGINS
HEIGHT = DRAFT_CARD_SIZE + ROWS * (PADDING + CARD_SIZE) + 2 * MARGINS
WHITE = (255, 255, 255)
LIGHT_GREY = (245, 245, 245)
DARK_GREY = (210, 210, 210)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Totem")
font = pygame.freetype.SysFont('Arial', 20)


def get_image(type, width, height):
    name = ('assets/' + type + '.png')
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (width, height))
    return image


def get_text(type):
    text = eval(f"{type}Card()")
    return text.__doc__


def your_turn(state, player):
    if state.current_player == player:
        return True
    else:
        return False


def get_opponent(player):
    if player == 1:
        return 2
    else:
        return 1


def game_is_end(state):
    if not state.draft and state.deck == []:
        return True
    else:
        return False


def word_wrap(surf, text, font, color=(0, 0, 0)):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height() + 2
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y


class SelectBoard:
    """card interactivity"""

    def check_collision_board(self, board, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
                rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    board.selected_board = col, row

    def check_collision_draft(self, state, board, mx, my):
        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                board.selected_draft = pos

        x = 5 * (DRAFT_CARD_SIZE + PADDING) + MARGINS
        y = MARGINS
        rect = pygame.draw.rect(window, LIGHT_GREY, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
        if rect.collidepoint(mx, my):
            board.selected_draft = 5

    def check_hovered(self, state, board, mx, my):
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            for row in range(ROWS):
                y = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
                rect = pygame.draw.rect(window, WHITE, (x, y, CARD_SIZE, CARD_SIZE))
                if rect.collidepoint(mx, my):
                    pos = col, row
                    board.hovered = pos

        for pos in range(len(state.draft)):
            x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
            y = MARGINS
            rect = pygame.draw.rect(window, WHITE, (x, y, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE))
            if rect.collidepoint(mx, my):
                board.hovered = pos

    def end_of_turn_btn(self, board, mx, my):
        btn = pygame.draw.rect(window, BLACK, (WIDTH - SIDEBAR_WIDTH - MARGINS, (ROWS - 1) * (CARD_SIZE + PADDING) + BOARD_MARGIN, SIDEBAR_WIDTH, 60))
        if btn.collidepoint(mx, my) and board.selected_draft is not None and board.selected_board is not None:
            board.end_turn_pressed = True

    def view_board_btn(self, board, mx, my):
        btn = pygame.draw.rect(window, BLACK, (WIDTH - SIDEBAR_WIDTH - MARGINS, (ROWS - 1) * (CARD_SIZE + PADDING) + BOARD_MARGIN + 70, SIDEBAR_WIDTH, 60))
        if btn.collidepoint(mx, my):
            if board.viewed_board == board.player:
                board.viewed_board = board.opponent
            else:
                board.viewed_board = board.player


class ViewBoard:
    """draws the state of the game"""

    def __init__(self, player, opponent):
        self.end_turn_pressed = False
        self.selected_draft = None
        self.selected_board = None
        self.hovered = None
        self.player = player
        self.opponent = opponent
        self.viewed_board = player

    def update_draft(self, state):
        """draws the draft"""
        if state.draft:
            for pos in range(len(state.draft)):
                x = pos * (DRAFT_CARD_SIZE + PADDING) + MARGINS
                y = MARGINS
                image = get_image(str(state.draft[pos]), DRAFT_CARD_SIZE, DRAFT_CARD_SIZE)
                window.blit(image, (x, y))
        if state.deck:
            for pos in range(1):
                x = 5 * (DRAFT_CARD_SIZE + PADDING) + MARGINS
                y = MARGINS
                image = get_image('deck', DRAFT_CARD_SIZE, DRAFT_CARD_SIZE)
                window.blit(image, (x, y))

        if self.selected_draft is not None:
            place = (self.selected_draft * (DRAFT_CARD_SIZE + PADDING) + MARGINS)
            pygame.draw.rect(window, BLACK, (place, MARGINS, DRAFT_CARD_SIZE, DRAFT_CARD_SIZE), 3, border_radius=1)

    def update_board(self, state):
        """draws the board"""
        self.your_turn = your_turn(state, self.player)
        for col in range(COLS):
            x = col * (CARD_SIZE + PADDING) + MARGINS
            if len(eval(f"state.p{self.viewed_board}.totems[col]")) > 0:
                for row in range(len(eval(f"state.p{self.viewed_board}.totems[col]"))):
                    y = (3 - row) * (CARD_SIZE + PADDING) + BOARD_MARGIN
                    image = get_image(str(eval(f"state.p{self.viewed_board}.totems[col][row]")), CARD_SIZE, CARD_SIZE)
                    window.blit(image, (x, y))

        for pos in range(len(self.get_valid_placements(state))):
            col, row = self.get_valid_placements(state)[pos]
            a = col * (CARD_SIZE + PADDING) + MARGINS
            b = row * (CARD_SIZE + PADDING) + BOARD_MARGIN
            pygame.draw.rect(window, DARK_GREY, (a, b, CARD_SIZE, CARD_SIZE), 5, border_radius=1)

        if self.selected_board is not None:
            c, d = self.selected_board
            if [c, d] in self.valid:
                x = c * (CARD_SIZE + PADDING) + MARGINS
                y = d * (CARD_SIZE + PADDING) + BOARD_MARGIN
                pygame.draw.rect(window, BLACK, (x, y, CARD_SIZE, CARD_SIZE), 3, border_radius=1)
            else:
                pass

    def sidebars(self, state):
        """draws information about the cards and points"""
        font_a = pygame.font.SysFont("Arial", 30)
        points = 'points on selected board: ' + str((eval(f"state.p{self.viewed_board}.points")))
        point_text = font_a.render(points, 1, (0, 0, 0))
        window.blit(point_text, (25, 5))
        sidebar = pygame.Surface((SIDEBAR_WIDTH, SIDEBAR_HEIGHT))
        sidebar.fill(WHITE)

        if self.hovered is not None and len(str(self.hovered)) <= 2:
            pos = self.hovered
            image = get_image(str(state.draft[pos]), SIDEBAR_WIDTH, SIDEBAR_WIDTH)
            text = get_text(str(state.draft[pos]))
            word_wrap(sidebar, text, font, BLACK)
            window.blit(sidebar, (WIDTH - SIDEBAR_WIDTH - PADDING, BOARD_MARGIN + PADDING + SIDEBAR_WIDTH))
            window.blit(image, (WIDTH - SIDEBAR_WIDTH - PADDING, BOARD_MARGIN))


        elif self.hovered is not None:
            col, row = self.hovered
            row = 3 - row
            if row <= (len(eval(f"state.p{self.viewed_board}.totems[col]")) - 1):
                image = get_image(str(eval(f"state.p{self.viewed_board}.totems[col][row]")), SIDEBAR_WIDTH, SIDEBAR_WIDTH)
                text = get_text(str(eval(f"state.p{self.viewed_board}.totems[col][row]")))
                word_wrap(sidebar, text, font, BLACK)
                window.blit(sidebar, (WIDTH - SIDEBAR_WIDTH - PADDING, BOARD_MARGIN + PADDING + SIDEBAR_WIDTH))
                window.blit(image, (WIDTH - SIDEBAR_WIDTH - PADDING, BOARD_MARGIN))

    def buttons(self):
        """draws buttons"""
        if self.your_turn:
            image = pygame.image.load('assets/move.png')
        else:
            image = pygame.image.load('assets/cantMove.png')
        window.blit(image, (WIDTH - SIDEBAR_WIDTH - PADDING, (ROWS - 1) * (CARD_SIZE + PADDING) + BOARD_MARGIN))

        if self.viewed_board == self.player:
            image = pygame.image.load('assets/opponent_board.png')

        else:

            image = pygame.image.load('assets/your_board.png')
        window.blit(image, (WIDTH - SIDEBAR_WIDTH - PADDING, (ROWS - 1) * (CARD_SIZE + PADDING) + BOARD_MARGIN + 70))

    def get_valid_placements(self, state):
        """find valid coordinates for placing"""

        self.valid = []
        for col in range(COLS):
            if len(eval(f"state.p{self.viewed_board}.totems[col]")) < 4:
                row = 3 - (len(eval(f"state.p{self.viewed_board}.totems[col]")))
                self.valid.append([col, row])
            else:
                pass

        return self.valid

    def turn_end(self, state):

        if self.selected_board is not None:
            if list(self.selected_board) in self.valid and self.end_turn_pressed:
                self.end_turn_pressed = False
                self.valid = self.get_valid_placements(state)
                return True


def main():
    """main pygame loop"""
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP()) + 1
    opponent = get_opponent(player)
    select = SelectBoard()
    board = ViewBoard(player, opponent)


    while run:
        clock.tick(60)
        try:
            state = n.send("get")
            assert state is not None
        except:
            run = False
            print("Couldn't get game")
            break

        if board.turn_end(state):
            x, y = board.selected_board
            n.send(str(board.selected_draft) + ',' + str(x) + ',' + str(y))
            board.selected_board = None
            board.selected_draft = None

        if game_is_end(state):
            print("GAME ENDED")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                select.end_of_turn_btn(board, mx, my)
                select.view_board_btn(board, mx, my)
                if your_turn(state, player) and board.viewed_board == player:
                    select.check_collision_board(board, mx, my)
                    select.check_collision_draft(state, board, mx, my)

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                select.check_hovered(state, board, mx, my)

            if not state.ready:
                window.fill((230, 225, 161))
                font = pygame.font.SysFont("Arial", 60)
                text = font.render("Waiting for second player...", 1, (0, 0, 0))
                window.blit(text, (40, 400))
                pygame.display.update()

            else:

                window.fill(WHITE)
                board.update_draft(state)
                board.update_board(state)
                board.sidebars(state)
                board.buttons()
                pygame.display.flip()


def menu_screen():
    """draws a basic menu screen"""
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        window.fill((230, 225, 161))

        menu = pygame.Surface((880, 880))
        menu.fill((230, 225, 161))
        font_a = pygame.font.SysFont("Arial", 60)
        text_click = font_a.render("Click to Play!", 1, (0, 0, 0))
        rules = "The rules are simple - make totems that bring you the most points! Take turns picking cards from the " \
                "central draft. Remember you have to build them from the bottom up. " \
                "Instant cards give you points instantly and EoG (End of Game) are counted up at the end of the game" \
                " - when the draft runs dry. You should also check your opponent's board, " \
                "you might snatch a card they wanted. "

        word_wrap(menu, rules, font, BLACK)
        window.blit(menu, (40, 400))
        window.blit(text_click, (40, 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
