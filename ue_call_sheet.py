import ueAssets as uelib
reload(uelib)

def output(callsheet_path,fbx_path):
	my_lib = uelib.hex_assets()
	print my_lib
	
	#my_lib.setOutPutPath("G:\\")

	#print my_lib.callsheet_path
	#my_lib.setJsonName("tst.json")
	#my_lib.setCsvName("tst.csv")

	my_lib.getSelectedAssets()

	my_lib.setCallsheetPath(callsheet_path)
	my_lib.setfbxPath(fbx_path)
	my_lib.setData()

	my_lib.exportJson()
	my_lib.exportMyAssets()

	print "finished :{fbxpath}".format(fbxpath = my_lib.fbx_path )
	#my_lib.exportCsv(callsheet_path)
