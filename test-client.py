import QDP

client = QDP.QDPclient()

client.send_packet(0, "Test:\nHello!")

client.close()