"""setup.py file for the package ``dv_sounds``.
"""

import os
import sys
from setuptools import find_packages, setup

from dv_sounds import __version__, __test_version__


# Choose the correct version based on script's arg
if len(sys.argv) > 1 and sys.argv[1] == "testing":
    VERSION = __test_version__
    # Remove "testing" from args so setup doesn't process "testing" as a cmd
    sys.argv.remove("testing")
else:
    VERSION = __version__

# Directory of this file
dirpath = os.path.abspath(os.path.dirname(__file__))

# The text of the README file (used on PyPI)
with open(os.path.join(dirpath, "README.md")) as f:
    README = f.read()


setup(name='DV-Sounds',
      version=VERSION,
      description='Sounds for the Darth-Vader-RPi project',
      long_description=README,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
      ],
      keywords='Raspberry Pi sounds starwars Darth Vader',
      url='https://github.com/raul23/DV-RPi-Sounds',
      author='Raul C.',
      author_email='rchfe23@gmail.com',
      license='GPLv3',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False)
