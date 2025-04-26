import pygame, sys
from button import Button
import game_logic
import random

pygame.init()

icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.Surface(SCREEN.get_size())
BG.fill((93, 78, 96))

normal_color = (168, 143, 172, 180)
hover_color = (239, 206, 250, 180)

def get_font(size):
    return pygame.font.Font("images/font.ttf", size)

def tint_image(image, tint_color):
    tinted = image.copy()
    tinted.fill(tint_color, special_flags=pygame.BLEND_RGBA_MULT)
    return tinted

def play():
    # --- Variables ---
    result_text = ""
    result_alpha = 0
    computer_choice = ""

    # --- Buttons ---
    ROCK_BUTTON = Button(image="images/rock.png", pos=(340, 350), text_input=None, font=None, base_color="#D4B2D8", hovering_color="#EFCEFA", size=(200, 200))
    PAPER_BUTTON = Button(image="images/paper.png", pos=(640, 350), text_input=None, font=None, base_color="#D4B2D8", hovering_color="#EFCEFA", size=(200, 200))
    SCISSORS_BUTTON = Button(image="images/scissors.png", pos=(940, 350), text_input=None, font=None, base_color="#D4B2D8", hovering_color="#EFCEFA", size=(200, 200))
    PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="#D4B2D8", hovering_color="#EFCEFA")

    choices_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("#5d4e60")

        # --- Title ---
        PLAY_TEXT = get_font(70).render("Choose rock, paper, or scissors.", True, "#D4B2D8")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # --- Buttons Update ---
        for button in [ROCK_BUTTON, PAPER_BUTTON, SCISSORS_BUTTON, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # --- Rectangle behind BACK button ---
        text_surface = PLAY_BACK.text
        text_rect = text_surface.get_rect(center=(640, 600))
        padding_x, padding_y = 40, 20
        bg_rect = pygame.Rect(0, 0, text_rect.width + padding_x, text_rect.height + padding_y)
        bg_rect.center = text_rect.center

        is_hovered = bg_rect.collidepoint(PLAY_MOUSE_POS)
        current_color = hover_color if is_hovered else normal_color

        rect_surf = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(rect_surf, current_color, rect_surf.get_rect(), border_radius=25)
        SCREEN.blit(rect_surf, bg_rect.topleft)

        # --- Show Result ---
        if result_text:
            full_result = f"{result_text} (Computer chose {choices_names[computer_choice]})"
            result_surface = get_font(40).render(full_result, True, "#D4B2D8")
            result_surface.set_alpha(result_alpha)
            result_rect = result_surface.get_rect(center=(640, 500))
            SCREEN.blit(result_surface, result_rect)

            if result_alpha < 255:
                result_alpha += 5

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ROCK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    result_text, computer_choice = game_logic.play('r')
                    result_alpha = 0
                elif PAPER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    result_text, computer_choice = game_logic.play('p')
                    result_alpha = 0
                elif SCISSORS_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    result_text, computer_choice = game_logic.play('s')
                    result_alpha = 0
                elif PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(200).render("MAIN MENU", True, "#D4B2D8")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        play_rect = pygame.Rect(440, 240, 400, 120)
        play_color = hover_color if play_rect.collidepoint(MENU_MOUSE_POS) else normal_color
        play_surf = pygame.Surface((400, 120), pygame.SRCALPHA)
        pygame.draw.rect(play_surf, play_color, play_surf.get_rect(), border_radius=25)
        SCREEN.blit(play_surf, play_rect.topleft)

        quit_rect = pygame.Rect(440, 400, 400, 120)
        quit_color = hover_color if quit_rect.collidepoint(MENU_MOUSE_POS) else normal_color
        quit_surf = pygame.Surface((400, 120), pygame.SRCALPHA)
        pygame.draw.rect(quit_surf, quit_color, quit_surf.get_rect(), border_radius=25)
        SCREEN.blit(quit_surf, quit_rect.topleft)

        PLAY_BUTTON = Button(image=None, pos=(640, 300), text_input="PLAY", font=get_font(120), base_color="#D4B2D8", hovering_color="#EFCEFA")
        QUIT_BUTTON = Button(image=None, pos=(640, 460), text_input="QUIT", font=get_font(120), base_color="#D4B2D8", hovering_color="#EFCEFA")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
