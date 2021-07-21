from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_josephus_circle_ui import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # file = None
    # file_path = file[0]
    # file_suffix = file_path.split('.', 2)[1]   #后缀名