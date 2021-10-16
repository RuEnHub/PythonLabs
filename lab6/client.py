from PyQt5.QtWidgets import QMainWindow, QApplication
import gui
import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 8080)
print('Подключено к {} порт {}'.format(*address))
sock.connect(address)


class Main(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.Func)

    def Func(self):
        mess = self.text1.toPlainText()
        if mess:
            message = mess.encode()
            sock.sendall(message)

            data = sock.recv(512)
            mess = data.decode()
            self.text2.setText(mess)
        else:
            self.text2.setText("")


app = QApplication(sys.argv)
form = Main()
form.show()
app.exec()
