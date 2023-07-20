# TYPETR-Bitcount

This document gives an overview of the files in this repository.

For a full description about TYPETR-Bitcount history, design background, functionality and OT-features read **documentation/BitcountReference.pdf**

![](documentation/BitcountReference.pdf)

## Files & folders

### AUTHORS.txt

* This is the official list of project authors for copyright purposes. 
* This file is distinct from the *CONTRIBUTORS.txt* file. 
* See the latter for an explanation. 

### CNAME

Allows Github to run the *docs/* as Bitcount website with static pages from *http://bitcount.typenetwork.com*

### CONTRIBUTORS.txt

This is the list of people who have contributed to this project, and includes those not listed in AUTHORS.txt because they are not copyright authors. For example, company employees may be listed here because their company holds the copyright and is listed there.

### develop/COLRv1

Comtains a range of small test masters how to implement various *COLRv1* functions.

### docs/

* Allows Github to run the *docs/* as Bitcount website with static pages from *http://bitcount.typenetwork.com*
* Main home page is *docs/index.html*

### documentation/

* Contains the source markdown file for *documentation/BitcountReference.pdf* and its *images/* source files.

### FONTLOG.md

This file provides detailed information on the Bitcount font software.
This information should be distributed along with the Bitcount fonts and any derivative works.

### LICENSE.txt

* Copyright 1980 The Bitcount Project Authors (tptr@petr.com)
* This Font Software is licensed under the SIL Open Font License, Version 1.1.
* This license is copied below, and is also available with a FAQ at:
http://scripts.sil.org/OFL

### METADATA.yml

Production script

### otf/

Exported OTF instance font files, ready to use.

### README.md

This file.

### sources/

#### Current archtecture of design spaces

This directary contains all UFO sources, build scripts and design space file, that are used to generate the font files in *otf/*, *ttf/* and *vf/*.

~~~

Bitcount_Grid_Double4-COLRv1.designspace
Bitcount_Grid_Single4-COLRv1.designspace
Bitcount_Mono_Double4-COLRv1.designspace
Bitcount_Mono_Single4-COLRv1.designspace
Bitcount_Prop_Double4-COLRv1.designspace
Bitcount_Prop_Single4-COLRv1.designspace

~~~

The flags in sources/build.py decide which VF is building and which stage of the building process is exectuted.

**WARNING** Generating the 6 different Bitcount VF flavours of about 8Mb, each of the 6 design spaces needs over 22Gb of free space in the _masters/ folder for the 208 expanded pixel UFO’s files (3x2x12x2 + 2x2x2x2x2x2), each over 100Mb.

#### Earlier attempts

Earliers attempts to create a separate 8-axes COLRv1 disign space, each with 3 masters expanded the project to too many masters.

Generating the 6 different Bitcount VF flavours of about 8Mb, each of the 6 design spaces needs over 100Gb of free space in the _masters/ folder for the 873 expanded pixel UFO’s files (3x2x12x2 + 3x3x3x3x3x3, with 3 masters on the COLRv1 axes), each with a size over 100Mb.


### TODO.md

An overview on future development and plans.

### TRADEMARKS.md

Bitcount is a registered trademark of TYPETR | Buro Petr van Blokland + Claudia Mens

Rotterdamseweg 150-d
2628AP Delft The Netherlands



### otf/

Exported TTF instance font files, ready to use.

### vf/

Exported Variable Font files.

