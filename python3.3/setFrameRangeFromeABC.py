import hou 
import _alembic_hom_extensions as abc
def setFrameRangeByABC(abcpath):
    frame_range=abc.alembicTimeRange(abcpath)

    if frame_range is not None:
    
        fps=hou.fps()
        
        FSTART=frame_range[0]
        FEND=frame_range[1]
    
    
        hou.hscript("setenv -g F_START='{F_START}'".format(F_START=FSTART*fps))
        hou.hscript("setenv -g F_END='{F_END}'".format(F_END=FEND*fps))
    
        hou.playbar.setFrameRange(FSTART*fps,FEND*fps)
        hou.playbar.setPlaybackRange(FSTART*fps,FEND*fps)
    else :
        print "please give a valid path"  





abcpath=hou.ui.readInput("abcPath")[1]
setFrameRangeByABC(abcpath)



