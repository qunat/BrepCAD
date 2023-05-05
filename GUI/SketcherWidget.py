# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Process_message_word.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout


class SketcherWidget(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(SketcherWidget, self).__init__(parent)
		self.parent=parent
		self.setupUi()
		x = parent.geometry().x() + parent.geometry().width() / 2
		y = parent.geometry().y() + parent.geometry().height() / 2
		self.setGeometry(x, y, 250, 80)
		self.setWindowTitle('创建草图')
		self.pushbutton_ok.clicked.connect(self.ok)
		self.pushbutton_cancel.clicked.connect(self.cancel)
		
		
	
	def setupUi(self):
		self.widget = QtWidgets.QWidget(self)
		#self.setMovable(False)
		#self.addWidget(self.widget)
		# self.setStyleSheet("background-color: rgb(14, 162, 185);")
		self.setCentralWidget(self.widget)
		HBOX = QVBoxLayout()
		HBOX_comboBOX=QVBoxLayout()
		HBOX_button = QHBoxLayout()
		self.widget.setLayout(HBOX)
		HBOX.addLayout(HBOX_comboBOX)
		HBOX.addLayout(HBOX_button)
		
		self.comboBox = QtWidgets.QComboBox(self.widget)
		self.comboBox.setGeometry(QtCore.QRect(80, 100, 221, 500))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("XY平面")
		self.comboBox.addItem("XZ平面")
		self.comboBox.addItem("YZ平面")
		HBOX_comboBOX.addWidget(self.comboBox,0, QtCore.Qt.AlignTop)
		
		self.pushbutton_ok=QtWidgets.QPushButton("确定")
		self.pushbutton_cancel = QtWidgets.QPushButton("取消")
		HBOX_button.addWidget(self.pushbutton_ok)
		HBOX_button.addWidget(self.pushbutton_cancel)
		self.statusBar().showMessage("请选择草绘平面")
	def ok(self):
		self.parent.Sketcher.uptoplane()
		self.close()
		
	def cancel(self):
		self.close()
		
	def Show(self):
		self.show()
