__author__ = 'pwn'
from Main import Connection
import time


class Update:

    def __init__(self, log, profile, ip_list):
        self.log = log
        self.profile = profile
        self.ip_list = ip_list
        self.thread_count = 0

    def perform_update(self):

        for ip in self.ip_list:
            while self.thread_count >= 25:
                pass
            flag = True
            cn = Connection(self, ip, flag)
            cn.start()

        time.sleep(120)
        
        self.thread_count = 0
        for ip in self.ip_list:
            while self.thread_count >= 25:
                pass
            flag = False
            cn = Connection(self, ip, flag)
            cn.start()