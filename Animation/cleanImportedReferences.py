# cleanImportedReferences.py

import maya.cmds as cmds

def import_all_references_and_get_top_nodes():
    refs = cmds.file(query=True, reference=True) or []
    imported_top_nodes = []
    for ref_file in refs:
        try:
            # get top-level transform nodes in this reference (with namespace)
            top_nodes = cmds.referenceQuery(ref_file, nodes=True, dagPath=True) or []
            top_transforms = [
                n for n in top_nodes
                if cmds.objectType(n) == 'transform' and '|' not in n
            ]
            # import the reference into the scene
            cmds.file(ref_file, importReference=True)
            print("Imported:", ref_file)
            imported_top_nodes.extend(top_transforms)
        except Exception as e:
            print("Failed to import reference:", ref_file, str(e))
    return imported_top_nodes

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

def select_all_descendants_and_remove_namespace(objects):
    if not objects:
        cmds.warning("No objects provided!")
        return

    all_objs = get_all_descendants(objects)
    cmds.select(all_objs, replace=True)

    for obj in sorted(all_objs, key=lambda x: x.count('|'), reverse=True):
        short_name = obj.split('|')[-1]
        if ':' in short_name:
            base_name = short_name.split(':')[-1]
            try:
                cmds.rename(obj, base_name)
            except RuntimeError:
                pass

def cleanImportedReferences():
    """
    Import all file references, select their descendants,
    and strip namespaces from their names.
    """
    imported_top_nodes = import_all_references_and_get_top_nodes()
    if imported_top_nodes:
        select_all_descendants_and_remove_namespace(imported_top_nodes)
    else:
        cmds.warning("No references imported.")

# Execute the tool
cleanImportedReferences()
