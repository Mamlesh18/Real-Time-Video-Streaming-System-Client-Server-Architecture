import cv2
import socket
import pickle
import struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.43.138', 5556))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    connection = client_socket.makefile('wb')

    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, (640, 480))
            data = pickle.dumps(frame)
            size = struct.pack('>L', len(data))
            connection.write(size + data)
    except:

        pass

    connection.close()
    client_socket.close()
