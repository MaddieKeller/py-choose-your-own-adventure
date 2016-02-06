import wx
import db_connect

class GUIWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, None, title="Choose your own Adventure", size=(900,600))
        self.pathDictionary = kwargs
        self.currentPath = list()
        for a in args:
            self.currentPath.append(a)

        print(self.currentPath, self.pathDictionary)
        #create panel
        panel = wx.Panel(self)

        #***** MENU **********

        #create menu
        menuBar = wx.MenuBar()

        #Create a Quit Menu and quit button
        quitMenuButton = wx.Menu()
        quitMenuItem = wx.MenuItem(quitMenuButton,wx.ID_EXIT,'QUIT\tCtrl+Q')
        quitMenuButton.AppendItem(quitMenuItem)


        menuBar.Append(quitMenuButton, '&QUIT') #append the quit menu to the menu bar

        self.SetMenuBar(menuBar) #put the menu bar on the window

        #Bind actions to the menu bar
        self.Bind(wx.EVT_MENU, self.Quit, quitMenuItem)


        #********STATS************
        statBox = wx.StaticBox(panel,
                               label="Stats",
                               pos=(3,3),
                               size=(145,145))
        wx.StaticText(statBox,
                      label="Name:",
                      pos=(10,25))
        wx.StaticText(statBox,
                      label=self.pathDictionary["nameSt"],
                      pos=(65,25))
        wx.StaticText(statBox,
                      label="Life:",
                      pos=(10,50))
        self.lifeInd = wx.TextCtrl(statBox,
                                   value=str(self.pathDictionary["life"]),
                                   pos=(65,50),
                                   size=(50,20),
                                   style=wx.TE_READONLY)
        wx.StaticText(statBox,
                      label="Gold:",
                      pos=(10,75))
        self.goldInd = wx.TextCtrl(statBox,value=str(
                                   self.pathDictionary["gold"]),
                                   pos=(65,75),
                                   size=(50,20),
                                   style=wx.TE_READONLY)
        wx.StaticText(statBox,
                      label="Class:",
                      pos=(10,100))
        self.classInd = wx.TextCtrl(statBox,
                                    value = self.pathDictionary["classAns"],
                                    pos = (65,100),
                                    size = (50,20),
                                    style = wx.TE_READONLY)
        wx.StaticText(statBox,
                      label="Race:",
                      pos=(10,125))
        self.raceInd = wx.TextCtrl(statBox,
                                   value=self.pathDictionary["raceAns"],
                                   pos=(65,125),
                                   size=(50,20),
                                   style=wx.TE_READONLY)

        self.adventureText = wx.TextCtrl(panel,
                                         value=self.pathDictionary["advText"],
                                         pos=(150,3),
                                         size=(700,300),
                                         style=wx.TE_READONLY | wx.TE_MULTILINE)

        choiceABox = wx.StaticBox(panel,
                                  id=1,
                                  label="",
                                  pos=(150,305),
                                  size=(700,70))
        choiceA = wx.Button(choiceABox,
                            label="Choose A",
                            pos=(600,30))
        self.choiceAText = wx.TextCtrl(choiceABox,
                                       value=self.pathDictionary["afill"],
                                       pos=(10,10),
                                       size=(590,60),
                                       style=wx.TE_READONLY | wx.TE_MULTILINE)
        choiceA.Bind(wx.EVT_BUTTON, lambda evt,temp=1: self.selectMade(evt, temp))

        choiceBBox = wx.StaticBox(panel,
                                  id=2,
                                  label="",
                                  pos=(150,375),
                                  size=(700,70))
        choiceB = wx.Button(choiceBBox,
                            label="Choose B",
                            pos=(600,30))
        self.choiceBText = wx.TextCtrl(choiceBBox,
                                       value=self.pathDictionary["bfill"],
                                       pos=(10,10),
                                       size=(590,60),
                                       style=wx.TE_READONLY | wx.TE_MULTILINE)
        choiceB.Bind(wx.EVT_BUTTON, lambda evt, temp=2: self.selectMade(evt, temp))

        choiceCBox = wx.StaticBox(panel,
                                  id=3,
                                  label="",
                                  pos=(150,445),
                                  size=(700,70))
        choiceC = wx.Button(choiceCBox,
                            label="Choose C",
                            pos=(600,35))
        self.choiceCText = wx.TextCtrl(choiceCBox,
                                       value=self.pathDictionary["cfill"],
                                       pos=(10,10),
                                       size=(590,60),
                                       style=wx.TE_READONLY |wx.TE_MULTILINE)
        choiceC.Bind(wx.EVT_BUTTON,lambda evt, temp=3: self.selectMade(evt, temp))

        self.Centre()
        self.Show()

    def Quit(self, e):
        self.Close()

    def Save(self, e):
        pass
        #later link to database

    def selectMade(self, event, chosenPath,):
        self.currentPath.append(chosenPath)
        self.pathDictionary = db_connect.getPath(*self.currentPath, **self.pathDictionary)

        self.adventureText.SetValue(self.pathDictionary["advText"])
        self.choiceAText.SetValue(self.pathDictionary["afill"])
        self.choiceBText.SetValue(self.pathDictionary["bfill"])
        self.choiceCText.SetValue(self.pathDictionary["cfill"])


def initialSetup():
    #********INITIAL SETUP*********
    dlg = wx.MessageDialog(None, "This is a choose your own adventure game. Before we get started we'll need to set up your character","Welcome!",wx.OK_DEFAULT)
    dlg.ShowModal()
    dlg.Destroy()

    raceChoice = wx.SingleChoiceDialog(None,"CHOOSE YOUR RACE:","RACE",["Human","Elf","Dwarf"])
    if raceChoice.ShowModal()==wx.ID_OK:
        raceAnswer=raceChoice.GetStringSelection()
    else:
        raceAnswer = "Human"

    classChoice = wx.SingleChoiceDialog(None,"CHOOSE YOUR CLASS:","CLASS",
                                    ["Fighter","Wizard","Rogue","Priest"])
    if classChoice.ShowModal()==wx.ID_OK:
        classAnswer = classChoice.GetStringSelection()
    else:
        classAnswer="Fighter"

    nameDialog = wx.TextEntryDialog(None,"Finally, what is your character's name?","NAME")
    if nameDialog.ShowModal() == wx.ID_OK:
        nameSet = nameDialog.GetValue()
    else:
        nameSet = "Bob"

    #call to the choose your own adventure to get starting path settings
    pathDictionary = db_connect.getPath(0, nameSt = nameSet, raceAns=raceAnswer,classAns=classAnswer)
    print (pathDictionary)
    GUIWindow(0, **pathDictionary)


def main():
    app = wx.App() #initialize the application
    initialSetup()
    app.MainLoop() #tells wx app to start its loop

if __name__ == '__main__': main()
