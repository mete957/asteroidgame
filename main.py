import pygame
import constants
def main():
  print("Starting asteroids!")
  print(f"Screen width: {constants.SCREEN_WIDTH}")
  print(f"Screen height: {constants.SCREEN_HEIGHT}")

  pygame.init()
  screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
  running = True
  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    pygame.display.flip()
  
  pygame.quit()

if  __name__ == "__main__":
     main()
