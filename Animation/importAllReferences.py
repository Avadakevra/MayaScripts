#Import_Reference_rig_how_object
import maya.cmds as cmds

def importAllReferences():
    refs = cmds.file(query=True, reference=True) or []
    for ref_file in refs:
        try:
            cmds.file(ref_file, importReference=True)
            print("Imported:", ref_file)
        except Exception as e:
            print("Failed to import reference:", ref_file, str(e))

# Execute the tool
importAllReferences()