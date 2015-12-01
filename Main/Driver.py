from Main import Log
from Main import Update


class Driver:

    def __init__(self, database):
        self.database = database

    def perform_update(self, profile, ip_list):
        update_instance = Update(Log(), profile, ip_list)
        update_instance.perform_update()
        update_instance.log.printout()
        self.database.store_log(update_instance.log)








