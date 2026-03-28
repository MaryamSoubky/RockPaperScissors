import pygame
import sys
from button import Button
import game_logic
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BG_COLOR, TEXT_COLOR, HOVER_TEXT_COLOR,
    NORMAL_BUTTON_COLOR, HOVER_BUTTON_COLOR,
    FONT_PATH,
)

pygame.init()

icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

BG = pygame.Surface(SCREEN.get_size())
BG.fill((93, 78, 96))


def get_font(size):
    return pygame.font.Font(FONT_PATH, size)


# ---------------------------------------------------------------------------
# Game screen
# ---------------------------------------------------------------------------

def game_screen():
    """Main gameplay loop — renamed from play() to avoid shadowing game_logic.play()."""

    # Game state
    result_text = ""
    result_alpha = 0
    computer_choice = ""
    score = {'wins': 0, 'losses': 0, 'ties': 0}

    # Build buttons once, outside the loop
    rock_btn     = Button(image="images/rock.png",     pos=(340, 350), text_input=None, font=None, size=(200, 200))
    paper_btn    = Button(image="images/paper.png",    pos=(640, 350), text_input=None, font=None, size=(200, 200))
    scissors_btn = Button(image="images/scissors.png", pos=(940, 350), text_input=None, font=None, size=(200, 200))
    back_btn     = Button(image=None, pos=(640, 600),  text_input="BACK", font=get_font(75))

    action_buttons = [rock_btn, paper_btn, scissors_btn]
    choice_map = {id(rock_btn): 'r', id(paper_btn): 'p', id(scissors_btn): 's'}

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill(BG_COLOR)

        # Title
        title = get_font(70).render("Choose rock, paper, or scissors.", True, TEXT_COLOR)
        SCREEN.blit(title, title.get_rect(center=(640, 100)))

        # Score display
        score_text = get_font(35).render(
            f"Wins: {score['wins']}  Losses: {score['losses']}  Ties: {score['ties']}",
            True, TEXT_COLOR
        )
        SCREEN.blit(score_text, score_text.get_rect(center=(640, 200)))

        # Draw BACK button background, then all buttons
        back_btn.draw_background(screen=SCREEN, mouse_pos=mouse_pos)
        for btn in [*action_buttons, back_btn]:
            btn.change_color(mouse_pos)
            btn.update(SCREEN)

        # Result text (fades in)
        if result_text:
            full = f"{result_text}  (Computer chose {game_logic.get_choice_name(computer_choice)})"
            result_surf = get_font(40).render(full, True, TEXT_COLOR)
            result_surf.set_alpha(result_alpha)
            SCREEN.blit(result_surf, result_surf.get_rect(center=(640, 500)))
            if result_alpha < 255:
                result_alpha = min(result_alpha + 5, 255)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in action_buttons:
                    if btn.check_for_input(mouse_pos):
                        user_choice = choice_map[id(btn)]
                        result_text, computer_choice = game_logic.play(user_choice)
                        result_alpha = 0

                        # Update score
                        if result_text == "You won!":
                            score['wins'] += 1
                        elif result_text == "You lost!":
                            score['losses'] += 1
                        else:
                            score['ties'] += 1

                if back_btn.check_for_input(mouse_pos):
                    main_menu()

        pygame.display.update()


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def main_menu():
    # Build buttons once, outside the loop
    play_btn = Button(image=None, pos=(640, 300), text_input="PLAY", font=get_font(120))
    quit_btn = Button(image=None, pos=(640, 460), text_input="QUIT", font=get_font(120))

    while True:
        SCREEN.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, TEXT_COLOR)
        SCREEN.blit(menu_text, menu_text.get_rect(center=(640, 100)))

        for btn in [play_btn, quit_btn]:
            btn.draw_background(screen=SCREEN, mouse_pos=mouse_pos)
            btn.change_color(mouse_pos)
            btn.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.check_for_input(mouse_pos):
                    game_screen()
                if quit_btn.check_for_input(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
