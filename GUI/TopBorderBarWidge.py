from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
from GUI.RibbonTab import RibbonTab
from GUI import gui_scale
from GUI.StyleSheets import get_stylesheet
from PyQt5 import  QtWidgets,QtCore,QtGui,Qt

__author__ = 'loujiand'

from GUI.TittleBarButton import TittleBarButton,TittleBarButton_windown


class TopBorderBarWidget(QToolBar):
	def __init__(self, parent):
		QToolBar.__init__(self, parent)
		self.parent=parent
		self.setStyleSheet(get_stylesheet("ribbon"))
		self.setObjectName("TittleWidget")
		self.setWindowTitle("Tittle")
		self._Tittle_widget = QtWidgets.QWidget(self)
		self._Tittle_widget.setMaximumHeight(37)
		self._Tittle_widget.setMinimumHeight(37)
		self.setMovable(False)
		self.addWidget(self._Tittle_widget)
		#self.setStyleSheet("background-color: rgb(14, 162, 185);")
		
		self.HBOX_LeftlLayoutWidget = QtWidgets.QWidget(self._Tittle_widget)
		self.HBOX_LeftlLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 40))
		self.HBOX_LeftlLayoutWidget.setObjectName("HBOX_LeftlLayoutWidget")
		
		HBOX=QHBoxLayout()
		HBOX_Logo = QHBoxLayout()
		HBOX_Left=QHBoxLayout(self.HBOX_LeftlLayoutWidget)
		HBOX_Center = QHBoxLayout()
		HBOX_Right= QHBoxLayout()
		self._Tittle_widget.setLayout(HBOX)
		HBOX.addLayout(HBOX_Logo)
		HBOX.addLayout(HBOX_Left,0)
		HBOX.addLayout(HBOX_Center,280)
		HBOX.addLayout(HBOX_Right,0)
		#HBOX.setSpacing(500)
		
		#add logo-------------------------------------------------------------------------------------
		#self.logo_pushButton = QtWidgets.QPushButton(self._Tittle_widget)
		#self.logo_pushButton.setObjectName("logo_pushButton")
		
		#self.logo_pushButton.setFlat(True)
		#icon = QtGui.QIcon()
		#icon.addPixmap(QtGui.QPixmap("icons/logo-no-background.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		#self.logo_pushButton.setIcon(icon)
		#self.logo_pushButton.setIconSize(QtCore.QSize(30, 30))
		#HBOX_Logo.addWidget(self.logo_pushButton, 0, QtCore.Qt.AlignVCenter)
		
		#add open file
		#self.menu_pushButton = TittleBarButton(self._Tittle_widget, "folder_pushButton", "folder", [20, 20],"打开",parent.OCAF.Open_part)
		#HBOX_Left.addWidget(self.menu_pushButton, 50)

		#select combobox--------------------------------------------------------------------------------------
		self.select_combobox = QtWidgets.QComboBox()
		self.select_combobox.addItem("无选择过滤器")
		self.select_combobox.addItem("坐标系")
		self.select_combobox.addItem("基准")
		self.select_combobox.addItem("曲线特性")
		self.select_combobox.addItem("点")
		self.select_combobox.addItem("特性")
		self.select_combobox.addItem("视图")
		HBOX_Left.addWidget(self.select_combobox,50)
		# select combobox--------------------------------------------------------------------------------------
		self.select_model_combobox = QtWidgets.QComboBox()
		self.select_model_combobox.addItem("整个装配")
		self.select_model_combobox.addItem("在工作部件和组件内")
		self.select_model_combobox.addItem("仅在工作部件内")
		HBOX_Left.addWidget(self.select_model_combobox, 50)

		#--------------------------------------------------------------------------------------------------
		print(self.parent.current_window_name)
		#add open file
		self.folder_pushButton = TittleBarButton(parent, "folder_pushButton", "view_top", [32, 32],"打开",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Top)
		HBOX_Left.addWidget(self.folder_pushButton, 0)
		#add undo--------------------------------------------------------------------------------------
		self.undo_pushButton = TittleBarButton(parent,"undo_pushButton","view_tfr_tri",[32,32],"撤销",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Rear)
		HBOX_Left.addWidget(self.undo_pushButton,0)
		#add redo---------------------------------------------------------------------------------------------
		self.redo_pushButton = TittleBarButton(parent,"redo_pushButton","view_tfr_iso",[32,32],"重做",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Iso)
		HBOX_Left.addWidget(self.redo_pushButton, 0)
		#add save------------------------------------------------------------------------------------------------
		self.save_pushButton = TittleBarButton(parent,"save_pushButton","view_right",[32,32],"保存",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Right)
		HBOX_Left.addWidget(self.save_pushButton, 0)
		#add copy
		self.copy_pushButton = TittleBarButton(parent, "copy_pushButton", "view_left", [32, 32],"复制",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Left)
		HBOX_Left.addWidget(self.copy_pushButton, 0)
		#add paste
		self.paste_pushButton = TittleBarButton(parent, "paste_pushButton", "view_front", [32, 32],"黏贴",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Front)
		HBOX_Left.addWidget(self.paste_pushButton, 0)
		# add about
		self.about_pushButton = TittleBarButton(parent, "about_pushButton", "view_bottom", [32, 32],"关于",
			self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Bottom)
		HBOX_Left.addWidget(self.about_pushButton, 0)
		
		

	def add_ribbon_tab(self, name):
		ribbon_tab = RibbonTab(self, name)
		ribbon_tab.setObjectName("tab_" + name)
		self._ribbon_widget.addTab(ribbon_tab, name)
		return ribbon_tab
	
	def set_active(self, name):
		self.setCurrentWidget(self.findChild("tab_" + name))