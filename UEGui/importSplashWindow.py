import importSplashUI as splashUI
reload(splashUI)

if __name__ == "__main__":
	import sys
	import threading

	try:
		app = splashUI.QtGui.QApplication(sys.argv)
	except:
	    app = splashUI.QtCore.QCoreApplication.instance()


	app.setQuitOnLastWindowClosed(False)

	importAssetsDialog = splashUI.Ui_MainWindow()
	importAssetsDialog.setupUi()
	importAssetsDialog.MainWindow.show()

	
	t = threading.Thread(target = lambda: app.exec_())
	t.daemon = True
	
	#t.start()



	print ("App freezes the main process!" )
	
