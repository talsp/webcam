import cv2
import socket
import struct
import pickle

cap = cv2.VideoCapture(0)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4444))
server_socket.listen(5)
conn, addr = server_socket.accept()

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    conn.sendall(message_size + data)

cap.release()
conn.close()
server_socket.close()
