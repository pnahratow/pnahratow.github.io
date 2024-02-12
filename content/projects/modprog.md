Title: Chainforcer Lowpoly Modeling Stages
Slug: chainforcer-lowpoly-modeling-stages
Date: 2016-03-11
Tags: gaming

![Chainforcer model]({static}/static/modprog/title_pose.png)

While working on this model I saved several in between backups. These screenshots show the stages the model went through.

## Concept / Viewport Background

The basic character concept and also essential viewport backgrounds that will define the form. Both views contain different information on one axis but the same on the vertical axis. To use this as viewport backgrounds I made sure the landmarks on the vertical axis are on the same height. That's why there are these lines.

![Chainforcer model]({static}/static/modprog/00_background.png)

## Blender's Skin Modifier

The basic form is created using a combination of blender modifiers (mirror, skin, subdivison). You can see a thin line inside the model. Thats what's manually defined. The actual hull is what the skinmodifier does. It creates a hull mesh around verts and edges. Geometry will be added when verts move apart. The volume increases when verts are scaled. The geometry isn't optimal but I think it still saves time since I only had to define 13 vertices to get this basic shape.

![Skin modifier]({static}/static/modprog/01_skinmod.png)
![Skin modifier with arms]({static}/static/modprog/02_skinmod_w_arms.png)

## Refining

* Started with the boots by moving the verts from all angles so they align with the background images.

![Boot progress]({static}/static/modprog/03_progress_boot.png)

* Removed some unneccessary edges to have about even poly density.

![Less geometry]({static}/static/modprog/04_less_geometry.png)

* I noticed some triangles in the geometry and removed them by adding edge loops.

![Better topology]({static}/static/modprog/05_better_topo.png)

* Gradually touching all vertices to define the form.

![Defining general shape]({static}/static/modprog/06_getting_in_shape.png)

* Some more form definiton on the hips and head.

![Hip and head details]({static}/static/modprog/07_hip_head_detail.png)

* Extruded the belly plate and arm ammo packs. Also defined the shoulder/glove transition.

![Plate and glove details]({static}/static/modprog/08_plate_glove_detail.png)

* Create the leg ammo packs and face indentation using the extrude tool.

![Visor and legammo details]({static}/static/modprog/09_shade_legpacks_detail.png)

## Done

* Finally removed edgeloops that don't add much to the form to reduce polycount.

![Done backside]({static}/static/modprog/10_done_backside.png)
![Done frontside]({static}/static/modprog/11_done_frontside.png)

* Added a weapon (chainsaw-grenade-launcher) and a "muzzle flash"

![With weapon]({static}/static/modprog/12_with_weapon.png)

## UV Mapping

* This is how the model was cut for uv mapping. The red edges mark uv seams.

![UV cuts and seams]({static}/static/modprog/13_cut_and_seam.png)

* Here the resulting UV map. I aligned some of the seam vertices to make hiding them easier later. Unwrapping option was set to "conformal" most of the time.

![UV map]({static}/static/modprog/15_uv_map.png)
![Testmap on model]({static}/static/modprog/14_test_uv.png)
