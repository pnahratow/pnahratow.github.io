Title: Chainforcer (Baseogre) Release
Slug: chainforcer-baseogre-release
Date: 2024-02-09
Tags: gaming

*Hey, I finished the project and it only took about 400 weeks.*

<img src="{static}/static/baseogre_release/cut.png" style="max-height:512px" />

## Files

[Baseogre Quake MDL files - baseogre.zip]({static}/static/baseogre_release/baseogre.zip) - *Includes baseogre.mdl and h_baseogre.mdl*

[Baseogre Source Files - baseogre_sources.zip]({static}/static/baseogre_release/baseogre_sources.zip) - *Includes the rigged and animated blender file and the texture as a .psd file including layers*

## Description

This finalizes the work shown in my earlier posts

- [Chainforcer Lowpoly Modeling Stages]({filename}/projects/modprog.md)
- [Chainforcer Texture Painting Workflow]({filename}/projects/texworkflow.md)

What can I say. Apparently I got so annoyed from painting this texture that I needed a seven year break to regenerate all the cells in my body or something.

Nevertheless, it is done. Here is an ingame demo of the guy.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/UVERBoYa40g" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

The animations are setup so that they can directly replace the original Ogre model. Maybe to use the ogre enemy in base maps with a more fitting look. To do this just download the .mdl files and rename them to `ogre.mdl` and `h_ogre.mdl` and put the in the progs directory of your mod and you are good to go.

<img src="{static}/static/baseogre_release/front.png" style="max-height:512px" />
<img src="{static}/static/baseogre_release/back.png" style="max-height:512px" />

If you are interested in technical details or just generally want to play with the source files. I have provided them at the top. In there you have the final state of the blender file after I was done with the process. The character is rigged and animated.

<video controls playsinline autoplay muted loop preload="auto" style="width: 100%; max-width: 400px; height: auto;">
  <source src="{static}/static/baseogre_release/rigged.webm" type="video/webm" />
</video>

The texture is included as well as a source file with layers. It is a mess so don't expect anything.

![Skin original size]({static}/static/baseogre_release/skin512.png)

After resize and color conversion to the quake palette the texture looks like this.

![Skin converted for quake]({static}/static/baseogre_release/skin256_paletted_bayer_16.png)

Nothing more to say. Have fun!

<img src="{static}/static/baseogre_release/leatherface.png"  style="max-height:600px" />
<img src="{static}/static/baseogre_release/muzzleflash.png" style="max-height:512px" />
