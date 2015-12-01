"""
FILENAME: Update.py

DESCRIPTION: Contains the Update Class. Update class corresponds to a singular and specific request by the user to
initiate a firmware update on a list of IP addresses, using the settings specified in the profile. Serves as the hub
for the creation of Connection Objects.

REFERENCES: Requires Connection, which is included in the package.
            Requires time, a standard python 2.7 library.
"""

from Main import Connection
import time


class Update:
    """Constructor method for the Update class. This object is created whenever a user chooses to launch an update.
    Update has 3 parameters and then a specified 4th field.
    1) log: The log object to which this specific update request will be reporting.
    2) profile: The settings to use during this update request.
    3) ip_list: The list of IPs the software will attempt to update.
    4th Field) thread_count: Variable that tracks how many threads are active at one time. thread_count is incremented
        and deducted as threads start and finish. Must be tracked here.
    """
    def __init__(self, log, profile, ip_list):
        self.log = log
        self.profile = profile
        self.ip_list = ip_list
        self.thread_count = 0

    """Method specifies two separate iterations of 'iterate_over_ips'; the first iteration corresponds with
        updating each router, and the second iteration is a 'poll' to determine the efficacy of the update."""
    def perform_update(self):
        self.iterate_over_ips(True)
        #We have to let our last 25 FTPs finish up before moving on.
        time.sleep(120)
        self.iterate_over_ips(False)

    """Method for iterating over each ip specified in the update request, creating up to 25 Connection objects at once,
        and starting each of their processes (threaded). It passes on the flag received by its call."""
    def iterate_over_ips(self, flag):
        for ip in self.ip_list:
            while self.thread_count >= 25:
                pass
            cn = Connection(self, ip, flag)
            cn.start()
