import requests as rq
import datetime

class User:
    def __init__(self, ip, dev_name, mac_id):
        self.ip = ip
        self.dev_name = dev_name
        self.connection_time = datetime.datetime.now()
        self.mac_id = mac_id

    def get_user_ip(self):
        return self.ip

    def get_device(self):
        return self.dev_name

    def get_mac(self):
        return self.mac_id