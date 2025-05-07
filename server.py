import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()

print("Servidor iniciado: ")

game_status = {
  "player1": [20, 250, 20, 40],
  "player2": [600, 250, 20, 40],
  "ball": (320,180),
  "ball_dir_x":1,
  "ball_dir_y":1
            }

while True:  

  conn, addr = server.accept()
  print(f"Um cliente novo se conectou: {addr}")