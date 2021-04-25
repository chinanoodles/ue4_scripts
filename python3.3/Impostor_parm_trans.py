#   ___ ___ _______________  ___   _________  __              .___.__         
#  /   |   \\_   _____/\   \/  /  /   _____/_/  |_  __ __   __| _/|__|  ____  
# /    ~    \|    __)_  \     /   \_____  \ \   __\|  |  \ / __ | |  | /  _ \ 
# \    Y    /|        \ /     \   /        \ |  |  |  |  // /_/ | |  |(  <_> )
#  \___|_  //_______  //___/\  \ /_______  / |__|  |____/ \____ | |__| \____/ 
#        \/         \/       \_/         \/                    \/             
#    Copyright 2020 chenzhaoxin@corp.netease.com. All Rights Reserved.

import unreal


@unreal.uclass()
class EditorUtil(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class MaterialEditingLib(unreal.MaterialEditingLibrary):
    pass

editorUtil = EditorUtil()
materialEditingLib = MaterialEditingLib()

selectedAssets = editorUtil.get_selected_assets()

FoliageMat = False
ImpostorMat = False

for selectedAssetMesh in selectedAssets:
    if selectedAssetMesh.get_class().get_name() == 'StaticMesh':
        # get parm
        for MaterialIndex in range(10):
            AssetMeshMat = selectedAssetMesh.get_material(MaterialIndex)
            if AssetMeshMat:
                if AssetMeshMat.get_base_material().get_name() == 'PBR_Foliage':
                    FoliageMat = AssetMeshMat
                elif AssetMeshMat.get_base_material().get_name() == 'Impostor2D':
                    ImpostorMat = AssetMeshMat
        if FoliageMat and ImpostorMat:
            MaxRot = materialEditingLib.get_material_instance_scalar_parameter_value(FoliageMat,"cMaxRotationL1_Piv")
            WindScale = materialEditingLib.get_material_instance_scalar_parameter_value(FoliageMat,"cLocalWindScaleL1_Piv")

            # set parm
            materialEditingLib.set_material_instance_scalar_parameter_value(ImpostorMat,"cMaxRotation_Piv",MaxRot)
            materialEditingLib.set_material_instance_scalar_parameter_value(ImpostorMat,"cLocalWindScale_Piv",WindScale)

            # update change
            materialEditingLib.update_material_instance(ImpostorMat)
            print 'Transmit ' + selectedAssetMesh.get_name() + ' Impostor Material'
