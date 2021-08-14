import pygame as pg
from button import Button

# Try and make a recursive pizza topping (pizza on pizza)

# TODO add buttons to top
# TODO add functionality to buttons
# TODO create pizza surface

WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))


def draw(*args):
    WIN.fill((128, 128, 128))
    WIN.blit(pg.image.load("Pepperoni.png"), pg.image.load("Pepperoni.png").get_rect(x=0, y=0))
    for arg in args:
        WIN.blit(arg.surface, arg.rect)
    pg.display.update()


def main():
    offset = 64
    pepperoni = Button((26, 26))
    mushroom = Button((26+offset*1, 26))
    oliveB = Button((26+offset*2, 26))
    oliveG = Button((26+offset*3, 26))
    pineapple = Button((26+offset*4, 26))
    sausage = Button((26+offset*5, 26))
    buttons = [pepperoni, mushroom, oliveB, oliveG, pineapple, sausage]
    toppings = ["Pepperoni.png", "Mushroom_Red.png", "Olive_Black.png", "Olive_Green.png", "Pineapple.png", "Sausage.png"]
    for x in range(len(toppings)):
        img = pg.image.load(toppings[x])
        # buttons[x].surface.blit(img, img.get_rect(x=0, y=0))
    play = True
    printed = False
    while play:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                play = False
        if pg.mouse.get_pressed()[0] and pepperoni.rect.collidepoint(pg.mouse.get_pos()):
            pepperoni.rect.center = pg.mouse.get_pos()
        draw(*buttons)
        if pg.mouse.get_pressed()[2] and not printed:
            printed = True
            print([button.rect.center for button in buttons])
        pg.display.set_caption("pizza")


if __name__ == "__main__":
    main()