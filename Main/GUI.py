#!/usr/bin/python
# -*- coding: utf-8 -*-

# MAIN GUI Code
# comment


import wx       # import the wxPython Library


class MainMenu(wx.Frame):   # the inital frame is for the main menu

    def __init__(self, parent, title):  # at initialization, call the following functions

        super(MainMenu, self).__init__(parent, title=title,
            size=(390, 350))

        self.InitMainUI()
        self.Centre()
        self.Show()

    def InitMainUI(self):

        panel = wx.Panel(self)  # create a wx panel called panel, our components will be displayed in this

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)    # get the default system font, and set it as the apllication font
        font.SetPointSize(12)   # set the default font size for this application to 12 point font

        vertOrganizer = wx.BoxSizer(wx.VERTICAL) # vbox = vertOrganizer

        updateMenuBox = wx.BoxSizer(wx.HORIZONTAL)  # hbox5 = updateMenuBox
        updateMenuBtn = wx.Button(panel, label='Run Updates', size=(170, 40))    # btn1 = updateMenuBtn
        updateMenuBtn.Bind(wx.EVT_BUTTON,InitUpdateUI)
        # btn1.onclick( UpdateMenu(None, title = 'Firmwhere: Update Menu'))
        updateMenuBox.Add(updateMenuBtn, border=50)  # wx.TOP | wx.CENTER | wx.BOTTOM
        profileBtnBox = wx.BoxSizer(wx.HORIZONTAL)  # hbox6 = profileBtnBox
        profileBtn = wx.Button(panel, label='Profiles', size=(170, 40))   # btn2 = profileBtn
        # btn2.onclick( ProfileMenu(None, title = 'Firmwhere: Profile Menu'))
        # profile = ProfileMenu(None, title='FirmWhere: Profile Menu')
        profileBtn.Bind(wx.EVT_BUTTON,InitProfileUI)
        profileBtnBox.Add(profileBtn, border=10)  # wx.CENTER | wx.BOTTOM
        logMenuBox = wx.BoxSizer(wx.HORIZONTAL)  # hbox7 = logMenuBox
        logMenuBtn = wx.Button(panel, label='Logs', size=(170, 40))   # btn3 = logMenuBtn
        logMenuBtn.Bind(wx.EVT_BUTTON,InitLogUI)
        # btn3.onclick(LogMenu(None, title = 'FirmWhere: Log Menu'))
        logMenuBox.Add(logMenuBtn, border=10)
        vertOrganizer.Add(updateMenuBox, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 50)  # Center | wx.Bottom
        vertOrganizer.Add(profileBtnBox, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 25)  # Center | wx.Bottom
        vertOrganizer.Add(logMenuBox, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT | wx.RIGHT, 0)  # Center | wx.Bottom

        panel.SetSizer(vertOrganizer)

def InitProfileUI(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        profVertOrganizer = wx.BoxSizer(wx.VERTICAL)

        labelBox = wx.BoxSizer(wx.HORIZONTAL)
        labelBox.Add((10,10))
        availProfLabel = wx.StaticText(panel, label='Available Profiles')
        availProfLabel.SetFont(font)
        labelBox.Add(availProfLabel)
        profVertOrganizer.Add(labelBox, flag= wx.TOP, border=20)

        profVertOrganizer.Add((-1, 10))

        listAndButtonOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        listBox = wx.BoxSizer(wx.HORIZONTAL)
        profList = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 250))
        listBox.Add(profList, proportion=1, flag=wx.EXPAND)

        profBtnOrganizer = wx.BoxSizer(wx.VERTICAL)
        newProfBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        newProfBtn = wx.Button(panel, label='New Profile', size=(170, 50))
        newProfBtn.Bind(wx.EVT_BUTTON,ProfileCreationUI)
        newProfBtnBox.Add(newProfBtn, flag= wx.LEFT, border=10)  # wx.TOP | wx.CENTER | wx.BOTTOM
        editProfBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        editProfBtn = wx.Button(panel, label='Edit Selected Profile', size=(170, 50))
        editProfBtn.Bind(wx.EVT_BUTTON,ProfileCreationUI)
        editProfBtnBox.Add(editProfBtn, flag= wx.LEFT, border=10)  # wx.CENTER | wx.BOTTOM

        profBtnOrganizer.Add((1, 10))
        profBtnOrganizer.Add(newProfBtnBox)
        profBtnOrganizer.Add((1, 20))
        profBtnOrganizer.Add(editProfBtnBox)

        listAndButtonOrganizer.Add(listBox)
        listAndButtonOrganizer.Add(profBtnOrganizer)

        profVertOrganizer.Add(listAndButtonOrganizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        profVertOrganizer.Add((-1, 25))

        panel.SetSizer(profVertOrganizer)
        panel.Show()


def InitUpdateUI(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        updateVertOrganizer = wx.BoxSizer(wx.VERTICAL)

        labelOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        availProfLabelOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        availProfLabelOrganizer.Add((10,10))
        availProfLabel = wx.StaticText(panel, label='Available Profiles')
        availProfLabel.SetFont(font)
        availProfLabelOrganizer.Add(availProfLabel)

        labelSpacingBox = wx.BoxSizer(wx.HORIZONTAL)
        labelSpacingBox.Add((75,10))
        addrToUpdateLabel = wx.StaticText(panel, label='IP Addresses to Update')
        addrToUpdateLabel.SetFont(font)
        labelSpacingBox.Add(addrToUpdateLabel)

        labelOrganizer.Add(availProfLabelOrganizer)
        labelOrganizer.Add(labelSpacingBox)

        updateVertOrganizer.Add(labelOrganizer, flag= wx.TOP, border=20)

        updateVertOrganizer.Add((-1, 10))

        canvasOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        availProfilesTxtBox = wx.BoxSizer(wx.HORIZONTAL)
        availProfilesTxt = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        availProfilesTxtBox.Add(availProfilesTxt, proportion=1, flag=wx.EXPAND)


        ipAddrListBox = wx.BoxSizer(wx.HORIZONTAL)
        ipAddrList = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        ipAddrListBox.Add(ipAddrList, proportion=1, flag=wx.EXPAND)

        canvasOrganizer.Add(availProfilesTxtBox)
        canvasOrganizer.Add((30,10))
        canvasOrganizer.Add(ipAddrListBox)

        updateVertOrganizer.Add(canvasOrganizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        buttonOrganizer = wx.BoxSizer(wx.HORIZONTAL)

        statusOrganizer = wx.BoxSizer(wx.VERTICAL)

        statusLabelBox = wx.BoxSizer(wx.HORIZONTAL)
        statusLabelBox.Add((10,10))
        statusLabel = wx.StaticText(panel, label='Update Status')
        statusLabel.SetFont(font)
        statusLabelBox.Add(statusLabel)

        statusBox = wx.BoxSizer(wx.HORIZONTAL)
        statusBox.Add((10,10))
        status = wx.TextCtrl(panel, size=(162, 25))
        statusBox.Add(status)

        statusOrganizer.Add(statusLabelBox)
        statusOrganizer.Add((10,5))
        statusOrganizer.Add(statusBox)

        updateBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        updateBtn = wx.Button(panel, label='Update', size=(162, 48))
        updateBtnBox.Add(updateBtn, flag= wx.LEFT, border=27)  # wx.CENTER | wx.BOTTOM

        buttonOrganizer.Add((1, 50))
        buttonOrganizer.Add(statusOrganizer)
        buttonOrganizer.Add((1, 20))
        buttonOrganizer.Add(updateBtnBox)

        updateVertOrganizer.Add((-1, 10))
        updateVertOrganizer.Add(buttonOrganizer)

        updateVertOrganizer.Add((-1, 10))

        panel.SetSizer(updateVertOrganizer)
        panel.Show()


def InitLogUI(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vertOrganizer = wx.BoxSizer(wx.VERTICAL)

        labelOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        availLogLabelOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        availLogLabelOrganizer.Add((10,10))
        availLogLabel = wx.StaticText(panel, label='Available Logs')
        availLogLabel.SetFont(font)
        availLogLabelOrganizer.Add(availLogLabel)

        selLogOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        selLogOrganizer.Add((93,10))
        selLogLabel = wx.StaticText(panel, label='Selected Log')
        selLogLabel.SetFont(font)
        selLogOrganizer.Add(selLogLabel)

        labelOrganizer.Add(availLogLabelOrganizer)
        labelOrganizer.Add(selLogOrganizer)

        vertOrganizer.Add(labelOrganizer, flag= wx.TOP, border=20)

        vertOrganizer.Add((-1, 10))

        canvasOrganizer = wx.BoxSizer(wx.HORIZONTAL)# hbox3 #hold canvas and buttons
        availLogLabelTxtBox = wx.BoxSizer(wx.HORIZONTAL)
        availLogLabelText = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        availLogLabelTxtBox.Add(availLogLabelText, proportion=1, flag=wx.EXPAND)

        selLogTxtBox = wx.BoxSizer(wx.HORIZONTAL)
        availLogText = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(160, 250))
        selLogTxtBox.Add(availLogText, proportion=1, flag=wx.EXPAND)

        canvasOrganizer.Add(availLogLabelTxtBox)
        canvasOrganizer.Add((30,10))
        canvasOrganizer.Add(selLogTxtBox)

        vertOrganizer.Add(canvasOrganizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        buttonOrganizer = wx.BoxSizer(wx.HORIZONTAL)
        opnLogFolderBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        opnLogFolderBtn = wx.Button(panel, label='Open Log Folder', size=(162, 50))
        opnLogFolderBtnBox.Add(opnLogFolderBtn, flag= wx.LEFT, border=8)  # wx.TOP | wx.CENTER | wx.BOTTOM
        viewLogBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        viewLogBtn = wx.Button(panel, label='View Log', size=(162, 50))
        viewLogBtnBox.Add(viewLogBtn, flag= wx.LEFT, border=27)  # wx.CENTER | wx.BOTTOM

        buttonOrganizer.Add((1, 50))
        buttonOrganizer.Add(opnLogFolderBtnBox)
        buttonOrganizer.Add((1, 20))
        buttonOrganizer.Add(viewLogBtnBox)

        vertOrganizer.Add((-1, 10))
        vertOrganizer.Add(buttonOrganizer)

        vertOrganizer.Add((-1, 10))

        panel.SetSizer(vertOrganizer)
        panel.Show()

def ProfileCreationUI(evt):

        panel = wx.Frame(None,-1)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)


        vertOrganizer = wx.BoxSizer(wx.VERTICAL)

        connectionTypeBox = wx.BoxSizer(wx.HORIZONTAL)
        connectionTypeBox.Add((10,10))
        connectionTypeLabel = wx.StaticText(panel, label='Connection Type')
        connectionTypeLabel.SetFont(font)
        connectionTypeBox.Add(connectionTypeLabel)
        connectionType = wx.BoxSizer(wx.HORIZONTAL)
        connectionType.Add((49,10))
        connection = wx.TextCtrl(panel, size=(162, 25))
        connectionType.Add(connection)
        connectionTypeBox.Add(connectionType)
        vertOrganizer.Add(connectionTypeBox, flag= wx.TOP, border=20)

        vertOrganizer.Add((-1, 1))

        routerModelBox = wx.BoxSizer(wx.HORIZONTAL)
        routerModelBox.Add((10,10))
        model = wx.StaticText(panel, label='Router Model')
        model.SetFont(font)
        routerModelBox.Add(model)
        statusBox = wx.BoxSizer(wx.HORIZONTAL)  #still needs refactoring
        statusBox.Add((70,10))
        status = wx.TextCtrl(panel, size=(162, 25))
        statusBox.Add(status)
        routerModelBox.Add(statusBox)
        vertOrganizer.Add(routerModelBox, flag= wx.TOP, border=20)

        vertOrganizer.Add((-1, 1))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add((10,10))
        st2 = wx.StaticText(panel, label='Firmware Version ID')
        st2.SetFont(font)
        hbox1.Add(st2)
        statusBox = wx.BoxSizer(wx.HORIZONTAL)
        statusBox.Add((26,10))
        status = wx.TextCtrl(panel, size=(162, 25))
        statusBox.Add(status)
        hbox1.Add(statusBox)
        vertOrganizer.Add(hbox1, flag= wx.TOP, border=20)

        vertOrganizer.Add((-1, 1))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add((10,10))
        st2 = wx.StaticText(panel, label='Firmware File Location')
        st2.SetFont(font)
        hbox1.Add(st2)
        statusBox = wx.BoxSizer(wx.HORIZONTAL)
        statusBox.Add((10,10))
        status = wx.TextCtrl(panel, size=(162, 25))
        statusBox.Add(status)
        hbox1.Add(statusBox)
        vertOrganizer.Add(hbox1, flag= wx.TOP, border=20)

        vertOrganizer.Add((-1, 20))

        updateBtnBox = wx.BoxSizer(wx.HORIZONTAL)
        updateBtn = wx.Button(panel, label='Create Profile', size=(162, 48))
        updateBtnBox.Add(updateBtn, flag= wx.LEFT | wx.RIGHT, border=117)  # wx.CENTER | wx.BOTTOM

        vertOrganizer.Add(updateBtnBox)

        panel.SetSizer(vertOrganizer)
        panel.Show()

if __name__ == '__main__':  # if this file is 'main', run the following statements

    app = wx.App(redirect = False)  # Create a new wx App called 'app'
    MainMenu(None, title='FirmWhere: Main Menu')    # call the main menu class, pass the title 'Firmwhere: Main Menu' to the init function
    app.MainLoop()  # begin reveiving and processing user inputs
