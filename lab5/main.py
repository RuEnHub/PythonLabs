from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QListWidget, QMessageBox
import gui
import sys


def intt(arg):
        try:
            return int(arg)
        except:
            return 0


class Car:
    def __init__(self, code, mark, model, year, body_type, price):
        self.code = code
        self.maker = mark
        self.model = model
        self.year = year
        self.body_type = body_type
        self.price = price

    def __str__(self):
        return f"{self.code}: {self.maker} {self.model}, {self.year} год, {self.body_type} - {self.price}$"


class Main(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.Add)
        self.delBtn.clicked.connect(self.Del)
        self.searchBtn.clicked.connect(self.Search)
        self.createMB.triggered.connect(self.Create)
        self.openMB.triggered.connect(self.Open)
        self.saveMB.triggered.connect(self.Save)
        self.saveAsMB.triggered.connect(self.SaveAs)
        self.exitMB.triggered.connect(lambda: sys.exit())
        self.infoMB.triggered.connect(lambda: info.show())

    def Add(self):
        code = intt(self.code.text())
        if self.radioButton_2.isChecked():
            maker = self.radioButton_2.text()
        elif self.radioButton.isChecked():
            maker = self.radioButton.text()
        else:
            maker = self.radioButton_3.text()
        model = self.model.text()
        year = intt(self.year.value())
        body_type = self.body_type.currentText()
        price = int(self.price.value())
        car = Car(code, maker, model, year, body_type, price)
        cars.append(car)
        self.myList.addItem(str(car))

    def Del(self):
        index = self.myList.currentRow()
        if index >= 0:
            cars.pop(index)
            self.myList.takeItem(index)

    def Search(self):
        w.resize(250, 150)
        w.clear()
        w.show()
        search_year = intt(self.year.value())
        for i in range(len(cars)):
            if cars[i].year == search_year:
                w.addItem(str(cars[i]))

    def Create(self):
        cars.clear()
        self.myList.clear()
        self.code.setText("")
        self.radioButton_2.setChecked(True)
        self.model.setText("")
        self.year.setValue(1990)
        self.body_type.setCurrentText("Седан")
        self.price.setValue(10000)

    def Open(self):
        print("open")

    def Save(self):
        print("save")

    def SaveAs(self):
        print("saveAs")


cars = []
app = QApplication(sys.argv)
form = Main()
w = QListWidget()
info = QMessageBox()
info.setText("Никулин")
form.show()
app.exec()
