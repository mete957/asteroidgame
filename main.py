import pygame
from constants import *
from player import *
from circleshape import *
def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  
  clock = pygame.time.Clock()

  updatable_group = pygame.sprite.Group()
  drawable_group = pygame.sprite.Group()
  Player.containers = (updatable_group, drawable_group)
  player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
  
  dt = 0
  running = True
  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    
    
    updatable_group.update(dt)

    screen.fill("black")

    for drw in drawable_group:
      drw.draw(screen)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
  
  pygame.quit()

if  __name__ == "__main__":
     main()
