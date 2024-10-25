from PyQt5.QtWidgets import*
from ui import*
import json 

app=QApplication([])
class MainNoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes={
            "Ласкаво просимо":
            {
            "текст":'Ласкаво просимо в найшій програмі!' ,
            "теги" : ["вітання","інструкція"] 
            }
          
        
        }
        self.ReadFile() 
        self.LoadNotes()
        
        self.ui.listView.clicked.connect(self.ShowNotes)
        self.ui.pushButton.clicked.connect(self.AddNote)
        self.ui.pushButton_3.clicked.connect(self.DeleteNotes)
        self.ui.pushButton_2.clicked.connect(self.SaveNote)
    def ReadFile(self):
        with open("notes.json","r") as file:
            self.notes=json.load(file)
            self.ui.listView.addItems(self.notes)
        print("файл прочитано")
    def LoadNotes(self):
        with open('notes.json','w') as file:
            json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
        print("Файл загружено")
    def ShowNotes(self):
        key = self.ui.listView.selectedItems()[0].text()
        self.ui.textEdit.setText(self.notes[key]['текст'])
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.notes[key]['теги'])
        print("Замітка обрана") 
    def AddNote(self):
        NoteName,Ok=QInputDialog.getText(ex,'Додати замітку', 'Назва замітку:')
        if Ok and NoteName !='':
            self.notes[NoteName]={'текст':'','теги':[]}
            self.ui.listView.addItem(NoteName)
            self.ui.listView.addItems(self.notes[NoteName]['теги'])
            with open('notes.json','w') as file:
                json.dump(self.notes,file,sort_keys=True,ensure_ascii=False)
            print(self.notes)
    def DeleteNotes(self):
        if self.ui.listView.selectedItems():
             key = self.ui.listView.selectedItems()[0].text()
             del self.notes[key]
             self.ui.listView.clear()
             self.ui.listWidget.clear()
             self.ui.textEdit.clear()
             self.ui.listView.addItems(self.notes)
             with open('notes.json','w') as file:
                json.dump(self.notes,file,sort_keys=True,ensure_ascii=False)
             print(self.notes)
        else:
            print("Замітка для видалення не вибрана")
    def SaveNote(self):
        if self.ui.listView.selectedItems():
             key = self.ui.listView.selectedItems()[0].text()
             self.notes[key]['текст'] = self.ui.textEdit.toPlainText()
             with open('notes.json','w') as file:
                json.dump(self.notes,file,sort_keys=True,ensure_ascii=False)
             print("Замітка збережена")





ex=MainNoteWindow()
ex.show()
app.exec_()