import pygame, sys
from dino import Dino
from pygame.locals import QUIT
from cactus import Cactus

FPS = 60
clock = pygame.time.Clock()
pygame.init()
width = 600
height = 400
white = (255, 255, 255)
frame_count = 60
Dinorun1 = pygame.image.load("DinoRun1.png")
Dinorun2 = pygame.image.load("DinoRun2.png")
Dinorunning = [Dinorun1, Dinorun2]

dino = Dino(25, height - 91, Dinorunning)

cactus = Cactus()
screen = pygame.display.set_mode((width, height))


def draw(obj):
    screen.blit(obj.image, (obj.x, obj.y))


pygame.display.set_caption('Dino Jump!')
newspeed = 0
while True:
    if pygame.sprite.collide_mask(dino,cactus):
      pygame.quit()
      sys.exit()
    if frame_count == 60:
        frame_count = 0

    if dino.is_jumping:
        dino.jump()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino.is_jumping == False:
                dino.jump()
                jump_movement = 10
                dino.is_jumping = True

    newspeed += 0.0040
    
    
    screen.fill(white)
    draw(dino)
    draw(cactus)
    dino.update()

    cactus.changespeed(newspeed)

    if cactus.x > -10:
        cactus.x -= cactus.speed
    else:
        cactus.x = width + 100

    frame_count += 1
    pygame.display.update()
    clock.tick(FPS)
