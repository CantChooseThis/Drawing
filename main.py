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
    for arg in args:
        WIN.blit(arg.surface, arg.rect)
    pg.display.update()


def main():
    offset = 64
    pepperoni = Button((26, 26), "Pepperoni")
    mushroom = Button((26+offset*1, 26), "Mushroom_Red")
    oliveB = Button((26+offset*2, 26), "Olive_Black")
    oliveG = Button((26+offset*3, 26), "Olive_Green")
    pineapple = Button((26+offset*4, 26), "Pineapple")
    sausage = Button((26+offset*5, 26), "Sausage")
    buttons = [pepperoni, mushroom, oliveB, oliveG, pineapple, sausage]
    toppings = []
    play = True
    printed = False
    while play:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                play = False
        if pg.mouse.get_pressed()[0]:
            for button in buttons:
                if button.rect.collidepoint(pg.mouse.get_pos()):
                    topping = button.copy()
                    toppings.append(topping)

                    pg.mouse.set_pos(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]+50)

        draw(*buttons, *toppings)
        if pg.mouse.get_pressed()[2] and not printed:
            printed = True
            print([button.rect.center for button in buttons])
        pg.display.set_caption("pizza")


if __name__ == "__main__":
    main()
