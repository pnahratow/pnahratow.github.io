Title: Creating Models For Quake 1
Slug: creating-models-for-quake-1
Date: 2016-02-26
Tags: gaming


# Preface

This is kind of a tutorial/gathering of infomation about creating a model (specifically enemy model) for quake 1. I recently went through the whole process and want to share some of the stuff I've learned.

![Image of monster model]({filename}/images/mon_knut.png)

I'm a hobbyist and learned most of this as I went along. Aside from the part about texture-painting (which I have done in before) this is more a collection of links than a tutorial.

# Index

[TOC]

# Software

* [Blender](http://blender.org) - for 3d modeling
* [Taniwha's mdl exporter](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Quake_mdl) - for exporting to mdl format
* [Krita](http://krita.org) - for digital painting
* [Fteqcc](http://fte.triptohell.info/ftedownloads/) - for compiling quakec
* [QuakeC v1.06 Base](http://www.moddb.com/games/quake/downloads/quake-c-version-106)

# Creating The Model

I saw this video [Protoss Leg Modeling Method](https://www.youtube.com/watch?v=nm4E5QG9ZDM) some time ago. Although it is not much I really liked it because it shows a flowchart way of modeling shapes that have a cylindrical nature. It's something I understood and was confident that I could replicate. It is how I did the legs of the model.

Doing this in Blender seemed cumbersome at first because the box selection tool uses a keyboard shortcut <kbd>B</kbd> instead of just beeing the right mouse default function. But I then discovered that <kbd>A</kbd> is De/select-All and this becomes super fast by alternating <kbd>A</kbd>,<kbd>B</kbd>.

There is alot to learn about blender and I haven't really scratched the surface but [blender.stackexchange.com](http://blender.stackexchange.com/) is the ultimate resource of awesome and <kbd>SPACE</kbd> opens a textfield that lets you search for anything in blender.

Aside from that I would urge you to visit the [Youtube Channel of Darrin Lile](https://www.youtube.com/user/DarrinLile) because thats where I learned what I wanted in an enjoyable and easy to grasp manner.

# Creating The UV Map

In order to paint the texture the model needs to be unwrapped. Which means the models needs information about how 2d image would be applied to the 3d polygons to be its texture. A result of this looks something like this.

![UV Maps example]({filename}/images/uv_map.png)

Again by Darrin Lile [UV Mapping](https://www.youtube.com/playlist?list=PLyelx0TsmSpfZRCzf9qDFn4XOPZqH0rQp) you can pretty much follow this tutorial exactly.

## Seams, Stretching and Shapes

The tutorial talks a bit about stretching and seam placement. One thing I would add to that would be to keep in mind that you want to paint the texture later. When you use blenders 3d painting tools this is less of a problem. But in an imageeditor some seams are very hard to fix. Try to make seams straight lines where possible because that is easily to hide by copying/mirroring. Also try to maintain recognizable shapes. When painting one tends to stick to how he/she would do it in a drawing. Stretches and forms that only look good on the model but are weird on the texturemap are hard to paint. Usually the painted texturemap should look cool by itself. 

## Applying the image texture


# Painting The Texture

This step essentially comes down to plain digital painting where you handpaint everything starting from a blank screen. There is no single tutorial for this because the topic is vast and people spend lifetimes on it. If you've never done anything in this area your texture will probably come out sub par at first but I do want to encourage you. I personally was very invested into pursuing 2d art at one point in my life but stopped because I realized I wasn't quite willing to put in the necessary work to get gud.

However painting textures for a 3d model is less hard. Proportions and perspective is taken care of by the 3d model and you won't have to worry about that. Gamemodels are usually moving so you can get away with textures that don't ooze perfection in still. Also, especially old tech like quake can be very forgiving because of the low resolutions. If you for example have trouble painting ears that won't be more than a couple of pixels in the end so don't sweat it. What I'm saying is that it's possible to make at least decent 2d gameart without being a dedicated 2d artist.

## Tablet

A graphic tablet is a necessity in my opinion. Maybe not if you primarily do very technical stuff like machines, mechs, weapons or if you are a superb pixel artists but when it comes to organic forms I wouldn't want to use a mouse.

Wacom makes great products. I have a Graphire4 which is old but does the job. I wish I had more pressure levels and more DPI but it's not a big problem. Basically if you're starting out get any wacom tablet that suits your price doesn't matter which. If you wan't to have something better get an Intuos Pro or Cintiq.

## Brushes

Photoshop is great but expensive. Gimp is great but also not. I recently tried Krita which I like. Doesn't matter which software - I always try to assemble this basic set of tools.

### Paintbrush

A tool to lay down paint. I use only one because I'm not very experienced and don't know how to handle the many presets there are. I know how to use a real pencil and thats why I fiddle with the brush settings until I can comfortably create this gradienty kind of thing in one stroke.

![A painted gradient]({filename}/images/brush_gradient.png)

Here are a couple of tips to get this

* The brushtip is 100% hard.
* Play with the density/spacing. Try 100%.
* Pressuresensitivity is on for size and opacity
* If you're not super precise with the pressure. Try limiting the size range maybe only 100%-80%.
* If you're not super precise with the pressure. Play with the pressure curve for opacity. Make it so that 100% opacity only comes when you press real hard.
* If opacity builds up during one stroke when you pass a section twice. Try to deactivate that. Search for "build up" or "wash" mode.

### Smudger

Literally satan. Having hard edges is a thing that makes stuff look crisp. It's why I use a hard brush to paint. Blurry brushstrokes is one of the most common things that makes beginner artwork look bad. Still I use this tool. Most of the time when evening out too harsh highlights like this. 

![A smudged highlight]({filename}/images/smudge_hl.png)

This brush is 2-4px wide and at 20-40% strength.

### Softie

A big round brush with soft edges and very low opacity. I use this to create soft gradients or to apply color lighly without disrupting anything. Usually in a situation where I have a selection and then use the side of the brush like this.

![Application for soft brushes]({filename}/images/softbrush_appl.png)

## Workflow and Tips

I attack the empty texture with this basic arsenal until I'm happy with what I see. At this point I feel like a crazy chicken running in circles hoping for something good to happen. All the brushstrokes are bad. Colors look off or boring but I know it gets better when I invest more time so I keep at it. I can't say much about this but other people can. Here is a [youtube user](https://www.youtube.com/user/Sycra) that I like . I'm sure you can find more. 

Regarding general workflow

Here are some other generic bits of information.

### Double Resolution

My brushstrokes are wonky and I don't know how to do close-up pixel pushing. What I do to help with that is paint the texture in twice the resolution. If the target texture is 256x256px I paint in 512x512px. The downscaling in the end smooths out some of the irregularities. Lazily done gradients become smooth and some mistakes disappear. However the whole image becomes blurry and looses contrast too. To help with that there is a filter called "Unsharp Mask" (look under sharpen or enhance). Use with low values. The image below shows how to get some of the crispness back with this filter.

![Unsharp Mask filter result]({filename}/images/unsharp_mask.png)

### Blending Modes

Learn about blending modes regarding brushes and layers. There are cool light effects like rimlights, neon glow, fire and subsurface scattering and all those flashy things. They look great on textures. Blending modes help with this. You should become familiar with multiply, screen/lighten, dodge, burn and overlay. Check out this [Video](https://www.youtube.com/watch?v=AybFWViT-3Q).

### Moar Color

A quick thing on colors. If you experience the problem that your skintones look dull or off. Check out this [Video](https://www.youtube.com/watch?v=PPdkEEYo3F0).

# Rigging And Animation

# Exporting To MDL

# QuakeC