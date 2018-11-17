import sys
import random
from main import addTestData, deleteTestData, createStructure
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import datetime


# create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Test Data Generator')
w.resize(320, 240)
w.setFixedSize(800, 460)

w.setStyleSheet("background-color: white;")


class QProgBar(QProgressBar):

    value = 0

    @pyqtSlot()
    def increaseValue(progressBar):
        progressBar.setValue(progressBar.value)
        progressBar.value = progressBar.value+1

# Create progressBar
bar = QProgBar(w)
bar.resize(320,30)
bar.setValue(0)
bar.move(460,400)


# Labels
lName = QLabel(w)
lLastName = QLabel(w)
lLevel = QLabel(w)
lArea = QLabel(w)
lSalary = QLabel(w)
lGrade = QLabel(w)

lName.setText("Name")
lName.move(60,60)
lLastName.setText("Last Name")
lLastName.move(220,60)
lLevel.setText("Level")
lLevel.move(70,230)
lArea.setText("Area")
lArea.move(210,230)
lSalary.setText("Salary")
lSalary.move(450,60)
lGrade.setText("Grade")
lGrade.move(660,60)

# Action buttons
btnDelete = QPushButton('Delete Test Data', w)
btnLoad = QPushButton('Load Test Data', w)
btnStructure = QPushButton('Create Structure', w)

# Comboboxes
schema = QComboBox(w)
schema.addItem("Test Schema")
schema.addItem("Dev Schema")
schema.move(200,10)
schema.resize(120,25)

# TextBoxes
database = QLineEdit(w)
database.move(30, 10)
database.resize(120,25)
database.setPlaceholderText("DB Name")

# Checkboxes
name1 = QCheckBox('Name 1', w)
name1.move(30, 85)
name1.setChecked(True)
name2 = QCheckBox('Name 2', w)
name2.move(30, 115)
name3 = QCheckBox('Name 3', w)
name3.move(30, 145)
name4 = QCheckBox('Name 4', w)
name4.move(30, 175)

lastName1 = QCheckBox('Last Name 1', w)
lastName1.move(200, 85)
lastName1.setChecked(True)
lastName2 = QCheckBox('Last Name 2', w)
lastName2.move(200, 115)
lastName3 = QCheckBox('Last Name 3', w)
lastName3.move(200, 145)
lastName4 = QCheckBox('Last Name 4', w)
lastName4.move(200, 175)

level1 = QCheckBox('1', w)
level1.move(30, 255)
level1.setChecked(True)
level2 = QCheckBox('2', w)
level2.move(30, 285)
level3 = QCheckBox('3', w)
level3.move(30, 315)
level4 = QCheckBox('4', w)
level4.move(30, 345)

area1 = QCheckBox('QA', w)
area1.move(200, 255)
area1.setChecked(True)
area2 = QCheckBox('DEV Back', w)
area2.move(200, 285)
area3 = QCheckBox('DEVOPS', w)
area3.move(200, 315)
area4 = QCheckBox('DEV Front', w)
area4.move(200, 345)

# TextBoxes
salary = QLineEdit(w)
salary.move(380, 85)
salary.resize(170,25)
salary.setPlaceholderText("10000")

grade = QLineEdit(w)
grade.move(600, 85)
grade.resize(170,25)
grade.setPlaceholderText("8")

# Create the actions
@pyqtSlot()
def on_click_loadData():
    bar.setValue(25)
    levelList = []
    areaList = []
    nameList = []
    lastNameList = []

    db = str(database.text())
    Salary = str(salary.text())
    Grade = str(grade.text())

    if(area1.isChecked()==True):
       areaList.append("QA")
    if(area2.isChecked()==True):
       areaList.append("DEV Back")
    if(area3.isChecked()==True):
       areaList.append("DEVOPS")
    if(area4.isChecked()==True):
       areaList.append("Dev Front")
    if(len(areaList)>0):
       Area = str(areaList[randomValueGenerator(len(areaList))-1])

    if(level1.isChecked()==True):
       levelList.append("1")
    if(level2.isChecked()==True):
       levelList.append("2")
    if(level3.isChecked()==True):
       levelList.append("1")
    if(level4.isChecked()==True):
       levelList.append("2")
    if(len(levelList)>0):
       Level = str(levelList[randomValueGenerator(len(levelList))-1])

    if(name1.isChecked()==True):
        nameList.append("Name 1")
    if(name2.isChecked()==True):
        nameList.append("Name 2")
    if(name3.isChecked()==True):
        nameList.append("Name 3")
    if(name4.isChecked()==True):
        nameList.append("Name 4")
    if(len(nameList)>0):
        Name = str(nameList[randomValueGenerator(len(nameList))-1])

    if(lastName1.isChecked()==True):
        lastNameList.append("Last Name 1")
    if(lastName2.isChecked()==True):
        lastNameList.append("Last Name 2")
    if(lastName3.isChecked()==True):
        lastNameList.append("Last Name 3")
    if(lastName4.isChecked()==True):
        lastNameList.append("Last Name 4")
    if(len(lastNameList)>0):
        LastName = str(lastNameList[randomValueGenerator(len(lastNameList))-1])


    bar.setValue(50)
    if(str(schema.currentText())=='Test Schema'):
       addTestData(db, 'Test', Name, LastName, Level, Area, Salary, Grade)
    elif(str(schema.currentText())=='Dev Schema'):
       addTestData(db, 'dbo', Name, LastName, Level, Area, Salary, Grade)
       bar.setValue(75)
    bar.setValue(100)

def on_click_deleteData():
    bar.setValue(25)
    db = str(database.text())
    bar.setValue(50)
    if(str(schema.currentText())=='Test Schema'):
       deleteTestData(db, 'Test')
    elif(str(schema.currentText())=='Dev Schema'):
       deleteTestData(db, 'dbo')
    print('Test data deleted')
    bar.setValue(75)
    bar.setValue(100)

def on_click_createStructure():
    bar.setValue(25)
    bar.setValue(50)
    db = str(database.text())
    if(str(schema.currentText())=='Test Schema' and db != ''):
       createStructure(db)
    print('Structure created')
    bar.setValue(75)
    bar.setValue(100)

def randomValueGenerator(len):
    return random.randint(1,len)

# connect the signals to the slots
btnStructure.clicked.connect(on_click_createStructure)
btnStructure.move(20, 400)
btnStructure.resize(120,30)

btnLoad.clicked.connect(on_click_loadData)
btnLoad.move(160, 400)
btnLoad.resize(120,30)

btnDelete.clicked.connect(on_click_deleteData)
btnDelete.move(300, 400)
btnDelete.resize(120,30)


# Show the window and run the app
w.show()
app.exec_()