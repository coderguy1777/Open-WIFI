import socket as sk
class Server:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip
        self.curr_connection = []

    def init_connection(self, user=User):
        sk.create_connection(self.port, [self.ip, 1000])
        