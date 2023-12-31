import socket
import hashlib

def hashmessage(message):
    message_bytes = message.encode('utf-8')
    hash_object = hashlib.sha256(message_bytes)
    return hash_object.hexdigest()

class QDPclient:
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 5006
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def send_packet(self, num, message : str):
        newmessage = message.replace(":", "%1]")
        self.sock.sendto(f"{num}:{hashmessage(newmessage)}:{newmessage}".encode(), (self.IP, self.port))

class QDPserver:
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 5006
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.port))
    def recvpacket(self):
        data, addr = self.sock.recvfrom(1024)
        data = data.decode().split(":")

        num = data[0]
        hash = data[1]
        message = data[2]
        valid = False

        if hashmessage(message) == hash:
            valid = True
        
        print(f"num:{num}\nhash:{hash}\nmessage:{message}\nvalid:{valid}")
