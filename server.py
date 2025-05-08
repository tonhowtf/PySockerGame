import socket
import pickle
import threading

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
      for client in clients:
        client.sendall(pickle.dumps(game_status))

  except Exception as error:
    print(error)

while True:  

  conn, addr = server.accept()
  if len(clients) == 0:
    player_name = "player1"
  else:
    player_name = "player2"
  threading.Thread(target=receive_data, args=(conn, addr, player_name), daemon=True).start()

  