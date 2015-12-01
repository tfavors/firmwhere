"""
FILE NAME: Connection.py

DESCRIPTION: Contains the Connection class. Connection class inherits threading.Thread, which allows processes in
Connection to occur while other parts of the software execute in parallel.

Connection objects are 1:1 with an IP address, and serve as the gateway between processes in this software and
the routers that are the intended targets.

REFERENCE:
Requires three standard Python 2.7 libraries: ftplib, telnetlib, and threading.
"""

from ftplib import FTP
from telnetlib import Telnet
import threading

class Connection(threading.Thread):

        """Constructor for the Connection class. Requires 3 parameters:
        1) The Update object that is creating this Connection object
        2) The host that this Connection object will work with
        3) The flag for whether the Connection object is a part of an update cycle or a polling cycle."""
        def __init__(self, caller, ip, flag):
            threading.Thread.__init__(self)
            self.host = ip
            self.thread_caller = caller
            self.profile = caller.profile
            self.flag = flag
            self.log = caller.log

        """Function that is called when ConnectionObject.run() is called.
            Inherited from the super class, threading.Thread
            Determines if this connection object is a part of an update cycle or a poll cycle."""
        def run(self):
            if self.flag is True:
                self.update_cycle()
            else:
                self.poll_cycle()

        """Update cycle actually performs both phases of the update; it checks to see if the firmware is valid by polling
            the device through telnet. If invalid, will create an FTP connection and push the correct firmware. """
        def update_cycle(self):
            self.thread_caller.thread_count += 1
            tel_conn = self.shell_connection()
            self.login(tel_conn)
            if self.firmware_check(tel_conn) is False:
                #Tells log that bad firmware was found in initial update cycle.
                self.log.ini_bad_firm()

                ftp_conn = self.file_connection()
                tel_conn.close()
                ftp_conn.login(self.profile.username, self.profile.password)
                self.send_file(ftp_conn)
                ftp_conn.close()
            else:
                #Tells log that good firmware was found in initial update cycle.
                self.log.ini_good_firm()
            self.thread_caller.thread_count -= 1

        """Method is ran after a full iteration of the update_cycle(). This method checks the total number of correct
            and incorrect firmwares to determine if updates were successful"""
        def poll_cycle(self):
            self.thread_caller.thread_count += 1
            tel_conn = self.shell_connection()
            self.login(tel_conn)
            if self.firmware_check(tel_conn) is False:
                #Tells log that bad firmware was found in second update cycle (poll)
                self.log.fin_bad_firm()
            else:
                #Tells log that good firmware was found in second update cycle.
                self.log.fin_good_firm()
            tel_conn.close()
            self.thread_caller.thread_count -= 1

        """Logs into the shell over telnet using the specified username and password"""
        def login(self, t_conn):
            t_conn.send(self.profile.username)
            t_conn.send(self.profile.password)
            t_conn.read_eager()

        """Uses the 'get_firmware' command specified in the selected profile to retrieve the current firmware
            on the device. Checks to see if it matches valid firmware, and returns True or False accordingly."""
        def get_firmware(self, t_conn):
            t_conn.send(self.profile.get_firmware)
            active_firm = t_conn.read_eager()
            if self.profile.firmware_version in active_firm:
                return True
            else:
                return False

        """Creates the FTP object and starts the connection. Returns the FTP object."""
        def file_connection(self):
            ftp_conn = FTP()
            ftp_conn.set_pasv(0)
            ftp_conn.connect(self.host, self.profile.ftp_port, 3)  #timeout is 3 seconds
            return ftp_conn

        """Creates the Telnet object and starts the connection. Returns the Telnet object"""
        def shell_connection(self):
            telnet_conn = Telnet.open(self.host, self.profile.telnet_port, 3)  #timeout is 3 seconds
            return telnet_conn

        """Takes the binary of the firmware file (which is specified in the profile),
            and sends it over the FTP connection."""
        def send_file(self, ftp_conn):
            ftp_conn.storbinary("STOR "+self.profile.firmware_file_name, self.profile.binary)

