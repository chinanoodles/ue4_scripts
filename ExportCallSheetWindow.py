from ExportCallSheetUi import *
if __name__ == "__main__":
	import sys
	import threading

	try:
		app = QtGui.QApplication(sys.argv)
	except:
	    app = QtCore.QCoreApplication.instance()

	
	ui = Ui_Dialog()
	ui.setupUi()
	ui.Dialog.show()
	t = threading.Thread(target = lambda: app.exec_())
	t.daemon = True
	#t.start()


	print "App freezes the main process!"
	