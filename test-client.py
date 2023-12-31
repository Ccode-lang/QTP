import QDP

client = QDP.QDPclient()

client.send_packet(0, "Hello!")

client.close()