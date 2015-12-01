import telnetlib
import ftplib
import time
import threading

class Connection(threading.Thread):

        def __init__(self, caller, ip, flag):
            threading.Thread.__init__(self)
            self.host = ip
            self.caller = caller
            self.profile = caller.profile
            self.flag = flag
            self.log = caller.log

        def run(self):
            if self.flag is True:
                self.update_cylce()
            else:
                self.poll_cycle()

        def update_cycle(self):
            self.caller.thread_count += 1
            tel_conn = self.shell_connection()
            self.login(tel_conn)

            if self.firmware_check(tel_conn) is False:
                ftp_conn = self.file_connection()
                tel_conn.close()
                ftp_conn.login(self.profile.user, self.profile.pass)
                self.send_file(ftp_conn)
                ftp_conn.close()
            self.caller.thread_count -= 1
            
        def poll_cylce(self):
            self.caller.thread_count += 1
            tel_conn = self.shell_connection()
            self.login(tel_conn)
            
            if self.firmware_check(tel_conn) is False:
                #update log
            else:
                #update log
            
            tel_conn.close()
            self.caller.thread_count -= 1

        def login(self, t_conn):
            t_conn.send(self.profile.user)
            t_conn.send(self.profile.pass)
            t_conn.read_eager()

        def get_firmware(self, t_conn):
            t_conn.send(self.profile.get_firmware)
            active_firm = t_conn.read_eager()
            if self.profile.firmware_name in active_firm:
                return True
            else:
                return False


        def file_connection(self):
            ftp_conn = FTP.connect(self.host, self.profile.ftp_port, 3)
            #add setpsv or not. 
            return ftp_conn

        def shell_connection(self):
            telnet_conn = Telnet.open(self.host, self.profile.telnet_port, 3)
            return telnet_conn

        def send_file(self):
            pass
        
        
    