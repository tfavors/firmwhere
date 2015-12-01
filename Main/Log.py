__author__ = 'pwn'
import datetime


class Log:

    def __init__(self):
        self.initial_good_firmware = 0
        self.final_good_firmware = 0
        self.initial_bad_firmware = 0
        self.final_bad_firmware = 0


    def ini_good_firm(self):
        self.initial_good_firmware += 1

    def fin_good_firm(self):
        self.final_good_firmware += 1

    def ini_bad_firm(self):
        self.initial_bad_firmware += 1

    def fin_bad_firm(self):
        self.final_bad_firmware += 1

    def profile_used(self, profile):
        self.profile = profile

    def time_of_update(self):
         self.time = datetime.today()

    def printout(self):
        pass
