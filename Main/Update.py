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
        self.iterate_over_ips(True)
        time.sleep(120)
        self.iterate_over_ips(False)

    def iterate_over_ips(self, flag):
        for ip in self.ip_list:
            while self.thread_count >= 25:
                pass
            cn = Connection(self, ip, flag)
            cn.start()
