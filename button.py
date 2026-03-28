import pygame
from constants import TEXT_COLOR, HOVER_TEXT_COLOR, NORMAL_BUTTON_COLOR, HOVER_BUTTON_COLOR


class Button:
    def __init__(self, image, pos, text_input, font, base_color=TEXT_COLOR, hovering_color=HOVER_TEXT_COLOR, size=None):
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input

        self.image = self._load_image(image, size)
        self.text = self._build_text(base_color)

        # Rect is based on image if present, otherwise text
        base = self.image if self.image is not None else self.text
        self.rect = base.get_rect(center=(self.x_pos, self.y_pos)) if base else pygame.Rect(self.x_pos, self.y_pos, 0, 0)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) if self.text else None

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _load_image(self, image, size):
        """Load and optionally scale an image. Returns None if no image given."""
        if image is None:
            return None
        if isinstance(image, str):
            img = pygame.image.load(image).convert_alpha()
        else:
            img = image
        if size:
            img = pygame.transform.smoothscale(img, size)
        return img

    def _build_text(self, color):
        """Render the label surface. Returns None if no text given."""
        if self.text_input and self.font:
            return self.font.render(self.text_input, True, color)
        return None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        if self.text is not None:
            screen.blit(self.text, self.text_rect)

    def draw_background(self, screen, mouse_pos, padding_x=40, padding_y=20, border_radius=25):
        """Draw a rounded-rect background behind the button label (hover-aware)."""
        if self.text_rect is None:
            return
        bg_rect = pygame.Rect(0, 0,
                              self.text_rect.width + padding_x,
                              self.text_rect.height + padding_y)
        bg_rect.center = self.text_rect.center

        color = HOVER_BUTTON_COLOR if bg_rect.collidepoint(mouse_pos) else NORMAL_BUTTON_COLOR
        surf = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(surf, color, surf.get_rect(), border_radius=border_radius)
        screen.blit(surf, bg_rect.topleft)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, position):
        if self.text is not None:
            color = self.hovering_color if self.rect.collidepoint(position) else self.base_color
            self.text = self.font.render(self.text_input, True, color)

    # Keep old camelCase names as aliases so existing call-sites don't break
    def checkForInput(self, position):
        return self.check_for_input(position)

    def changeColor(self, position):
        self.change_color(position)
