# MayaScripts
Maya scripts: animation, rigging, etc

1) Animation

- reOpenScene.mel - Reopens the current saved scene, forcefully ignores the file version, and does not save any changes.

- autoFitAnimTimeline.mel - This script scans all NURBS-curve controls in the scene, gathers every keyframe on their transform attributes, computes the minimum and maximum frame, and then sets both the playback and animation range to that span.

- selectAllAnimCurves.mel - This script collects all types of anim Curve nodes in the scene and selects them.

- infinityCycle.mel - This script toggles animation curves’ infinity settings in the Graph Editor: a single click enables cycle infinities (pre- and post-infinity) and shows their indicators, while a double-click switches infinities back to constant mode and hides the infinity indicators for the selected controls.


1) Rigging

- importAllReferences.py -  This script retrieves a list of all file references in the scene and sequentially imports them into the current scene, printing success or error messages for each file.

- cleanNamespaces.py - This script gathers every child object of your current selection, selects them all, and then removes any namespaces from their names (starting with the deepest items to avoid conflicts).

- cleanImportedReferences.py - This script imports every file reference in the scene, grabs each reference’s top-level transform nodes, gathers all their descendants, selects them, and then strips any namespaces from those names (deepest nodes first to prevent naming conflicts).



