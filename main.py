import pygame

from models.gamestate import GameState

def main():
  pygame.init()
  pygame.display.set_caption('People Rocketry')
  running = True
  gamestate = GameState()
  last_draw_moment = gamestate.elapsed_time

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw():
  screen = pygame.display.set_mode((800, 600))
  screen.fill((255, 255, 255))
  pygame.display.flip()
  pygame.quit()

def update(dt: float, gamestate: GameState):
  """
  Update the game state.
  :param dt: The amount of time by which to update the game state
  """
  gamestate.elapsed_time += dt
  pass


if __name__ == '__main__':
  main()