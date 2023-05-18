import pygame


class Dino(pygame.sprite.Sprite):
  def __init__(self,x,y,Dinorunning):  
    super().__init__()
    self.x = x
    self.y = y
    self.image=Dinorunning[0]
    self.dinorunning=Dinorunning
    #self.image = pygame.image.load("Dino.png")
    #self.image = pygame.transform.scale(self.image,(100,80))
    self.jump_count = 35
    self.is_jumping = False
    self.isrunning=True 
    self.rect=self.image.get_rect()
    self.rect.x=self.x
    self.rect.y=self.y
    self.mask=pygame.mask.from_surface(self.image)

    self.runindex=0
  
  def jump(self):
    if self.is_jumping:
      if self.jump_count >= -35:
        neg =1
        if self.jump_count<0:
          neg= -1
        self.y-= self.jump_count**2*0.004*neg
        self.jump_count-=1
      else:
        self.is_jumping= False
        self.jump_count = 35
  def run(self):
    self.image=self.dinorunning[self.runindex//5]
    self.runindex+=1
    if self.runindex>=10:
      self.runindex=0
  def update(self):
    self.run()
    self.jump()
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    self.mask = pygame.mask.from_surface(self.image)
  