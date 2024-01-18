# _*_ coding: utf 8
import pygame as pg
import sys
import random as rd

# Konstanter
WIDTH = 400
HEIGHT = 600

# Størrelsen på vinduet
SIZE = (WIDTH, HEIGHT)

# FRAMES PER SECOND
FPS = 80

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (110, 110, 110)
LIGHTBLUE = (175, 175, 255)

# Rektangel posisjon
x = 0
y = 0
h = 25
w = 25

# Fargen til rektangelet
COLOR = RED

# Initierer pygame
pg.init()

# Lager en overflate vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True

# Verdier for spilleren
w = 50
h = 80

# Start posisjon
x = WIDTH // 2
y = HEIGHT - h

#Henter bildet til spilleren
player_img = pg.image.load('bucket.png')

#POENG
Points = 0
liv = 3 

#Henter font
font = pg.font.SysFont('Arial', 26)
#Funksjon som viser antall poeng
def displayPoints():
    text_img = font.render(f"Antall poeng: {Points}",True, BLACK)
    surface.blit(text_img, (25, 50))

def antallLiv():
    text_img = font.render(f"Antall liv: {liv}",True, BLACK)
    surface.blit(text_img, (250, 50))


class Ball:
    def __init__(self):
        self.r = 10
        self.x = rd.randint(0, 400)
        self.y = -self.r
        
        
    def update(self):
        self.y += 1
        
    
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x, self.y), self.r)
        
            

#Lager et ball objekt
ball = Ball()




# Spill-løkken
while run:
    # Sørger for at løkken kjøres i korrekt hastighet
    clock.tick(FPS)

    # Går gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False  # Spillet skal avsluttes    

    # Fyller skjermen med en farge
    surface.fill(LIGHTBLUE)

    # Hastighet til spilleren
    vx = 0

    # Henter knappene fra tastaturet som trykkes på
    keys = pg.key.get_pressed()

    # Sjekker om ulike taster trykkes på
    if keys[pg.K_LEFT]:
        if x <= 0:
            vx = 0
        else:
            vx -= 10

    if keys[pg.K_RIGHT]:
        if x >= (WIDTH - w):
            vx = 0
        else:
            vx += 10

    if keys[pg.K_SPACE]:
        color_sequence = [(255, 0, 0), (0, 0, 255), (110, 110, 110), (0, 255, 0)]
        for color in color_sequence:
            COLOR = color
            pg.draw.rect(surface, COLOR, [x, y, w, h])
            pg.display.flip()
            pg.time.delay(10)
            Points += 1

    if keys[pg.K_TAB]:
        x = WIDTH // 2
        y = HEIGHT - h
        w = 50
        h = 80
        COLOR = (255, 0, 0)
        
    

    # Oppdaterer posisjonen til rektangelet
    x += vx
    
    #Ball
    ball.update()
    ball.draw()
    
    #Sjekker kollisjon
    if ball.y > y and x <= ball.x <= x + w:
        Points += 1
        ball = Ball()
    
    #Sjekker om vi ikke klarer fange ballen
    if ball.y + ball.r >= HEIGHT:
        liv -= 1
        ball = Ball()
        if liv <= 0:
            print("Du klarte ikke fange ballen")
            print(f"Antall poeng: {Points}")
            run = False
    
    if Points < 5:
        ball.y += 3
    elif 5 <= Points < 10:
        ball.y += 4
    elif 10 <= Points < 15:
        ball.y += 5
    elif 15 <= Points < 20:
        ball.y += 6
    else:
        ball.y += 8
        
        
    

    # Spiller
    #pg.draw.rect(surface, COLOR, [x, y, w, h])
    surface.blit(player_img, (x,y))
    
    #Tekst
    displayPoints()
    antallLiv()

    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()

# Avslutter pygame
pg.quit()
sys.exit()

