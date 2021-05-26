from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
	QWidget,
	QMainWindow,
	QHBoxLayout,
	QVBoxLayout,
	QPushButton,
	QLabel,
	QMessageBox,
	QDialog,
	QLineEdit,
	QFormLayout,
	QDialogButtonBox,
	QTableView,
	QAbstractItemView,
)
from .model import libraryModel

class window (QMainWindow):

	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle("Library Management System")
		self.resize(600,350)

		self.centralWidget=QWidget()
		self.setCentralWidget(self.centralWidget)

		self.setStyleSheet("background-image:url(D:/library.jpg) 0 0 0 0 stretch stretch")

		self.layout=QHBoxLayout()
		self.centralWidget.setLayout(self.layout)

		self.lmodel = libraryModel()

		self.setupUI()

	def setupUI(self):
		self.addButton = QPushButton("Add a Book")
		self.addButton.setStyleSheet("font: bold;color: red;font-size: 18px;height: 48px;width: 120px;")
		self.addButton.clicked.connect(self.addnew)

		self.deleteButton = QPushButton("Delete a Book")
		self.deleteButton.setStyleSheet("font: bold;color: red;font-size: 18px;height: 48px;width: 120px;")
		# self.deleteButton.clicked.connect(self.deletenew)

		self.viewButton = QPushButton("View all the Books")
		self.viewButton.setStyleSheet("font: bold;color: red;font-size: 18px;height: 48px;width: 120px;")
		self.viewButton.clicked.connect(self.viewall)

		self.issuebookButton = QPushButton("Issue a Book")
		self.issuebookButton.setStyleSheet("font: bold;color: red;font-size: 18px;height: 48px;width: 120px;")
		# self.issuebookButton.clicked.connect(self.issueone)

		self.returnbookButton = QPushButton("Return a Book")
		self.returnbookButton.setStyleSheet("font: bold;color: red;font-size: 18px;height: 48px;width: 120px;")
		# self.returnbookButton.clicked.connect(self.returnone)


		# l = QVBoxLayout()
		# l.addWidget(self.addButton)
		# self.layout.addLayout(l)

		layout = QVBoxLayout()
		layout.addWidget(self.addButton)
		layout.addWidget(self.deleteButton)
		layout.addWidget(self.viewButton)
		layout.addWidget(self.issuebookButton)
		layout.addWidget(self.returnbookButton)

		self.layout.addLayout(layout)

	def addnew(self):
		dialog = AddDialog(self)

		if dialog.exec() == QDialog.Accepted:
			self.lmodel.addBook(dialog.data)
			self.table.resizeColumnsToContent()

	# def deletenew(self):
	# 	row=self.table.currentIndex().row()

	# 	if row<0:
	# 		return

	# 	messagebox = QMessageBox.warning(
	# 		self,
	# 		"Warning",
	# 		"Are you sure you want to delete this book?",
	# 		QMessageBox.Ok | QMessageBox.Cancel
	# 	)

	# 	if messagebox == QMessageBox.Ok:
	# 		self.lmodel.deleteBook(row)

	def viewall(self):
		ViewDialog()
		pass

	# def issueone(self):
	# 	row = self.table.currentIndex().row()

	# 	if row<0:
	# 		return

	# 	dialog = IssueDialog(self)

	# 	if dialog.exec() == QDialog.Accepted:
	# 		self.lmodel.issueBook(dialog.data)

	# def returnone(self):

	# 	pass

#window for adding a book
class AddDialog(QDialog):

	def __init__(self,parent=None):
		super().__init__(parent=parent)

		self.setWindowTitle("Add Book")
		self.layout=QVBoxLayout()
		self.setLayout(self.layout)
		self.data=None

		self.setupUI()

	def setupUI(self):
		self.title = QLineEdit()
		self.title.setObjectName("Title")
		self.author = QLineEdit()
		self.author.setObjectName("Author Name")
		self.status = QLineEdit()
		self.status.setObjectName("Status")

		layout = QFormLayout()
		layout.addRow("Title :",self.title)
		layout.addRow("Author Name :",self.author)
		layout.addRow("Status :",self.status)
		self.layout.addLayout(layout)

		self.buttonBox = QDialogButtonBox(self)
		self.buttonBox.setOrientation(Qt.Horizontal)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		self.layout.addWidget(self.buttonBox)

	def accept(self):
		self.data =[]

		for f in (self.title,self.author,self.status):
			if not field.text():
				QMessageBox.critical(
					self,
					"Error!",
					f"You must provide contact's {field.objectName()}",
				)

				self.data = None
				return
			self.data.append(field.data())

		if not self.data:
			return

		super().accept()


# View the Table
class ViewDialog(QDialog):

	def __init__(self,parent=None):
		super().__init__(parent=parent)
		self.setWindowTitle("List of Books")
		self.resize(500,300)

		self.layout=QHBoxLayout()
		self.centralWidget.setLayout(self.layout)

		self.lmodel = libraryModel()

	def setupUI(self):
		self.table = QTableView()
		self.table.setModel(self.lmodel.model)
		self.table.setSlectionBehaviour(QAbstractItemView.SelectRows)

		self.layout.addWidget(self.layout)


# #Window for issuing a book
# def IssueDialog(QDialog):

# 	def __init__(self,parent=None):
# 		super().__init__(parent=parent)

# 		self.setWindowTitle("Issue a Book")
# 		self.layout=QVBoxLayout()
# 		self.setLayout(self.layout)
# 		self.data=None

# 		setupUI()

# 	def setupUI(self):
# 		self.title = QLineEdit()
# 		self.title.setObjectName("Title")

# 		layout = QFormLayout()
# 		layout.addRow("Title :",self.title)
# 		self.layout.setLayout(layout)

# 		self.buttonBox = QDialogButtonBox(self)
# 		self.buttonBox.setOrientation(Qt.Horizontal)
# 		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
# 		self.buttonBox.accepted.connect(self.accept)
# 		self.buttonBox.rejected.connect(self.reject)
# 		self.layout.addWidget(self.buttonBox)

# 	def accept(self):
# 		self.data =[]

# 		for f in self.title:
# 			if not field.text():
# 				QMessageBox.critical(
# 					self,
# 					"Error!",
# 					f"You must provide contact's {field.objectName()}",
# 				)

# 				self.data = None
# 				return
# 			self.data.append(field.data())

# 		if not self.data:
# 			return

# 		super().accept()


# def ReturnDialog(QDialog):

# 	def __init__(self,parent=None):
# 		super().__init__(parent=parent)

# 		self.setWindowTitle("Return a Book")
# 		self.layout=QVBoxLayout()
# 		self.setLayout(self.layout)
# 		self.data=None

# 		setupUI()

# 	def setupUI(self):
# 		self.title = QLineEdit()
# 		self.title.setObjectName("Title")

# 		layout = QFormLayout()
# 		layout.addRow("Title :",self.title)
# 		self.layout.setLayout(layout)

# 		self.buttonBox = QDialogButtonBox(self)
# 		self.buttonBox.setOrientation(Qt.Horizontal)
# 		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
# 		self.buttonBox.accepted.connect(self.accept)
# 		self.buttonBox.rejected.connect(self.reject)
# 		self.layout.addWidget(self.buttonBox)

# 	def accept(self):
# 		self.data =[]

# 		for f in self.title:
# 			if not field.text():
# 				QMessageBox.critical(
# 					self,
# 					"Error!",
# 					f"You must provide contact's {field.objectName()}",
# 				)

# 				self.data = None
# 				return
# 			self.data.append(field.data())

# 		if not self.data:
# 			return

# 		super().accept()
