import unreal
import json

# filename: str : Windows file fullname of the asset you want to import
# destination_path: str : Asset path
# option: obj : Import option object. Can be None for assets that does not usually have a pop-up when importing. (e.g. Sound, Texture, etc.)
# return: obj : The import task object
def buildImportTask(filename='', destination_path='', options=None):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    task.set_editor_property('options', options)
    return task

# tasks: obj List : The import tasks object. You can get them from buildImportTask()
# return: str List : The paths of successfully imported assets
def executeImportTasks(tasks=[]):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    imported_asset_paths = []
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            imported_asset_paths.append(path)
    return imported_asset_paths


# return: obj : Import option object. The basic import options for importing a static mesh
def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)  # Static Mesh
    # unreal.FbxMeshImportData
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxStaticMeshImportData
    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options

def importMyAssets(filepath):
	file = "G:/output/NEW/shot/assets/assetsrock/efx/blendingRock_lib.json"
	#file = "G:/output/NEW/shot/assets/assetsrock/efx/smallRock_lib.json"
	file = "F:/svn/art/Houdini/Project/output/TerrainTest01/terrain/blendingRocks//riverCliff_lib.json"
	file = filepath
	with open(file,"r") as json_file:
	    data = json.load(json_file)
	for asset_name in data: 
		mesh_fbx = data[asset_name]["fbxpath"]
		base_color = data[asset_name]["base_cd_path"]
		normal_texture =  data[asset_name]["normal_tex_path"]
		ao_texture = data[asset_name]["ao_tex_path"]
		destination_path = data[asset_name]["uepath"]
		
		options = buildStaticMeshImportOptions()
		task_fbx = buildImportTask(mesh_fbx,destination_path,options)
		task_Cd = buildImportTask(base_color,destination_path)
		task_N = buildImportTask(normal_texture,destination_path)
		task_ao = buildImportTask(ao_texture,destination_path)
		tasks = [ task_fbx,task_Cd,task_N,task_ao ]
		
		executeImportTasks(tasks)
