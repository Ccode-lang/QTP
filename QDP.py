import socket


class packet_data:
    def __init__(self, num : int, message : str, addr : tuple):
        self.num = num
        self.message = message
        self.addr = addr

class QDPclient:
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 5006
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def send_packet(self, num, message : str):
        newmessage = message.replace(":", "%1]")
        self.sock.sendto(f"{num}:{newmessage}".encode(), (self.IP, self.port))
    def close(self):
        self.sock.close()

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
        message = data[1].replace("%1]", ":")
        
        return packet_data(num, message, addr)
    def close(self):
        self.sock.close()
