#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
FILE NAME: GUI.py

DESCRIPTION: Contains the GUI menu functions.

Menu objects provide user interface between user and code.

REFERENCE:
Requires 32-bit Python 2.7 library: wxPython.
"""

import wx       # import the wxPython Library


class main_menu(wx.Frame):  

    """init method that runs on initialization of main_menu class. Requires 3 parameters:
    1) The main_menu object
    2) The parent frame of main_menu
    3) The title for the new window"""
    def __init__(self, parent, title):

        super(main_menu, self).__init__(parent, title=title,
            size=(390, 350))

        self.init_main_ui()
        self.Centre()
        self.Show()

    """init_main_ui method displays the main menu, allowing the user to navigate to the other menus. Requires 1 parameter:
    1) The main_menu object"""
    def init_main_ui(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        vert_organizer = wx.BoxSizer(wx.VERTICAL)

        update_menu_box = wx.BoxSizer(wx.HORIZONTAL)
        update_menu_btn = wx.Button(panel, label='Run Updates', size=(170, 40))
        update_menu_btn.Bind(wx.EVT_BUTTON,init_update_ui)
        update_menu_box.Add(update_menu_btn, border=50)
        profile_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        profile_btn = wx.Button(panel, label='Profiles', size=(170, 40))
        profile_btn.Bind(wx.EVT_BUTTON,init_profile_ui)
        profile_btn_box.Add(profile_btn, border=10)
        log_menu_box = wx.BoxSizer(wx.HORIZONTAL)
        log_menu_btn = wx.Button(panel, label='Logs', size=(170, 40))
        log_menu_btn.Bind(wx.EVT_BUTTON,init_log_ui)
        log_menu_box.Add(log_menu_btn, border=10)
        vert_organizer.Add(update_menu_box, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 50)
        vert_organizer.Add(profile_btn_box, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 25)
        vert_organizer.Add(log_menu_box, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 0)

        panel.SetSizer(vert_organizer)

"""init_profile_ui method displays the profile menu, allowing the user to view, edit, or create profiles.
    Requires 1 parameter:
    1) The event instance calling init_profile_ui"""
def init_profile_ui(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        prof_vert_organizer = wx.BoxSizer(wx.VERTICAL)

        label_box = wx.BoxSizer(wx.HORIZONTAL)
        label_box.Add((10,10))
        avail_prof_label = wx.StaticText(panel, label='Available Profiles')
        avail_prof_label.SetFont(font)
        label_box.Add(avail_prof_label)
        prof_vert_organizer.Add(label_box, flag= wx.TOP, border=20)

        prof_vert_organizer.Add((-1, 10))

        list_and_button_organizer = wx.BoxSizer(wx.HORIZONTAL)
        list_box = wx.BoxSizer(wx.HORIZONTAL)
        prof_list = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 250))
        list_box.Add(prof_list, proportion=1, flag=wx.EXPAND)

        prof_btn_organizer = wx.BoxSizer(wx.VERTICAL)
        new_prof_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        new_prof_btn = wx.Button(panel, label='New Profile', size=(170, 50))
        new_prof_btn.Bind(wx.EVT_BUTTON,profile_creation_ui)
        new_prof_btn_box.Add(new_prof_btn, flag= wx.LEFT, border=10)
        edit_prof_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        edit_prof_btn = wx.Button(panel, label='Edit Selected Profile', size=(170, 50))
        edit_prof_btn.Bind(wx.EVT_BUTTON,profile_creation_ui)
        edit_prof_btn_box.Add(edit_prof_btn, flag= wx.LEFT, border=10)

        prof_btn_organizer.Add((1, 10))
        prof_btn_organizer.Add(new_prof_btn_box)
        prof_btn_organizer.Add((1, 20))
        prof_btn_organizer.Add(edit_prof_btn_box)

        list_and_button_organizer.Add(list_box)
        list_and_button_organizer.Add(prof_btn_organizer)

        prof_vert_organizer.Add(list_and_button_organizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        prof_vert_organizer.Add((-1, 25))

        panel.SetSizer(prof_vert_organizer)
        panel.Show()

"""init_update_ui method displays the update menu, allowing the user to select a profile, enter a range of IP addresses,
    initiate an update, and view the result. Requires 1 parameter:
    1) The event instance calling init_update_ui"""
def init_update_ui(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        update_vert_organizer = wx.BoxSizer(wx.VERTICAL)

        label_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_prof_label_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_prof_label_organizer.Add((10,10))
        avail_prof_label = wx.StaticText(panel, label='Available Profiles')
        avail_prof_label.SetFont(font)
        avail_prof_label_organizer.Add(avail_prof_label)

        label_spacing_box = wx.BoxSizer(wx.HORIZONTAL)
        label_spacing_box.Add((75,10))
        addresses_to_update_label = wx.StaticText(panel, label='IP Addresses to Update')
        addresses_to_update_label.SetFont(font)
        label_spacing_box.Add(addresses_to_update_label)

        label_organizer.Add(avail_prof_label_organizer)
        label_organizer.Add(label_spacing_box)

        update_vert_organizer.Add(label_organizer, flag= wx.TOP, border=20)

        update_vert_organizer.Add((-1, 10))

        canvas_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_profiles_txt_box = wx.BoxSizer(wx.HORIZONTAL)
        avail_profiles_txt = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        avail_profiles_txt_box.Add(avail_profiles_txt, proportion=1, flag=wx.EXPAND)


        ip_address_list_box = wx.BoxSizer(wx.HORIZONTAL)
        ip_address_list = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        ip_address_list_box.Add(ip_address_list, proportion=1, flag=wx.EXPAND)

        canvas_organizer.Add(avail_profiles_txt_box)
        canvas_organizer.Add((30,10))
        canvas_organizer.Add(ip_address_list_box)

        update_vert_organizer.Add(canvas_organizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        button_organizer = wx.BoxSizer(wx.HORIZONTAL)

        status_organizer = wx.BoxSizer(wx.VERTICAL)

        status_label_box = wx.BoxSizer(wx.HORIZONTAL)
        status_label_box.Add((10,10))
        status_label = wx.StaticText(panel, label='Update Status')
        status_label.SetFont(font)
        status_label_box.Add(status_label)

        status_box = wx.BoxSizer(wx.HORIZONTAL)
        status_box.Add((10,10))
        status = wx.TextCtrl(panel, size=(162, 25))
        status_box.Add(status)

        status_organizer.Add(status_label_box)
        status_organizer.Add((10,5))
        status_organizer.Add(status_box)

        update_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        update_btn = wx.Button(panel, label='Update', size=(162, 48))
        update_btn_box.Add(update_btn, flag= wx.LEFT, border=27)

        button_organizer.Add((1, 50))
        button_organizer.Add(status_organizer)
        button_organizer.Add((1, 20))
        button_organizer.Add(update_btn_box)

        update_vert_organizer.Add((-1, 10))
        update_vert_organizer.Add(button_organizer)

        update_vert_organizer.Add((-1, 10))

        panel.SetSizer(update_vert_organizer)
        panel.Show()

"""init_log_ui method displays the log menu, allowing the user to view logs created by updates. Requires 1 parameter:
    1) The event instance calling init_log_ui"""
def init_log_ui(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vert_organizer = wx.BoxSizer(wx.VERTICAL)

        label_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_log_label_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_log_label_organizer.Add((10,10))
        avail_log_label = wx.StaticText(panel, label='Available Logs')
        avail_log_label.SetFont(font)
        avail_log_label_organizer.Add(avail_log_label)

        selectable_log_organizer = wx.BoxSizer(wx.HORIZONTAL)
        selectable_log_organizer.Add((93,10))
        selectable_log_label = wx.StaticText(panel, label='Selected Log')
        selectable_log_label.SetFont(font)
        selectable_log_organizer.Add(selectable_log_label)

        label_organizer.Add(avail_log_label_organizer)
        label_organizer.Add(selectable_log_organizer)

        vert_organizer.Add(label_organizer, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 10))

        canvas_organizer = wx.BoxSizer(wx.HORIZONTAL)
        avail_log_label_text_box = wx.BoxSizer(wx.HORIZONTAL)
        avail_log_label_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        avail_log_label_text_box.Add(avail_log_label_text, proportion=1, flag=wx.EXPAND)

        selectable_log_text_box = wx.BoxSizer(wx.HORIZONTAL)
        available_log_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        selectable_log_text_box.Add(available_log_text, proportion=1, flag=wx.EXPAND)

        canvas_organizer.Add(avail_log_label_text_box)
        canvas_organizer.Add((30,10))
        canvas_organizer.Add(selectable_log_text_box)

        vert_organizer.Add(canvas_organizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        button_organizer = wx.BoxSizer(wx.HORIZONTAL)
        open_log_folder_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        open_log_folder_btn = wx.Button(panel, label='Open Log Folder', size=(162, 50))
        open_log_folder_btn_box.Add(open_log_folder_btn, flag= wx.LEFT, border=8)
        view_log_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        view_log_btn = wx.Button(panel, label='View Log', size=(162, 50))
        view_log_btn_box.Add(view_log_btn, flag= wx.LEFT, border=27)

        button_organizer.Add((1, 50))
        button_organizer.Add(open_log_folder_btn_box)
        button_organizer.Add((1, 20))
        button_organizer.Add(view_log_btn_box)

        vert_organizer.Add((-1, 10))
        vert_organizer.Add(button_organizer)

        vert_organizer.Add((-1, 10))

        panel.SetSizer(vert_organizer)
        panel.Show()

"""profile_creation_ui method displays the profile creation menu, allowing the user to enter information to create
    profiles. Requires 1 parameter:
    1) The event instance calling profile_creation_ui"""
def profile_creation_ui(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)


        vert_organizer = wx.BoxSizer(wx.VERTICAL)

        username_box = wx.BoxSizer(wx.HORIZONTAL)
        username_box.Add((10,10))
        username_label = wx.StaticText(panel, label='Username:')
        username_label.SetFont(font)
        username_box.Add(username_label)
        username_text = wx.BoxSizer(wx.HORIZONTAL)
        username_text.Add((99,10))
        username = wx.TextCtrl(panel, size=(162, 25))
        username_text.Add(username)
        username_box.Add(username_text)
        vert_organizer.Add(username_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        password_box = wx.BoxSizer(wx.HORIZONTAL)
        password_box.Add((10,10))
        password_label = wx.StaticText(panel, label='Password:')
        password_label.SetFont(font)
        password_box.Add(password_label)
        password_text = wx.BoxSizer(wx.HORIZONTAL)
        password_text.Add((102,10))
        password = wx.TextCtrl(panel, size=(162, 25))
        password_text.Add(password)
        password_box.Add(password_text)
        vert_organizer.Add(password_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        firmware_version_box = wx.BoxSizer(wx.HORIZONTAL)
        firmware_version_box.Add((10,10))
        firmware_version_label = wx.StaticText(panel, label='Firmware Version:')
        firmware_version_label.SetFont(font)
        firmware_version_box.Add(firmware_version_label)
        firmware_version_text = wx.BoxSizer(wx.HORIZONTAL)
        firmware_version_text.Add((53,10))
        firmware_version = wx.TextCtrl(panel, size=(162, 25))
        firmware_version_text.Add(firmware_version)
        firmware_version_box.Add(firmware_version_text)
        vert_organizer.Add(firmware_version_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        ftp_port_box = wx.BoxSizer(wx.HORIZONTAL)
        ftp_port_box.Add((10,10))
        ftp_port_label = wx.StaticText(panel, label='Ftp Port:')
        ftp_port_label.SetFont(font)
        ftp_port_box.Add(ftp_port_label)
        ftp_port_text = wx.BoxSizer(wx.HORIZONTAL)
        ftp_port_text.Add((117,10))
        ftp_port = wx.TextCtrl(panel, size=(162, 25))
        ftp_port_text.Add(ftp_port)
        ftp_port_box.Add(ftp_port_text)
        vert_organizer.Add(ftp_port_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        telnet_port_box = wx.BoxSizer(wx.HORIZONTAL)
        telnet_port_box.Add((10,10))
        telnet_port_label = wx.StaticText(panel, label='Telnet Port:')
        telnet_port_label.SetFont(font)
        telnet_port_box.Add(telnet_port_label)
        telnet_port_text = wx.BoxSizer(wx.HORIZONTAL)
        telnet_port_text.Add((96,10))
        telnet_port = wx.TextCtrl(panel, size=(162, 25))
        telnet_port_text.Add(telnet_port)
        telnet_port_box.Add(telnet_port_text)
        vert_organizer.Add(telnet_port_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        file_location_box = wx.BoxSizer(wx.HORIZONTAL)
        file_location_box.Add((10,10))
        file_location_label = wx.StaticText(panel, label='File Location:')
        file_location_label.SetFont(font)
        file_location_box.Add(file_location_label)
        file_location_text = wx.BoxSizer(wx.HORIZONTAL)
        file_location_text.Add((83,10))
        file_location = wx.TextCtrl(panel, size=(162, 25))
        file_location_text.Add(file_location)
        file_location_box.Add(file_location_text)
        vert_organizer.Add(file_location_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        file_name_box = wx.BoxSizer(wx.HORIZONTAL)
        file_name_box.Add((10,10))
        file_name_label = wx.StaticText(panel, label='File Name:')
        file_name_label.SetFont(font)
        file_name_box.Add(file_name_label)
        file_name_text = wx.BoxSizer(wx.HORIZONTAL)
        file_name_text.Add((99,10))
        file_name = wx.TextCtrl(panel, size=(162, 25))
        file_name_text.Add(file_name)
        file_name_box.Add(file_name_text)
        vert_organizer.Add(file_name_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 1))

        get_firmware_command_box = wx.BoxSizer(wx.HORIZONTAL)
        get_firmware_command_box.Add((10,10))
        get_firmware_command_label = wx.StaticText(panel, label='Get Firmware Command:')
        get_firmware_command_label.SetFont(font)
        get_firmware_command_box.Add(get_firmware_command_label)
        get_firmware_command_text = wx.BoxSizer(wx.HORIZONTAL)
        get_firmware_command_text.Add((9,10))
        get_firmware_command = wx.TextCtrl(panel, size=(162, 25))
        get_firmware_command_text.Add(get_firmware_command)
        get_firmware_command_box.Add(get_firmware_command_text)
        vert_organizer.Add(get_firmware_command_box, flag= wx.TOP, border=20)

        vert_organizer.Add((-1, 20))

        create_profile_btn_box = wx.BoxSizer(wx.HORIZONTAL)
        create_profile_btn = wx.Button(panel, label='Create Profile', size=(162, 48))
        create_profile_btn_box.Add(create_profile_btn, flag= wx.LEFT | wx.RIGHT, border=117)  # wx.CENTER | wx.BOTTOM

        vert_organizer.Add(create_profile_btn_box)

        panel.SetSizer(vert_organizer)
        panel.Show()


if __name__ == '__main__':  # if this file is 'main', run the following statements

    app = wx.App(redirect = False)  # Create a new wx App called 'app'
    main_menu(None, title='FirmWhere: Main Menu')    # call the main menu class, pass the title 'Firmwhere: Main Menu'
                                                     # to the init function
    app.MainLoop()  # begin reveiving and processing user inputs
