import files_database as hexlib

hexAssets = hexlib("hex/assets/")
rocks_lib = hexAssets.getAssets("Rocks")
rocks_desert = rocks_lib.getAllByTag("DESERT")

#delete old versions

for rock in rocks_desert:
	for version in rock.versions():
		if version.tag() != "Latest":
				removeVersion(version)


print rocks_desert.list()

# get attribute from assets

rocks_desert_A_obj = rocks_desert.getByAttribute(width = 30,depth = 20, height = 10,id = 3)
rocks_desert_A = rocks_desert_A_obj.getVersion(Tag = "Latest")

rocks_desert_A = rock_A.ueShader()
rocks_desert_A = rock_A.filePath()
rocks_desert_A = rock_A.rock_A_uePath()