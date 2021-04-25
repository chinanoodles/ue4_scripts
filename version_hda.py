"""
Increments the version of a hda/otl

If no version information is in the filename / definition, it will be added
eg:
myAwesomeThing.hda -->  myAwesomeThing__1.0.hda (definition is myAwesomeThing::1.0)

namespaces are respected
blah::myAwesomeThing::1.0 --> blah::myAwesomeThing::1.1

== Installation ==
Save this file somewhere in your pythonpath.
invoke it with 
import version_hda
version_hda.versionUpHda(hou.selectedNodes()[0])

want the right click menu?
save the next section (all the xml-ey part, wihtout the quotes) into an OPMenu.xml file somewhere in your HOUDINI_PATH. 
more info on that here:
http://www.sidefx.com/docs/houdini/basics/config_menus

"""


"""
<?xml version="1.0" encoding="UTF-8"?>
<menuDocument>
	<menu>

        <scriptItem id="cg_versionUpHDA">
       	    <label>Version up HDA</label>
            <insertAfter>opmenu.optypemanager</insertAfter>
       	    <context>
       		<expression><![CDATA[
node = kwargs["node"]

if node.type().definition() is None:
   return False

# this should be after checking the node definition is not None
installPath = hou.expandString('$HFS')
if installPath in node.type().definition().libraryFilePath():
    return False

#if not node.matchesCurrentDefinition():
#   return False

if node.isInsideLockedHDA() and not node.isEditableInsideLockedHDA():
   return False

if hou.hda.safeguardHDAs():
   return False

if not node.type().areContentsViewable():
   return False

return True
       ]]></expression>
       	    </context>

        <scriptCode><![CDATA[

node = kwargs["node"]

import version_hda
version_hda.versionUpHda(node)

        ]]></scriptCode>

       	</scriptItem>

	</menu>
</menuDocument>
"""
import re
import os
import hou

def versionUpHda(node):
    print node
    if node is None:
        return None
    
    if node.type().definition() is None:
        return None
    
    typeDef = node.type().definition()
    
    if typeDef.libraryFilePath() == 'Embedded':
        print 'HDA is embedded. Cannot version up'
        return None
    
    reSrch = re.search('(.*)::(\d+)?\.?(\d+).*$', node.type().name())
    if reSrch:
        base = reSrch.group(1)
        maj = int(reSrch.group(2))
        min = int(reSrch.group(3))
        
        newMaj = '%s::%d.%d' % (base, maj + 1, 0)
        newMin = '%s::%d.%d' % (base, maj, min + 1)
        ret = hou.ui.displayMessage("Version major or minor?", buttons=(newMaj, newMin, 'Cancel'))
        if ret == 2:
            # cancel
            return
        
        if ret == 0:
            maj += 1
            min = 0
        elif ret == 1:
            min += 1
    
    else:
        maj = 1
        min = 0
        base = node.type().name()
    
    newVersion = '%s::%d.%d' % (base, maj, min)
    newVersionFile = '%s__%d.%d.hda' % (base.replace(':', '_'), maj, min)
    newVersionLabel = '%d.%d' % (maj, min)
    
    typeDef.setVersion(newVersionLabel)
    
    hdaDir, hdaFile = os.path.split(typeDef.libraryFilePath())
    newHdaPath = os.path.join(hdaDir, newVersionFile).replace('\\', '/')
    
    if os.path.isfile(newHdaPath):
        if hou.ui.displayMessage("New version exists. Overwrite?\n" + newHdaPath, buttons=('Overwrite', 'Cancel')) == 1:
            return
    elif os.path.isdir(newHdaPath):
        # H16+ 'expanded' HDAs are directories
        if hou.ui.displayMessage("New version exists. Overwrite?\n" + newHdaPath, buttons=('Overwrite', 'Cancel')) == 1:
            return
    
    print 'Saving new version to:', newHdaPath
    
    if node.matchesCurrentDefinition():
        typeDef.copyToHDAFile(newHdaPath, new_name=newVersion)
        hou.hda.installFile(newHdaPath)
        node.changeNodeType(newVersion, keep_network_contents=False)
    else:
        typeDef.copyToHDAFile(newHdaPath, new_name=newVersion)
        hou.hda.installFile(newHdaPath)
        node = node.changeNodeType(newVersion, keep_name=True,
                                   keep_parms=True,
                                   keep_network_contents=True)
        
        node.type().definition().updateFromNode(node)
        node.matchCurrentDefinition()
    
    return newVersion
