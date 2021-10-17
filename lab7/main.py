from PyQt5.QtWidgets import QMainWindow, QApplication
import gui
import sys
import pymysql
con = pymysql.connect(host='localhost', user='root', password='root', database='car')
cur = con.cursor()


def intt(str):
        try:
            return int(str)
        except:
            return 0


class Main(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.Add)
        self.delBtn.clicked.connect(self.Del)
        cur.execute("SELECT maker.name, model, year, body_type.name, price FROM car "
                    "JOIN maker ON maker_id = maker.id "
                    "JOIN body_type ON body_type_id = body_type.id")
        cars = cur.fetchall()
        for car in cars:
            self.myList.addItem(f"{car[0]} {car[1]}, {car[2]} год, {car[3]} - {car[4]}$")


    def Add(self):
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
        cur.execute(
            "INSERT INTO `car` (`maker_id`, `model`, `year`, `body_type_id`, `price`) VALUES ("
            f"(SELECT id FROM maker WHERE name='{maker}'),"
            f"'{model}',"
            f"'{year}',"
            f"(SELECT id FROM body_type WHERE name='{body_type}'),"
            f"'{price}');")
        self.myList.addItem(f"{maker} {model}, {year} год, {body_type} - {price}$")
        con.commit()

    def Del(self):
        index = self.myList.currentRow()
        if index >= 0:
            cur.execute(f"DELETE FROM car WHERE id = "
                        f"(select id from (select id FROM `car` ORDER BY id LIMIT {index}, 1) x)")
            self.myList.takeItem(index)
            con.commit()


app = QApplication(sys.argv)
form = Main()
form.show()
app.exec()
