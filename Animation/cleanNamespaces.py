import maya.cmds as cmds

def get_all_descendants(objects):
    result = set()
    def collect(obj):
        if obj in result:
            return
        result.add(obj)
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []
        for child in children:
            collect(child)
    for obj in objects:
        collect(obj)
    return list(result)

def cleanNamespaces():
    """
    Collects all descendants of the current selection,
    selects them, and strips their namespaces.
    """
    selection = cmds.ls(selection=True, long=True)
    if not selection:
        cmds.warning("Nothing selected!")
        return

    # Get all descendants (full recursion)
    all_objs = get_all_descendants(selection)
    # Update selection in Outliner
    cmds.select(all_objs, replace=True)

    # Remove namespace for every object (leaf to root)
    for obj in sorted(all_objs, key=lambda x: x.count('|'), reverse=True):
        short_name = obj.split('|')[-1]
        if ':' in short_name:
            base_name = short_name.split(':')[-1]
            try:
                cmds.rename(obj, base_name)
            except RuntimeError:
                pass

# Execute the tool
cleanNamespaces()