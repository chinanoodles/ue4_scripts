import unreal
import json,os
import csv

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False
class hex_assets:
	def __init__(self):
	    self.color = None
	    self.content = None
	    self.callsheet_path = None
	    self.fbx_path = None
	    self.csvData = None
	    self.jsonData = None
	    self.json_name = None
	    self.csv_name = None
	def setCallsheetPath(self,path):
		self.callsheet_path = path
	def setfbxPath(self,path):
		self.fbx_path = path
	def setJsonName(self,json_name):
		self.json_name = json_name
	def setCsvName(self,csv_name):
		self.csv_name = csv_name

	def getSelectedAssets(self):
		lib = unreal.EditorUtilityLibrary
		assets = lib.get_selected_assets()
		self.content = assets
		print self.content
	def getAssetsByPath(self,assets_path):
		asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
		assets = asset_reg.get_assets_by_path(assets_path)
		self.content = assets
	def setData(self):
		if self.content != None:
			self.jsonData = {}
			index = 0
			self.csvData = [["name","width","height","angle","depth"]]
			angle = -1
			for asset in self.content:
				if asset.get_class().get_name() =='StaticMesh':
					name = str(asset.get_name())
					bbox = asset.get_bounding_box()
					material = asset.get_material(0)
					center_x = ((bbox.max.x-bbox.min.x) *0.5 + bbox.min.x)*0.01
					center_y = ((bbox.max.z-bbox.min.z) *0.5 + bbox.min.z)*0.01
					center_z = ((bbox.max.y-bbox.min.y) *0.5 + bbox.min.y)*0.01
					# ------ right hand coord to left hand coord
					width = (bbox.max.x - bbox.min.x)*0.01
					height = (bbox.max.z - bbox.min.z)*0.01
					depth = (bbox.max.y - bbox.min.y)*0.01
					path = str(asset.get_path_name())
					self.jsonData[name]={
					#"id":id,
					"height": height,
					"width":width,
					"fbxpath":self.fbx_path+name+".fbx",
					"depth":depth,
					"uepath":str(path),
					"center":[float(center_x),float(center_y),float(center_z)],
					}
					row = [name,width,height,angle,depth]
					self.csvData.append(row)
					index+=1
		else:
			print "content is empty"
		#print self.csvData
		print json.dumps(self.jsonData)


	def exportJson(self):
		callsheet_path = self.callsheet_path
		isExist  = os.path.exists(os.path.dirname(callsheet_path))
		if isExist and self.jsonData != None :
			json_validator(json.dumps(self.jsonData))
			with open( callsheet_path,"w" ) as json_file:
				json.dump(self.jsonData,json_file,indent=4,sort_keys=True)
		else:
			print "can't find outPutPath"
	def exportCsv(self,callsheet_path):
		isExist  = os.path.exists(os.path.dirname(callsheet_path)) 
		if isExist and self.csvData != None:
			with open( callsheet_path, 'w') as outfile:
			    writer = csv.writer(outfile,delimiter=",",lineterminator="\n")
			    writer.writerows(self.csvData)
		else:
			print "can't find outPutPath"
	def exportFbx(self):

	   	isExist  = os.path.exists(os.path.dirname(self.fbx_path))
		if isExist and self.content != None:
			self.exportMyAssets()
		else:
			print "can't find fbx"
	# -------------------- Export FBX ----------------------------------
	def buildExportTask(self,asset_obj,filename='', options=None):
		task = unreal.AssetExportTask()
		task.set_editor_property('automated',True)
		task.set_editor_property('replace_identical',True)
		task.set_editor_property('filename', filename)
		task.set_editor_property('object', asset_obj)
		task.set_editor_property('options', options)
		task.set_editor_property('prompt',False)
	    
		return task
	def buildStaticMeshExportOptions(self):
		options = unreal.FbxExportOption()
		# unreal.FbxImportUI
		options.set_editor_property('collision', False)
		options.set_editor_property('level_of_detail', False)
		options.set_editor_property('vertex_color', False)
		options.set_editor_property('map_skeletal_motion_to_root', False)  # Static Mesh

		#options.set_editor_property('fbx_export_compatibility',2)
		# unreal.FbxMeshImportData
	def exportMyAsset(assets_path,output_path):
		asset_data = unreal.AssetData(assets_path)
		fbx_path = output_path + str(asset_data.asset_name) +".fbx"
		asset_obj=unreal.AssetRegistryHelpers().get_asset(asset_data)
		print asset_obj
		options = buildStaticMeshExportOptions()
		task_fbx = buildExportTask(asset_obj,output_path,options)
		a = unreal.Exporter.run_asset_export_task(task_fbx)
		print a

	def exportMyAssets(self):
		output_path = self.fbx_path
		assets = self.content
		tasks=[]
		for asset in assets:
			fbx_path = output_path + str(asset.get_name()) +".fbx"

			asset_obj = asset
			options = self.buildStaticMeshExportOptions()
			task_fbx = self.buildExportTask(asset_obj,fbx_path,options)
			tasks.append(task_fbx)
			
		unreal.Exporter.run_asset_export_tasks(tasks)
