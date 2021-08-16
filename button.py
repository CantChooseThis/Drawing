import pygame as pg


class Button:
    def __init__(self, center, image):  # center is a tuple
        self.image = image
        self.surface = pg.image.load(image+".png")
        self.rect = self.surface.get_rect(center=center)
        # self.state = False

    def copy(self):
        duplicate = Button((self.rect.x, self.rect.y+50), self.image)
        return duplicate

    # def toggle(self):
    #     if self.state:
    #         self.state = not self.state
    #         self.surface = self.unchecked
    #         self.rect = self.surface.get_rect(x=self.rect.x, y=self.rect.y)
    #
    #     else:
    #         self.state = not self.state
    #         self.surface = self.checked
    #         self.rect = self.surface.get_rect(x=self.rect.x, y=self.rect.y)

