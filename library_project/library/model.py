from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class libraryModel:

	def __init__(self):
		self.model = self.createTable()

	@staticmethod
	def createTable():
		tableModel = QSqlTableModel()
		tableModel.setTable("library")
		tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
		tableModel.select()

		headers = ("id","title","author","status")

		for c,h in enumerate(headers):
			tableModel.setHeaderData(c,Qt.Horizontal,h)

		return tableModel

	def addBook(self,data):
		row = self.model.rowCount()
		self.model.insertRows(row,1)

		for c,f in enumerate(data):
			self.model.setData(self.model.index(row,c+1),f)

		self.model.submitAll()
		self.model.select()

	def deleteBook(self,row):
		self.model.removeRow(row)
		self.model.submitAll()
		self.model.select()

	def issueBook(self,row):
		pass

	def returnBook(self,row):
		pass
