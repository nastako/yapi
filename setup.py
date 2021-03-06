from distutils.core import setup

classifiers = ["Development Status :: Beta",
               "Intended Audience :: Developers",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               'Topic :: Software Development :: Libraries :: Python Modules',
]

try:
  long_description = open('README.md').read()
except:
  long_description = ""

setup(
    name='yapi',
    version='v1.1',
    packages=[''],
    url='http://www.ahmetkotan.com.tr',
    license='GPL',
    author='Ahmet Kotan',
    author_email='ahmtkotan@gmail.com',
    description='Python Youtube Data API v3',
    long_description=long_description,
    keywords="youtube data api"
)
