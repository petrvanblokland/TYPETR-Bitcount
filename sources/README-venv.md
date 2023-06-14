## Create venv/ (Virtual environment) to run build.py

The **venv/** is not included into Github, it needs to be created in the local repository.

### Run in terminal:

~~~

cd sources/

mkdir venv
python -m venv venv --prompt=Bitcount

source venv/bin/activate

pip install --upgrade pip

pip install defcon
pip install fontbakery
pip install fontmake
pip install fontparts
pip install paintcompiler
pip install statmake
pip install ttfautohint-py
pip install brotli
pip install fontPens
pip install ufo2ft
pip install pillow

~~~

The "activate" step needs to be executed for every new terminal session.

### This is an essential reference:

* https://github.com/googlefonts/colr-gradients-spec

Don't for the README:

* https://github.com/justvanrossum/pixel-color-font-demo



