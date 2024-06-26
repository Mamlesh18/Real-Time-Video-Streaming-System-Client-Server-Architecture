import cv2
import socket
import pickle
import struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.39.214', 5555))

connection = client_socket.makefile('rb')

try:
    while True:
        size = struct.unpack('>L', connection.read(struct.calcsize('>L')))[0]
        data = connection.read(size)
        frame = pickle.loads(data)
        cv2.imshow('Received', frame)
        cv2.waitKey(1)
except:
    pass

connection.close()
client_socket.close()
cv2.destroyAllWindows()
