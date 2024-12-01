import sys
import sqlite3

from PyQt6 import QtWidgets, uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class Coffee(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.connection = sqlite3.connect('coffee.sqlite')
        self.model = None
        self.setupModel()
        self.populateTable()

        self.setFixedSize(self.size())

    def setupModel(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName('coffee.sqlite')

        self.model = QSqlTableModel(self)
        self.model.setTable("coffee")
        self.model.select()
        self.tableView.setModel(self.model)

    def populateTable(self):
        if self.model is not None:
            self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())
