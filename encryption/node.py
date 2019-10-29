from nodes import user
import sys
import os
class OpenWifiNode: 
    def __init__(self, msg,  user=User):
        self.user = user
        self.msg = msg
        self.key = 0

    def get_key(self):
        letter_vals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        letter_vals_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
        num_vals = [x for x in range(0, 256)]
