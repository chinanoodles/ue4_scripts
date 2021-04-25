import ueAssets as uelib
reload(uelib)

def output(output_path):
	my_lib = uelib.hex_assets()
	print my_lib
	
	#my_lib.setOutPutPath("G:\\")

	#print my_lib.output_path
	#my_lib.setJsonName("tst.json")
	#my_lib.setCsvName("tst.csv")

	my_lib.getSelectedAssets()
	my_lib.setData()

	my_lib.exportJson(output_path)
	#my_lib.exportCsv(output_path)
