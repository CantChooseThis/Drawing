import pygame as pg
from button import Button

WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))


def draw(*args, trash=None):
    WIN.fill((128, 128, 128))
    Pizza = pg.transform.scale(pg.image.load("Pizza.png"), (400, 400))
    WIN.blit(Pizza, (Pizza.get_rect(center=(250, 250))))
    for arg in args:
        WIN.blit(arg.surface, arg.rect)
    WIN.blit(trash[0], trash[1])
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
    clicking = False
    x = pg.image.load("X.png")
    xrect = x.get_rect(bottomleft=(0, HEIGHT))
    while play:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                play = False
        if pg.mouse.get_pressed()[0]:
            for button in buttons:
                if not clicking and button.rect.collidepoint(pg.mouse.get_pos()):
                    topping = button.copy()
                    toppings.append(topping)

                    # pg.mouse.set_pos(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]+50)
            for topping in toppings:
                if topping.rect.collidepoint(pg.mouse.get_pos()):
                    topping.rect.center = pg.mouse.get_pos()
            clicking = True
        else:
            for topping in toppings:
                if topping.rect.colliderect(xrect):
                    toppings.pop(toppings.index(topping))
            clicking = False
        draw(*buttons, *toppings, trash=(x, xrect))
        if pg.mouse.get_pressed()[2] and not printed:
            printed = True
            print([button.rect.center for button in buttons])
        pg.display.set_caption("pizza")


if __name__ == "__main__":
    main()
