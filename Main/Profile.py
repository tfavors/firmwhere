__author__ = 'pwn'

class Profile:

    def __init__(self, profile_file):
        p = profile_file
        self.username = self.parse_username(p)
        self.password = self.parse_password(p)
        self.firmware_version = self.parse_firmware_version(p)
        self.ftp_port = self.parse_ftp_port(p)
        self.telnet_port = self.parse_telnet_port(p)
        self.binary = self.import_file(p)
        self.firmware_file_name = self.parse_filename(p)
        self.get_firmware = self.parse_get_firmware(p)


    def parse_username(self, p_file):
        pass

    def parse_password(self, p_file):
        pass

    def parse_firmware_version(self, p_file):
        pass

    def parse_ftp_port(self, p_file):
        pass

    def parse_telnet_port(self, p_file):
        pass

    def import_file(self, p_file):
        pass

    def parse_filename(self, p_file):
        pass

    def get_firmware(self):
        pass