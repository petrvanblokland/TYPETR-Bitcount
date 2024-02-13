# TYPETR-Bitcount TODO


## TODO

* **Petr doing** Some solid color elements in both layers should still get some gradient and some minor adjustments to elements when there is slant. For the rest I think we are done.
* **Need input from Google** Decide on axis names for the main design space: 4 main axes and 6 color axes.
* ** Petr doing** Merge the test VF design space with the main Bitcount design spaces and build new VF. 
* **Editorial checks from Google?** The “manual” document is in documentation/Bitcountreference.md which exports into documentation/BitcountReference.pdf. This document has a download link on the site.
* **Petr doing, once the VF is running** Add more example images for documentation to generate BitcountReference.pdf, also including the latest state for COLRv1 examples.
* **Petr doing, once the VF is running** Implement COLv1 VF examples with additional layers and axes.
* **Petr doing, once the VF is running** Make Github repository public and start the website from there. 
* **Petr doing** Add comments to code about building and structure with COLRv1 layers.

## DONE

* **Aligning the /canvas with the actual shape of the pixels, cut from the layer size/position.**
* **DONE Needs some working with Simon** Decide on final color pixel types (design and layers) to show COLRv1 functions. ** This works great now, with very rapid compilation, thanks to Simon**
* **DONE** Make a VF with one layer first, to understand the relation on scaling and gradient positions.
* **DONE** Since the Bitcount-Bold has overlapping pixels (which is not visible in monochrome colors) needs to be sorted in the base masters in order to achieve a more consistent pattern inside letters. Now the order of the pixel components it random from copy/paste in the past. 
* **DONE** Rewrite the *build.py* using plain fontmake instead of the current FontProject. 
* **DONE** Generate all 6 standard VF (mono width black pixels only), including the COLRv1 axes.
	* Bitcount Grid Double
	* Bitcount Grid Single
	* Bitcount Mono Double
	* Bitcount Mono Single
	* Bitcount Prop Double
	* Bitcount Prop Single
* **Petr doing** Generate all instances font files in *otf/* and *ttf/*
* **DONE. Needs editorial input from Google?** Adapt the website to include COLRv1 examples.


## Nice to have

* An online editor to move/scale the two layers interactively?
* Add Bitcount outline masters.

## Committed

Try sources/vf/Bitcount_Mono_Double4-COLRv1-009.ttf in FontGoggles.

### Pixel shape axes: 

* slnt = Slant, circles stay circles, verticals slant, pixels positions slant. Note that there is a separate [ss08] OT-feature to make italic shapes, independent of the slanting angle.
* wght = Weight, size of the pixels. Default (400) is a pixel size, e.g. circles, where the pixels just touch. Lighter makes separate pixels, bolder makes them overlap.
* ELXP = Open pixels, split into 4 quadrants.
* ELSH = Shape, the axis enables a catalogue of shapes, fluently blending into the next. In order of appearance: filled circles (0), outline circles (80), filled squares with circle inside (180), filled square with diamond inside (265), outline square (362), filled square (500), plus (620), filled diamond (720), filled star (800), outline star (900), filled square with star inside (1000)

Then there are 6 independent COLRv1 axes that define the coloring of the selected pixel shape. Type /canvas (with the slash) and enable the [calt] OT-feature to show a canvas square as glyph. Different from showing the COLRv1 pattern in each individual pixel, the /canvas glyph show the full em-square with the color layers. There is a small square in the middle that shows the clipping area of the pixel. This was it's easy to select a color pattern and calibrate the position of the layers.

### The COLRv1 layers are:

* LR1S = Layer1-Scale, defines the scale of layer 1. By default the value is 0, so no colors are show. I don't see a possibility to alter the default value, without adding more masters to the axes (which dramatically will increase the size of the VF file). More about that below in "known issues"
* LR1X = Layer1-X. Horizontal position of layer 1. The same problem is here. Since the axis has 2 masters, the default position shows the circle in the middle of pixels. But that does not allow to move the layer to the right of the concentric circles. A work around is to add more circles on the left, but that requires the drawing of multiple elements in the same layer, something I did not manage to get working yet.
LR1Y = Layer1-Y. Vertical position of layer 1. The same happens here, it is not possible to have the circles centered in the pixel by default AND use only 2 masters AND allow showing area above the circles (making the layer go down, below the default position)
* LR2S = Layer 2 scale (same as LR1S in "independent" layer)
* LR2X = Layer 2 horizontal position (same as LR1X in "independent" layer)
* LR2Y = Layer 2 vertical position (same as LR1Y in "independent" layer)

See screens below with various axes settings.

Also note there is a number of normal OT-features supporting small-caps, stylistic alternates. For the Bitcount Single variants there is also a condensed available. Currently we only compile the Mono Double for testing the COLRv1 axes. For the other 5 Bitcount variants the color working will be identical.

### To do:

* Decision about all axis names.
* If final file size allows, we could add a third color layer with different shapes to choose from. The layers allow blending of color shapes. That is independent from the collection of shapes that can be on one each separate layer.
* Add a manual and visual examples to the documentation and the website.

### Known issues to the current COLRv1 state:

* Currently each COLRv1 axes has 2 masters. That causes limitations when selecting a default in the middle (e.g. with horizontal and vertical positioning). As mentioned before, a work around is to place multiple shapes on the same layer, so it is less of a problem that the half of the circle on the corner cannot be reached. I tried adding default masters to the X and Y axes, but that increases the number of color masters from 64 (2^6) to 729 (3^6), just for the color masters. Note that Bitcount has a large glyphset, so this adds a lot to the volume (and compile time)
* The 6 axes currently make a 6-dimensional cube, with the definition of the corners. This makes the selection of one layer dependent on the selection of another layer. It is visible when layer 1 is positioned, then changing the position of layer 2 will also alter the positions of layer 1. There is not a good way in VF to make truly independent axes if corners of the cubes remain undefined. However, adding them here will dramatically increase the side of the file. It would be nice if VF allowed true independent axes, especially with COLRv1 usage, since the axes that define the black masking shape and the axes that define the color layer don't need to be related. Even so, the two layers are now supposed to have a relation, but in the way VF currently is constructed, to do interact.
* How to draw multiple shapes in one layer? (See the current code below. Now multiple shapes are drawn in that layer, but the does not seem to work. Only returning if one is returned.)
* The default background color of layer it purple. I need to find a way to make the gray instead.
