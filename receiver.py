import socket
import threading
import cv2
import struct
import pickle

HOST = '127.0.0.1'
PORT = 4444

print("#"*90)
print("     Author: Talsp")
print("     This code is to be used for educational purposes or legal penetration testing only")
print("     I do not take responsibility for any misuse or illegal action/use of this code")
print("#"*90+"\n")

def handle_client(client_socket):
    data = b""
    payload_size = struct.calcsize("L")  # Expected size of packed message length
    while True:
        try:
            # Receive the message size
            while len(data) < payload_size:
                packet = client_socket.recv(4096)
                if not packet:
                    return
                data += packet

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]

            # Receive the frame data
            while len(data) < msg_size:
                data += client_socket.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            # Unpickle and display the frame
            frame = pickle.loads(frame_data)
            cv2.imshow('Receiver', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(e)
            break

    client_socket.close()
    cv2.destroyAllWindows()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Connection established with {addr}")
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()

    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    start_server()
