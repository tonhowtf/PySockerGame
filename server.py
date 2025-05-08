import socket
import pickle
import threading
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(2)

print("Servidor iniciado: ")

game_status = {
  "player1": [20, 250, 20, 40],
  "player2": [600, 250, 20, 40],
  "ball": (320,180),
  "ball_dir_x":1,
  "ball_dir_y":1
            }

clients = []
def receive_data(conn, addr, player_name):
  global game_status

  clients.append(conn)
  print(f"Um cliente novo se conectou: {addr}")

  
  try:
    while True:
      data = pickle.loads(conn.recv(1024))
      
      if data == "UP":
        game_status[player_name][1] -= 1
      elif data == "DOWN":
        game_status[player_name][1] += 1
      

  except Exception as error:
    print(error)

  def check_collision(ball, player):
    ball_x, ball_y = ball
    player_x, player_y, player_width, player_height = player

    closest_x = max(player_x, min(ball_x, player_x + player_width))
    closest_y = max(player_y, min(ball_y, player_y + player_height))

    return (ball_x - closest_x) ** 2 + (ball_y - closest_y) ** 2 < (10 ** 2)
  
  def update_game_status():

    global game_status

    try:
      while True:

        game_status["ball"][0] += game_status["ball_dir_x"]
        game_status["ball"][1] += game_status["ball_dir_y"]

        if game_status["ball"][0] < 0 or game_status["ball"][0] > 640:
          game_status["ball_dir_x"] *= -1
        
        if game_status["ball"][1] < 0 or game_status["ball"][1] > 360:
          game_status["ball_dir_y"] *= -1

        for client in clients:
          client.sendall(picklçe.dumps(game_status))

          time.sleep(0.1)
    except Exception as error:
      print(f"Erro encontrado: {error}")


while True:  

  conn, addr = server.accept()
  if len(clients) == 0:
    player_name = "player1"
  else:
    player_name = "player2"
  threading.Thread(target=receive_data, args=(conn, addr, player_name), daemon=True).start()

  