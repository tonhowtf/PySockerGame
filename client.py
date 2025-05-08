import pygame
import sys
import socket
import pickle
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))


pygame.init()

WIDTH = 640
HEIGHT = 360

display = pygame.display.set_mode((WIDTH, HEIGHT))

game_status = {
  "player1": [20, 250, 20, 40],
  "player2": [600, 250, 20, 40],
  "ball": [320,180],
  "ball_dir_x":1,
  "ball_dir_y":1
            }


def update_game_status():
  global game_status

  try:
    while True:
      data = pickle.loads(client.recv(4096))
      game_status = data
      print(game_status)
  except Exception as error:
    print(f"Erro encotrado: {error}")

threading.Thread(target=update_game_status, daemon=True).start()  


def draw(display):
  pygame.draw.rect(display, "blue", game_status["player1"])
  pygame.draw.rect(display, "red", game_status["player2"])
  pygame.draw.circle(display, "white", game_status["ball"], 10)


fps = pygame.time.Clock()
while True:


  fps.tick(30)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  key = pygame.key.get_pressed()
  if key[pygame.K_UP]:
    client.sendall(pickle.dumps("UP"))
  elif key[pygame.K_DOWN]:  
    client.sendall(pickle.dumps("DOWN"))

  display.fill("black")
  draw(display)
  pygame.display.update()
