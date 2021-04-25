#        __  _________  __    _____ __            ___     
#       / / / / ____/ |/ /   / ___// /___  ______/ (_)___ 
#      / /_/ / __/  |   /    \__ \/ __/ / / / __  / / __ \
#     / __  / /___ /   |    ___/ / /_/ /_/ / /_/ / / /_/ /
#    /_/ /_/_____//_/|_|   /____/\__/\__,_/\__,_/_/\____/ 
#    
#    Copyright 2020 chenzhaoxin@corp.netease.com. All Rights Reserved.

import unreal
# set ignor parm name
ignore_list = ["tMaskMap", "tOverlayNormal"] 

@unreal.uclass()
class EditorUtil(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MaterialEditingLib(unreal.MaterialEditingLibrary):
    pass


editorUtil = EditorUtil()
materialEditingLib = MaterialEditingLib()
# get selected asset
selectedAssets = editorUtil.get_selected_assets()

sourceMaterial = selectedAssets[0]
print ('source material ' + sourceMaterial.get_name())
# get source material parameter
scalar_parameter_names = materialEditingLib.get_scalar_parameter_names(sourceMaterial)
static_switch_parameter_names = materialEditingLib.get_static_switch_parameter_names(sourceMaterial)
texture_parameter_names = materialEditingLib.get_texture_parameter_names(sourceMaterial)
vector_parameter_names = materialEditingLib.get_vector_parameter_names(sourceMaterial)

source_base_Material = unreal.MaterialInterface.get_base_material(sourceMaterial)
target_materials = selectedAssets[1:]

for target_material in target_materials:
    print ('target material ' + target_material.get_name())
    materialEditingLib.set_material_instance_parent(target_material, source_base_Material)
    # set texture parm
    for texture_parameter_name in texture_parameter_names:
        if texture_parameter_name in ignore_list:
            continue
        value = materialEditingLib.get_material_instance_texture_parameter_value(sourceMaterial,texture_parameter_name)
        if value!=materialEditingLib.get_material_default_texture_parameter_value(source_base_Material,texture_parameter_name):
            materialEditingLib.set_material_instance_texture_parameter_value(target_material,texture_parameter_name,value)
    # set float parm
    for scalar_parameter_name in scalar_parameter_names:
        if scalar_parameter_name in ignore_list:
            continue
        value = materialEditingLib.get_material_instance_scalar_parameter_value(sourceMaterial,scalar_parameter_name)
        if value!=materialEditingLib.get_material_default_scalar_parameter_value(source_base_Material,scalar_parameter_name):
            materialEditingLib.set_material_instance_scalar_parameter_value(target_material,scalar_parameter_name,value)
    # set vector parm
    for vector_parameter_name in vector_parameter_names:
        if vector_parameter_name in ignore_list:
            continue
        value = materialEditingLib.get_material_instance_vector_parameter_value(sourceMaterial,vector_parameter_name)
        if value!=materialEditingLib.get_material_default_vector_parameter_value(source_base_Material,vector_parameter_name):
            materialEditingLib.set_material_instance_vector_parameter_value(target_material,vector_parameter_name,value)
    # update change
    materialEditingLib.update_material_instance(target_material)

