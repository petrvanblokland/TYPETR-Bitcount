# TYPETR-Bitcount
Bitcount VF


## TODO

* Generating all 6 standard VF with black pixels only
* Adding example images for documentation to generate BitcountReference.pdf again
* Implement COLv1 VF examples

## Nice to have

* Add Bitcount outline masters 

## Gradients

https://github.com/googlefonts/colr-gradients-spec

https://github.com/rsheeter/Bungee

## Axes specific for COLv1 fonts

fonts.google.com/variablefonts

https://github.com/google/fonts/tree/main/axisregistry

https://github.com/rosettatype/handjet#element-shape-axis-eshp

## Testing new ideas

https://github.com/MPEGGroup/OpenFontFormat

https://github.com/google/fonts/blob/main/CONTRIBUTING.md

https://github.com/googlefonts/gf-docs/tree/main/Spec

https://github.com/googlefonts/gf-docs/tree/main/Spec#upstream-repo-structure

## Building

Eindelijk een kleurenpixeldemo in elkaar gezet.

Net nog een uitbreiding gecommit.

~~~
_pixel.square is de glyph met pixel vorm

Maar _pixel.square is OOK een color glyph.
~~~

Glyph A tekent pixels op basis van de “gewone” pixelglyph. Elke pixel zou een individuele inkleuring kunnen krijgen.

Glyph B (maar ziet er uit als A...) tekent pixels op basis van de color pixelglyph. Elke pixel is dus een verwijzing naar dezelfde color pixel. Dit is efficienter als alle pixels hetzelfde behandeld worden.

Dat was het denk ik even voor nu. Roep maar als er iets niet duidelijk is.

Dit is een onmisbare referentie:

- https://github.com/googlefonts/colr-gradients-spec

En vergeet de readme niet:

- https://github.com/justvanrossum/pixel-color-font-demo


- Have a virtual environment set up with fontmake installed
- Run `./build_font.sh`
- Open `build/PixelColorDemo-VF.ttf` in FontGoggles


python -m venv venv --prompt=kleurdingest

source venv/bin/activate

pip install --upgrade pip

pip install fontmake

The "activate" step needs to be exceuted for every new terminal session.


python add_colrv1.py variable_ttf/BitcountGrid_Double4-VF.ttf
python build-black-pixel-Bitcount.py
python build-COLRv1-pixel-Bitcount.py

