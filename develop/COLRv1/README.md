# TYPETR-Bitcount COLRv1 tests

This document gives an overview of incremental tests on CLRv1 coding, applied on a small glyph set of just ('a', 'b', 'c')

Note that for simplicity of testing (and compilation speed) only the weight axis is taken from the main Bitcount design space. In reality it will have these 4 axes, besides the COLRv1 axes:

* Weight (size of the pixels)
* Open (split each pixel in 4 quadrants)
* Slant (slanting the position of the pixels)
* Shape (fluently stepping through a range of shapes: circle, diamond, start, square). These shapes work with any of the other axes.

The advantage of making the main mask axes independent from the COLRv1 is that no extra masters are needed to define the corners of the extended design space.

## What I would like to achieve

* Currently the test layers only contain one single shape (e.g. a set of concentric gradient circles). What I would like is to make a layer that contain multiple color shapes, e.g in a row or a matrix. This layer image can then be shown to the user, where interesting locations of the “map” can be reached by x and y coordinate axes. 
* How to add multiple shapes to the same layer on different positions?

Below the relevant test versions are shown.

## Test 001

Single axis, where the position of the yellow-black gradient is connected to the weight axis (size of the pixels)

![](test001/images/Screenshot 2023-03-20 at 7.25.18 PM.png)![](test001/images/Screenshot 2023-03-20 at 7.25.50 PM.png)

## Test 004

Single axis, where the scale of a number of concentric circles and gradients is scaled in the center of the pixels, combined with the Bitcount weight axis (size of the pixel)

![](test004/images/Screenshot 2023-03-20 at 7.30.17 PM.png)
![](test004/images/Screenshot 2023-03-20 at 7.30.23 PM.png)![](test004/images/Screenshot 2023-03-20 at 7.30.31 PM.png)![](test004/images/Screenshot 2023-03-20 at 7.30.34 PM.png)## Test 005

Some other variants of Test 004

![](test005/images/Screenshot 2023-03-20 at 7.44.03 PM.png)![](test005/images/Screenshot 2023-03-20 at 7.44.06 PM.png)![](test005/images/Screenshot 2023-03-20 at 7.43.53 PM.png)
![](test005/images/Screenshot 2023-03-20 at 7.43.57 PM.png)## Test 006

The same weight axis as before, but now combined with two axes that position the gradients of concentric circles in x and y independently inside the pixel mask. 

![](test006/images/Screenshot 2023-03-20 at 7.47.23 PM.png)
![](test006/images/Screenshot 2023-03-20 at 7.47.46 PM.png)![](test006/images/Screenshot 2023-03-20 at 7.48.09 PM.png)![](test006/images/Screenshot 2023-03-20 at 7.48.18 PM.png)![](test006/images/Screenshot 2023-03-20 at 7.48.25 PM.png)![](test006/images/Screenshot 2023-03-20 at 7.48.30 PM.png)## Test 007

Similar to Test 006, but with more extended usage of the weight and position axes.

![](test007/images/Screenshot 2023-03-20 at 8.04.34 PM.png)
![](test007/images/Screenshot 2023-03-20 at 8.04.41 PM.png)
![](test007/images/Screenshot 2023-03-20 at 8.04.46 PM.png)![](test007/images/Screenshot 2023-03-20 at 8.04.52 PM.png)![](test007/images/Screenshot 2023-03-20 at 8.05.01 PM.png)![](test007/images/Screenshot 2023-03-20 at 8.05.19 PM.png)![](test007/images/Screenshot 2023-03-20 at 8.05.45 PM.png)

## Test 008This version adds another layer, again with its own independent x and y position axis. The new layer contains a miniature white image of the glyph itself. 

![](test008/images/Screenshot 2023-03-20 at 8.15.26 PM.png)![](test008/images/Screenshot 2023-03-20 at 8.15.39 PM.png)![](test008/images/Screenshot 2023-03-20 at 8.15.48 PM.png)![](test008/images/Screenshot 2023-03-20 at 8.16.10 PM.png)![](test008/images/Screenshot 2023-03-20 at 8.16.36 PM.png)![](test008/images/Screenshot 2023-03-20 at 8.16.58 PM.png)

## Test 009

Currently identical to Test 008

