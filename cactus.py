import pygame

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
      self.x       =550     
      self.y       =350
    
      self.speed = 1.5      
      self.image = pygame.image.load("Cactus.png")
      self.image = pygame.transform.scale(self.image,(40,55))
      self.rect=self.image.get_rect()
      self.rect.x=self.x
      self.rect.y=self.y
      self.mask=pygame.mask.from_surface(self.image)
      
    def move(self):
      while self.x>0:
          self.x += self.speed
    
    def changespeed(self, newspeed):
      self.speed = newspeed
      