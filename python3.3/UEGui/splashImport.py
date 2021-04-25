import unreal
import json,os
lib = unreal.EditorAssetLibrary
foam = lib.load_asset('/Game/WaterMaterials/Particles/P_Waterfall_Foam.P_Waterfall_Foam')
splash = lib.load_asset('/Game/WaterMaterials/Particles/P_Water_Splashes.P_Water_Splashes')

splash = lib.load_asset('/Game/Test_assets/WaterfallTool/Particles/PS_BottomSplash.PS_BottomSplash')

def createSplash( json_path ):
    with open(json_path,"r") as json_file:
        data = json.load(json_file)
        for asset_name in data:
            pos = data[asset_name]["position"]
            rot = data[asset_name]["rotation"]
            splash_scale = data[asset_name]["splash_scale"]
            foam_scale = data[asset_name]["foam_scale"]
            splash_type = data[asset_name]["splash_type"]

            if splash_type == 1: # splash bottom
                splash = lib.load_asset('/Game/Test_assets/WaterfallTool/Particles/PS_BottomSplash.PS_BottomSplash')
                splash_scale *=2
            elif splash_type == 0: # splash top
                splash = lib.load_asset('/Game/Test_assets/WaterfallTool/Particles/PS_TopSplash.PS_TopSplash')

            actor_location = unreal.Vector(pos[0]*100,pos[1]*100,pos[2]*100)
            #actor_rotation = unreal.Rotator(rot[0],rot[2],rot[1])
            m_vector = unreal.Vector()
            m_vector.set(0,0,1)
            m_rot = m_vector.rotator_from_axis_and_angle(rot[1])
            actor_rotation =  unreal.Rotator(rot[0],rot[2],rot[1])
            #actor_rotation =  m_rot
            actor_splash_scale = unreal.Vector(splash_scale[0],splash_scale[1],splash_scale[2])
            actor_foam_scale = unreal.Vector(foam_scale[0],foam_scale[1],foam_scale[2]) 
            m_name = "streamSplash"

            actor_splash = unreal.EditorLevelLibrary.spawn_actor_from_object(splash, actor_location, actor_rotation)
            actor_splash.set_folder_path('/'+m_name+'/')
            actor_splash_tags = actor_splash.get_editor_property('tags')
            actor_splash_tags.append('stream splash')
            actor_splash.set_editor_property('tags', actor_splash_tags)
            actor_splash.set_actor_scale3d(actor_splash_scale)
            actor_splash_componet = actor_splash.get_components_by_class(unreal.ParticleSystemComponent)[0]
            actor_splash_componet.set_translucent_sort_priority(100)



            
'''
            actor_foam = unreal.EditorLevelLibrary.spawn_actor_from_object(foam, actor_location, actor_rotation)
            actor_foam.set_folder_path('/'+m_name+'/')
            actor_foam_tags = actor_foam.get_editor_property('tags')
            actor_foam_tags.append('stream foam')
            actor_foam.set_editor_property('tags', actor_foam_tags)
            actor_foam.set_actor_scale3d(actor_foam_scale)
'''