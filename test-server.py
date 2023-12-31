import QDP

server = QDP.QDPserver()

data = server.recvpacket()

print(f"num:{data.num}\nmessage:{data.message}\naddr:{data.addr}")

server.close()