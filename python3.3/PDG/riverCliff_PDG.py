# -*- coding: utf-8 -*-
import argparse
import hou
import os, time

parser = argparse.ArgumentParser(description='Feed in hipfile')
parser.add_argument('--nodes', action="store", dest="m_nodes")
parser.add_argument('--cfolder', action="store", dest="m_cfolder")
parser.add_argument('--hip', action="store", dest="m_hip")
parser.add_argument('--farm',  type=bool, dest="m_farm")

filepath = parser.parse_args().m_hip
folderpath = parser.parse_args().m_cfolder
nodespath = parser.parse_args().m_nodes
farm_option = parser.parse_args().m_farm


print "start"




root = hou.node('/obj')
parent = root.createNode('geo')
parent.loadChildrenFromFile( nodespath ,ignore_load_warnings=True)


riverCliff = hou.node('/obj/geo1/rivercliff1')
riverCliff.allowEditingOfContents()

riverCliff.matchCurrentDefinition()



#for i in range(10):
	#print "###############################################"
	#time.sleep(1)

print "load nodes"

submit = parent.node( 'rivercliff1' )
submit.parm( 'pfolder' ).set( folderpath )

filepath = filepath.replace("\\","/")

print submit

print submit.parm('submitjob')



hou.hipFile.save( filepath )

if farm_option == 1: 
		submit.parm('submitjob').pressButton();
else:
	pass



#---------------------------------------








