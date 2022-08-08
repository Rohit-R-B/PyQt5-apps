from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_DialogOpenTeam(object):
    def setupUi(self, DialogOpenTeam):
        DialogOpenTeam.setObjectName("DialogOpenTeam")
        DialogOpenTeam.resize(214, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogOpenTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogOpenTeam)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.OpenTeam_comboBox = QtWidgets.QComboBox(DialogOpenTeam)
        self.OpenTeam_comboBox.setObjectName("OpenTeam_comboBox")
        self.verticalLayout.addWidget(self.OpenTeam_comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openTeamButton = QtWidgets.QPushButton(DialogOpenTeam)
        self.openTeamButton.setObjectName("openTeamButton")
        self.horizontalLayout.addWidget(self.openTeamButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogOpenTeam)
        QtCore.QMetaObject.connectSlotsByName(DialogOpenTeam)

    def retranslateUi(self, DialogOpenTeam):
        _translate = QtCore.QCoreApplication.translate
        DialogOpenTeam.setWindowTitle(_translate("DialogOpenTeam", "Dialog"))
        self.label.setText(_translate("DialogOpenTeam", "Select the team you want to open:"))
        self.openTeamButton.setText(_translate("DialogOpenTeam", "Open"))


class Ui_DialogSaveTeam(object):
    def setupUi(self, DialogSaveTeam):
        DialogSaveTeam.setObjectName("DialogSaveTeam")
        DialogSaveTeam.resize(319, 182)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSaveTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogSaveTeam)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveTeamButton = QtWidgets.QPushButton(DialogSaveTeam)
        self.saveTeamButton.setObjectName("saveTeamButton")
        self.horizontalLayout.addWidget(self.saveTeamButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogSaveTeam)
        QtCore.QMetaObject.connectSlotsByName(DialogSaveTeam)

    def retranslateUi(self, DialogSaveTeam):
        _translate = QtCore.QCoreApplication.translate
        DialogSaveTeam.setWindowTitle(_translate("DialogSaveTeam", "Dialog"))
        self.label.setText(_translate("DialogSaveTeam", "Do you want to save this team? "))
        self.saveTeamButton.setText(_translate("DialogSaveTeam", "Save"))

class Ui_DialogEvalTeam(object):
    def setupUi(self, DialogEvalTeam):
        DialogEvalTeam.setObjectName("DialogEvalTeam")
        DialogEvalTeam.resize(400, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEvalTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogEvalTeam)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.evaluateTeamsButton = QtWidgets.QPushButton(DialogEvalTeam)
        self.evaluateTeamsButton.setObjectName("evaluateTeamsButton")
        self.verticalLayout.addWidget(self.evaluateTeamsButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.displayBestTeam = QtWidgets.QLineEdit(DialogEvalTeam)
        self.displayBestTeam.setObjectName("displayBestTeam")
        self.verticalLayout.addWidget(self.displayBestTeam)

        self.retranslateUi(DialogEvalTeam)
        QtCore.QMetaObject.connectSlotsByName(DialogEvalTeam)

    def retranslateUi(self, DialogEvalTeam):
        _translate = QtCore.QCoreApplication.translate
        DialogEvalTeam.setWindowTitle(_translate("DialogEvalTeam", "Dialog"))
        self.label.setText(_translate("DialogEvalTeam", "The best team amongst the current teams is:"))
        self.evaluateTeamsButton.setText(_translate("DialogEvalTeam", "Evaluate teams"))


class Ui_DialogNewTeam(object):
    def setupUi(self, DialogNewTeam):
        DialogNewTeam.setObjectName("DialogNewTeam")
        DialogNewTeam.resize(276, 197)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogNewTeam)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.EnterNewTeam_lineEdit = QtWidgets.QLineEdit(DialogNewTeam)
        self.EnterNewTeam_lineEdit.setObjectName("EnterNewTeam_lineEdit")
        self.verticalLayout.addWidget(self.EnterNewTeam_lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createNewTeamButton = QtWidgets.QPushButton(DialogNewTeam)
        self.createNewTeamButton.setObjectName("createNewTeamButton")
        self.horizontalLayout.addWidget(self.createNewTeamButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogNewTeam)
        QtCore.QMetaObject.connectSlotsByName(DialogNewTeam)

    def retranslateUi(self, DialogNewTeam):
        _translate = QtCore.QCoreApplication.translate
        DialogNewTeam.setWindowTitle(_translate("DialogNewTeam", "Dialog"))
        self.label.setText(_translate("DialogNewTeam", "Enter new team name:"))
        self.createNewTeamButton.setText(_translate("DialogNewTeam", "Create new Team"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label1.setFont(font)
        self.Label1.setObjectName("Label1")
        self.horizontalLayout.addWidget(self.Label1)
        self.batLabel = QtWidgets.QLabel(self.centralwidget)
        self.batLabel.setObjectName("batLabel")
        self.horizontalLayout.addWidget(self.batLabel)
        self.Label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label3.setFont(font)
        self.Label3.setObjectName("Label3")
        self.horizontalLayout.addWidget(self.Label3)
        self.arLabel = QtWidgets.QLabel(self.centralwidget)
        self.arLabel.setObjectName("arLabel")
        self.horizontalLayout.addWidget(self.arLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Label2.setFont(font)
        self.Label2.setObjectName("Label2")
        self.horizontalLayout_4.addWidget(self.Label2)
        self.bwlLabel = QtWidgets.QLabel(self.centralwidget)
        self.bwlLabel.setObjectName("bwlLabel")
        self.horizontalLayout_4.addWidget(self.bwlLabel)
        self.Label4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Label4.setFont(font)
        self.Label4.setObjectName("Label4")
        self.horizontalLayout_4.addWidget(self.Label4)
        self.wkLabel = QtWidgets.QLabel(self.centralwidget)
        self.wkLabel.setObjectName("wkLabel")
        self.horizontalLayout_4.addWidget(self.wkLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.PtsAvLabel = QtWidgets.QLabel(self.centralwidget)
        self.PtsAvLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PtsAvLabel.setAutoFillBackground(True)
        self.PtsAvLabel.setObjectName("PtsAvLabel")
        self.horizontalLayout_2.addWidget(self.PtsAvLabel)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.PtsUsdLabel = QtWidgets.QLabel(self.centralwidget)
        self.PtsUsdLabel.setObjectName("PtsUsdLabel")
        self.horizontalLayout_2.addWidget(self.PtsUsdLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BAT_radioButton = QtWidgets.QRadioButton(self.centralwidget, toggled = lambda: self.buttonfunction())
        self.BAT_radioButton.setObjectName("BAT_radioButton")
        self.horizontalLayout_3.addWidget(self.BAT_radioButton)
        self.BWL_radioButton = QtWidgets.QRadioButton(self.centralwidget, toggled = lambda: self.buttonfunction())
        self.BWL_radioButton.setObjectName("BWL_radioButton")
        self.horizontalLayout_3.addWidget(self.BWL_radioButton)
        self.AR_radioButton = QtWidgets.QRadioButton(self.centralwidget, toggled = lambda: self.buttonfunction())
        self.AR_radioButton.setObjectName("AR_radioButton")
        self.horizontalLayout_3.addWidget(self.AR_radioButton)
        self.WK_radioButton = QtWidgets.QRadioButton(self.centralwidget, toggled = lambda: self.buttonfunction())
        self.WK_radioButton.setObjectName("WK_radioButton")
        self.horizontalLayout_3.addWidget(self.WK_radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.TeamNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.TeamNameLabel.setObjectName("TeamNameLabel")
        self.horizontalLayout_3.addWidget(self.TeamNameLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.list1 = QtWidgets.QListWidget(self.centralwidget, itemDoubleClicked = lambda: self.selectPlayer())
        self.list1.setObjectName("list1")
        self.horizontalLayout_6.addWidget(self.list1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.list2 = QtWidgets.QListWidget(self.centralwidget, itemDoubleClicked = lambda: self.removePlayer())
        self.list2.setObjectName("list2")
        self.horizontalLayout_6.addWidget(self.list2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.actionNew_Team.triggered.connect(lambda: self.menufunction("new"))
        self.actionSave_Team.triggered.connect(lambda: self.menufunction("save"))
        self.actionOpen_Team.triggered.connect(lambda: self.menufunction("open"))
        self.actionEvaluate_Team.triggered.connect(lambda: self.menufunction("evaluate"))

    def menufunction(self, action):

        if action == 'new':
            self.window = QtWidgets.QDialog()
            self.ui_new = Ui_DialogNewTeam()
            self.ui_new.setupUi(self.window)
            self.window.show() 

            self.ui_new.createNewTeamButton.clicked.connect(lambda: self.newfunction()) 

        if action == 'save':
            self.window = QtWidgets.QDialog()
            self.ui_save = Ui_DialogSaveTeam()
            self.ui_save.setupUi(self.window)
            self.window.show() 

            self.ui_save.saveTeamButton.clicked.connect(lambda: self.savefunction())

        if action == 'open':
            self.window = QtWidgets.QDialog()
            self.ui_open = Ui_DialogOpenTeam()
            self.ui_open.setupUi(self.window)
            self.window.show()
            
            conn = sqlite3.connect('Cricket_fantasy.db')
            cur = conn.cursor()

            sql='SELECT Team FROM teams'
            cur.execute(sql)
            teams=cur.fetchall()

            if len(teams) > 0:
                for team in teams:
                    self.ui_open.OpenTeam_comboBox.addItem(team[0])

                self.ui_open.openTeamButton.clicked.connect(lambda: self.openfunction())

            else:
                msg = QMessageBox()
                msg.setText("No saved teams")
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()


        if action == 'evaluate':
            self.window = QtWidgets.QDialog()
            self.ui_eval = Ui_DialogEvalTeam()
            self.ui_eval.setupUi(self.window)
            self.window.show()

            self.ui_eval.evaluateTeamsButton.clicked.connect(lambda: self.ui_eval.displayBestTeam.setText(self.evalfunction()))


    def newfunction(self):
        new_team_name=self.ui_new.EnterNewTeam_lineEdit.text()
        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()

        cur.execute('SELECT Team FROM teams')
        teams=cur.fetchall()

        if len(teams)>0:
            for team in teams:
                if new_team_name == team[0]:
                    msg = QMessageBox()
                    msg.setText("Team already exists with same name!")
                    msg.setIcon(QMessageBox.Critical)
                    x=msg.exec_()
                else:    
                    self.TeamNameLabel.setText(new_team_name)
                    self.list2.clear()
                    self.PtsUsdLabel.setText(f'0')
                    self.PtsAvLabel.setText(f'1000')
                    self.batLabel.setText(f'0')
                    self.bwlLabel.setText(f'0')
                    self.arLabel.setText(f'0')
                    self.wkLabel.setText(f'0')
        else:
            self.TeamNameLabel.setText(new_team_name)

    def savefunction(self):
        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()
        
        player_list=[]
        for index in range(self.list2.count()):
            player=self.list2.item(index)
            player_list.append(player.text())
        player_text=' '.join(player_list)

        points=0
        for player in player_list:
            sql='SELECT points FROM match where Player="'+player+'"'
            cur.execute(sql)
            pts=cur.fetchone()
            points+=int(pts[0])

        sql='SELECT Team FROM teams'
        cur.execute(sql)
        teams=cur.fetchall()
        teams_list=[]

        for team in teams:
            teams_list.append(team[0])

        if self.TeamNameLabel.text() in teams_list:
            cur.execute('DELETE FROM teams WHERE Team=(:team)',{'team':self.TeamNameLabel.text()})
            
        cur.execute('INSERT INTO teams(Team,Player,Points) VALUES((:team),(:players),(:pts))',{'team':self.TeamNameLabel.text(), 'players':player_text,'pts':points})
                
        msg = QMessageBox()
        msg.setText("Done")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()

        conn.commit()

    def openfunction(self):
        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()
        self.TeamNameLabel.setText(self.ui_open.OpenTeam_comboBox.currentText())        
        self.list2.clear()

        cur.execute('SELECT Player FROM teams WHERE Team = (:team)',{'team':self.TeamNameLabel.text()})
        players_tuple=cur.fetchone()
        players_str=players_tuple[0]
        players_list=players_str.split()

        currency_used=0
        bat=0
        bwl=0
        ar=0
        wk=0

        for player in players_list:
            self.list2.addItem(player)
            sql = 'SELECT role,value from stats WHERE player="'+player+'"'
            cur.execute(sql)
            role,value=cur.fetchone()
            currency_used+=value
            if role == 'BAT':
                bat+=1
            elif role == 'BWL':
                bwl+=1
            elif role == 'AR':
                ar+=1
            else:
                wk+=1

        self.PtsUsdLabel.setText(str(currency_used))
        self.PtsAvLabel.setText(str(1000-currency_used))
        self.batLabel.setText(str(bat))
        self.bwlLabel.setText(str(bwl))
        self.wkLabel.setText(str(wk))
        self.arLabel.setText(str(ar))


    def evalfunction(self):
        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()

        cur.execute('SELECT Team FROM teams WHERE points>= (SELECT max(points) from Teams)')
        best_team=cur.fetchone()

        return best_team[0]

    
    def buttonfunction(self):
        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()

        self.list1.clear()

        selected_list=[]

        for index in range(self.list2.count()):
            player=self.list2.item(index)
            selected_list.append(player.text())

        if self.BAT_radioButton.isChecked():
            #display all batters in db not in list 2
            cur.execute('Select player from stats where role="BAT"')
            bat=cur.fetchall()
            for batter in bat:
                if batter[0] not in selected_list:
                    self.list1.addItem(batter[0])

        if self.BWL_radioButton.isChecked():
            cur.execute('Select player from stats where role="BWL"')
            bowl=cur.fetchall()
            for bowler in bowl:
                if bowler[0] not in selected_list:
                    self.list1.addItem(bowler[0])

        if self.AR_radioButton.isChecked():
            cur.execute('Select player from stats where role="AR"')
            alr=cur.fetchall()
            for al_er in alr:
                if al_er[0] not in selected_list:
                    self.list1.addItem(al_er[0])

        if self.WK_radioButton.isChecked():
            cur.execute('Select player from stats where role="WK"')
            wks = cur.fetchall()
            for wicky in wks:
                if wicky[0] not in selected_list:
                    self.list1.addItem(wicky[0])


    def selectPlayer(self):
        selected_index = self.list1.currentRow()
        item = self.list1.takeItem(selected_index)
        name = item.text()

        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()

        sql =  'SELECT role,value from stats WHERE player="'+name+'"'
        cur.execute(sql)
        role,value = cur.fetchone()
        # print(name,player[0],player[1])
        wk_count = int(self.wkLabel.text())

        #check if the player is a wk
        if role=='WK' and wk_count>0:
            msg = QMessageBox()
            msg.setText("Cannot select more than 1 Wicket Keeper")
            msg.setIcon(QMessageBox.Critical)
            x=msg.exec_()
            self.list1.addItem(item)

        else:
            curr_avl=int(self.PtsAvLabel.text())
            #check for sufficient currency
            if int(value) > curr_avl:
                msg = QMessageBox()
                msg.setText("Insufficient currency")
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()
                self.list1.addItem(item)

            else:
                self.list2.addItem(item)

                curr_avl-=int(value)
                self.PtsAvLabel.setText(str(curr_avl))

                curr_usd=int(self.PtsUsdLabel.text())
                curr_usd+=int(value)
                self.PtsUsdLabel.setText(str(curr_usd))

                if role=='BAT':
                    num=int(self.batLabel.text())
                    num+=1
                    self.batLabel.setText(str(num))
                elif role=='BWL':
                    num=int(self.bwlLabel.text())
                    num+=1
                    self.bwlLabel.setText(str(num))
                elif role=='AR':
                    num=int(self.arLabel.text())
                    num+=1
                    self.arLabel.setText(str(num))
                else:
                    num=int(self.wkLabel.text())
                    num+=1
                    self.wkLabel.setText(str(num))


    def removePlayer(self):
        selected_index = self.list2.currentRow()
        item = self.list2.takeItem(selected_index)
        name = item.text()

        conn = sqlite3.connect('Cricket_fantasy.db')
        cur = conn.cursor()

        sql =  'SELECT role,value from stats WHERE player="'+name+'"'
        cur.execute(sql)
        role,value = cur.fetchone()

        curr_avl=int(self.PtsAvLabel.text())
        self.PtsAvLabel.setText("")
        self.PtsAvLabel.setText(str(curr_avl+int(value)))

        curr_usd=int(self.PtsUsdLabel.text())
        self.PtsUsdLabel.setText("")
        self.PtsUsdLabel.setText(str(curr_usd-int(value)))

        if role=='BAT':
            num=int(self.batLabel.text())
            num-=1
            self.batLabel.setText(str(num))
        elif role=='BWL':
            num=int(self.bwlLabel.text())
            num-=1
            self.bwlLabel.setText(str(num))
        elif role=='AR':
            num=int(self.arLabel.text())
            num-=1
            self.arLabel.setText(str(num))
        else:
            num=int(self.wkLabel.text())
            num-=1
            self.wkLabel.setText(str(num))

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dream 11"))
        self.label_5.setText(_translate("MainWindow", "Your Selections"))
        self.Label1.setText(_translate("MainWindow", "Batters (BAT) "))
        self.batLabel.setText(_translate("MainWindow", "0"))
        self.Label3.setText(_translate("MainWindow", "All Rounders (AR) "))
        self.arLabel.setText(_translate("MainWindow", "0"))
        self.Label2.setText(_translate("MainWindow", "Bowlers (BWL) "))
        self.bwlLabel.setText(_translate("MainWindow", "0"))
        self.Label4.setText(_translate("MainWindow", "Wicket Keeper (WK) "))
        self.wkLabel.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Currency Available"))
        self.PtsAvLabel.setText(_translate("MainWindow", "1000"))
        self.label_7.setText(_translate("MainWindow", "Currency used"))
        self.PtsUsdLabel.setText(_translate("MainWindow", "0"))
        self.BAT_radioButton.setText(_translate("MainWindow", "BAT"))
        self.BWL_radioButton.setText(_translate("MainWindow", "BWL"))
        self.AR_radioButton.setText(_translate("MainWindow", "AR"))
        self.WK_radioButton.setText(_translate("MainWindow", "WK"))
        self.label.setText(_translate("MainWindow", "Team Name"))
        self.TeamNameLabel.setText(_translate("MainWindow", "xyz"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
