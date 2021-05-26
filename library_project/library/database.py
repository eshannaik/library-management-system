from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from PyQt5.QtWidgets import QMessageBox

def createDatabaseTable():

	createTable = QSqlQuery()
	return createTable.exec(
		"""
		CREATE TABLE IF NOT EXISTS library(
			id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
			title VARCHAR(100) NOT NULL,
			author VARCHAR(50) NOT NULL,
			status VARCHAR(100) NOT NULL
			)
		"""
	)

def createConnection(databaseName):
	connection = QSqlDatabase.addDatabase("QSQLITE")
	connection.setDatabaseName(databaseName)

	if not connection.open():
		QMessagebox.warning(
			"self",
			"Library",
			f"Database Error : {connection.lastError().text()}",
		)

		return False

	createDatabaseTable()
	return True
