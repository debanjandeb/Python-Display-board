import pygame,sys
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.font.init()
default_font = pygame.font.get_default_font()
font = pygame.font.SysFont("Arial", 50,bold=True)
clock=pygame.time.Clock()
color=(0,0,0)

pygame.mouse.set_visible(False)
def input1(events):
   for event in events:
      if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
            sys.exit()
      else:
         screen.fill(color)
         label = font.render('CENTRAL HOSPITAL DISPLAY BOARD', 1,(255,255,255))
         screen.blit(label, (550, 200))
         pygame.display.update()
         #clock.tick(60)
while True:
   input1(pygame.event.get())
