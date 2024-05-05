from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import QTextBrowser, QVBoxLayout
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport


class ConsoleWidget(RichJupyterWidget):

	def __init__(self, customBanner=None, *args, **kwargs):
		super(ConsoleWidget, self).__init__(*args, **kwargs)

		if customBanner is not None:
			self.banner = customBanner

		self.font_size = 6
		self.kernel_manager = kernel_manager = QtInProcessKernelManager()
		kernel_manager.start_kernel(show_banner=False)
		kernel_manager.kernel.gui = 'qt'
		self.kernel_client = kernel_client = self._kernel_manager.client()
		kernel_client.start_channels()

		def stop():
			kernel_client.stop_channels()
			kernel_manager.shutdown_kernel()
			guisupport.get_app_qt().exit()

		self.exit_requested.connect(stop)

	def push_vars(self, variableDict):
		"""
		Given a dictionary containing name / value pairs, push those variables
		to the Jupyter console widget
		"""
		self.kernel_manager.kernel.shell.push(variableDict)

	def clear(self):
		"""
		Clears the terminal
		"""
		self._control.clear()

		# self.kernel_manager

	def print_text(self, text):
		"""
		Prints some plain text to the console
		"""
		self._append_plain_text(text)

	def execute_command(self, command):
		"""
		Execute a command in the frame of the console widget
		"""
		self._execute(command, False)

class TextBrowser(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.textBrowser = None
		self.initUI()
		
	
	def initUI(self):
		# 创建QTextBrowser
		self.textBrowser = QTextBrowser()
		# 创建垂直布局管理器
		layout = QVBoxLayout()
		
		# 将QTextBrowser添加到布局管理器
		layout.addWidget(self.textBrowser)
		
		# 设置布局管理器为QWidget的布局
		self.setLayout(layout)
		
		# 设置QWidget的窗口标题和大小
		self.setGeometry(100, 100, 800, 600)
		self.textBrowser.append("交互控制台")
		
		#设置字体大小
		self.textBrowser.setFontPointSize(12)
		
if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	widget = ConsoleWidget()
	widget.show()
	app.exec_()