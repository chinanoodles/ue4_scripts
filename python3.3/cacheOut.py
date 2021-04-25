node = kwargs.get("node", None)
print "tst"
print node
if node is None:
	print "None"
elif node.parent().type().name()!="geo":
	print "It's not a sop node"
else:
	print "tst"
	node.type().category().name()
	root=node.parent()
	fileCache=root.createNode('filecache')
	fileCache.moveToGoodPosition()
	fileCache.setInput(0,node)
	fileCache.setColor(hou.Color(0,0.7,0.5))
	cmd = "oppresetload {PATH} cacheout".format(PATH=fileCache.path())
	hou.hscript(cmd)
	print cmd
