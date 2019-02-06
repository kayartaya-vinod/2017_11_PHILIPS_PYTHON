# setup.py

import setuptools

# python3 setup.py install

setuptools.setup(
    name = "mypack",
    version = "1.0.0",
    packages = ["mypack"],
    package_dir = {"mypack": "./mypack"},
    author="Vinod", 
    author_email="vinod@vinod.co", 
    maintainer="Vinod", 
    maintainer_email="vinod@vinod.co", 
    url="http://vinod.co", 
    description="The module numutils.numutils has a num2words(..) function.", 
    long_description="""The module numutils.numutils has a num2words(..) function.

To install this on you machine:

pip install numutils
python -m pip install numutils

If you are running behind a proxy,

python -m pip --proxy <<PROXY>> install numutils


Usage:..


...


    """, 
    license="MIT"
    )