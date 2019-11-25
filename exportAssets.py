import unreal
import json,os
import csv

root_path = unreal.Paths().project_dir()

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

def writeOut(file_path,data):
	if os.path.exists(file_path):
		with open( file_path ) as json_file:
			data_orig = json.load(json_file)
			#print data_orig
			data_orig.update(data)
			#print data
		with open( file_path,"w+" ) as json_file:
			json.dump(data_orig,json_file,indent=4,sort_keys=True)    
	else:
		with open( file_path,"w+" ) as json_file:
			json.dump(data,json_file,indent=4,sort_keys=True)


def writeOutJson():
	asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
	assets = asset_reg.get_assets_by_path('/Game/scene/Rocks/Meshes')
	#print assets
	data={}
	index = 0
	csv_data=[["name","width","height","angle","depth"]]
	angle = -1
	for asset in assets:
		if asset.asset_class =='StaticMesh':
			name = str(asset.asset_name)
			
			if name.find("Cliff")!=-1:
				asset_obj=unreal.AssetRegistryHelpers().get_asset(asset)
				bbox = asset_obj.get_bounding_box()

				material = asset_obj.get_material(0)

				width = (bbox.max.x - bbox.min.x)*0.01
				height = (bbox.max.y - bbox.min.y)*0.01
				depth = (bbox.max.z - bbox.min.z)*0.01
				path = str(asset.object_path)
				data[name]={
				#"id":id,
				"height": height,
				"width":width,
				"fbxpath":"",
				"depth":depth,
				"uepath":str(path),

				}
				row = [name,width,height,angle,depth]

				csv_data.append(row)

				index+=1
		else:
			print "None"
	folder_path = "G:/output/NEW/shot/assets/assetsrock/efx/"
	json_name = "call_sheet_ueAssets.json"
	csv_name = "call_sheet_ueAssets.csv"

	print data
	json_validator(str(data))
	with open( folder_path+json_name,"w+" ) as json_file:
		json.dump(data,json_file,indent=4,sort_keys=True)

	with open( folder_path+csv_name, 'w+') as outfile:
	    writer = csv.writer(outfile,delimiter=",",lineterminator="\n")
	    writer.writerows(csv_data)
	print index
def executeExportTasks(tasks=[]):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    imported_asset_paths = []
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            imported_asset_paths.append(path)
    return imported_asset_paths

def buildExportTask(asset_obj,filename='', options=None):
    task = unreal.AssetExportTask()
    task.set_editor_property('automated',True)
    task.set_editor_property('replace_identical',True)
    task.set_editor_property('filename', filename)
    task.set_editor_property('object', asset_obj)
    task.set_editor_property('options', options)
    task.set_editor_property('prompt',False)
    
    return task
def buildStaticMeshExportOptions():
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
def exportMyAssets(folder_path,output_path):
	folder_path = '/Game/scene/Rocks/Meshes'
	asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
	assets = asset_reg.get_assets_by_path(folder_path)
	output_path = "G:\\"
	tasks=[]
	for asset in assets:
		fbx_path = output_path + str(asset.asset_name) +".fbx"
		asset_obj=unreal.AssetRegistryHelpers().get_asset(asset)
		options = buildStaticMeshExportOptions()
		task_fbx = buildExportTask(asset_obj,fbx_path,options)
		tasks.append(task_fbx)
		
	unreal.Exporter.run_asset_export_tasks(tasks)
