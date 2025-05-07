import pygame

pygame.init()

WIDTH = 640
HEIGHT = 360

display = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(display):
  pygame.draw.rect(display, "blue", [20, 250, 20, 40])
  pygame.draw.rect(display, "red", [600, 250, 20, 40])
  pygame.draw.circle(display, "white", (320, 180), 10)


fps = pygame.time.Clock()
while True:
  fps.tick(30)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  display.fill("black")
  draw(display)
  pygame.display.update()
