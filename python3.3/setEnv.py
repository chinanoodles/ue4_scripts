
'''
	work path Z:\projects\huoshen\work\shot\a10\a10430
	cache path Z:\projects\huoshen\output\efx_cache\shot\a10\a10430
'''
import os
import hou
class pproject:
	def __init__(self,root,proj,scn,shot,fstart,fend):
		'''
		root = "Z:/projects"
		self.path_scene = "{ROOT}/{PROJ}/work/shot/{SCN}/{SCN}{SHOT}/efx/task/houdini".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.path_cache = "{ROOT}/{PROJ}/output/shot/{SCN}/{SCN}{SHOT}/efx".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.path_anim = "{ROOT}/{PROJ}/publish/shot/{SCN}/{SCN}{SHOT}/ani/publish".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.path_camera =""
		'''
		user = os.getenv("USER")
		self.path_scene = "{ROOT}/{PROJ}/work/{SCN}/{SHOT}/houdini".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.path_cache = "{ROOT}/output/{PROJ}/{SCN}/{SHOT}".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.path_anim = "{ROOT}/{PROJ}/publish/{SCN}/{SHOT}/ani/publish".format(ROOT=root,PROJ=proj,SCN=scn,SHOT=shot)
		self.proj = proj
		self.scn = scn
		self.shot =shot
		self.fstart=fstart
		self.fend=fend
	def setEnvVars(self):
		
		hou.hscript("setenv PROJ='{PROJ}'".format(PROJ=self.proj))
		hou.hscript("setenv SCN='{SCN}'".format(SCN=self.scn))
		hou.hscript("setenv SHOT='{SHOT}'".format(SHOT=self.shot))
		hou.hscript("setenv F_START='{F_START}'".format(F_START=self.fstart))
		hou.hscript("setenv F_END='{F_END}'".format(F_END=self.fend))		
		hou.hscript("setenv OUTPUT='{OUTPUT}'".format(OUTPUT=self.path_cache))
		hou.hscript("setenv WORKPATH='{WORKPATH}'".format(WORKPATH=self.path_scene))
		hou.hscript("setenv ANIMPATH='{ANIMPATH}'".format(ANIMPATH=self.path_anim))

	def mkdir(self):
		if not os.path.isdir(self.path_scene):
			os.makedirs(self.path_scene,0755)

	def listChars(self):
		print "listChars"
	def loadAnim(self):
		print "loadAnim"
	def loadCam(self):
		print "loadCam"

def main():
	p = pproject("huoshen","a01","430")
	print p.path_scene,p.path_cache,p.path_anim

if __name__ == '__main__':
	main()
	print "tst"
