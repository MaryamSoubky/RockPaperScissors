import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, size=None):
		if isinstance(image, str):
			self.image = pygame.image.load(image).convert_alpha()
			if size:
				self.image = pygame.transform.smoothscale(self.image, size)
		else:
			self.image = image
			if size and self.image is not None:
				self.image = pygame.transform.smoothscale(self.image, size)

		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input

		if self.text_input and self.font:
			self.text = self.font.render(self.text_input, True, self.base_color)
		else:
			self.text = None

		if self.image is not None:
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		elif self.text is not None:
			self.image = self.text
			self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		else:
			self.rect = pygame.Rect(self.x_pos, self.y_pos, 0, 0)

		if self.text is not None:
			self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		else:
			self.text_rect = None


	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		if self.text is not None:
			screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		return self.rect.collidepoint(position)

	def changeColor(self, position):
		if self.text is not None:
			if self.rect.collidepoint(position):
				self.text = self.font.render(self.text_input, True, self.hovering_color)
			else:
				self.text = self.font.render(self.text_input, True, self.base_color)

