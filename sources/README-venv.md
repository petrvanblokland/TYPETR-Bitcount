
Dit is een onmisbare referentie:

- https://github.com/googlefonts/colr-gradients-spec

En vergeet de readme niet:

- https://github.com/justvanrossum/pixel-color-font-demo

mkdir venv
python -m venv venv 

- Have a virtual environment set up with fontmake installed
- Run `./build_font.sh`
- Open `build/PixelColorDemo-VF.ttf` in FontGoggles

cd TYPETR-Bitcount/sources

mkdir venv
python -m venv venv --prompt=Bitcount

source venv/bin/activate

pip install --upgrade pip

pip install defcon
pip install fontbakery
pip install fontmake
pip install ttfautohint-py
pip install brotli
pip install fontPens
pip install ufo2ft
pip install pillow

The "activate" step needs to be executed for every new terminal session.


python add_colrv1.py variable_ttf/BitcountGrid_Double4-VF.ttf
python build-black-pixel-Bitcount.py
python build-COLRv1-pixel-Bitcount.py


