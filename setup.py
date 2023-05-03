
import io
import os
import re
from setuptools import setup

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
with open('androidguibot/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    install_requires=open(requirement_path,'r').read().replace("\r","").split("\n")
for idx,entry in enumerate(install_requires):
    cs = ""
    install_requires[idx]=""
    for ch in entry:
        if bytes(ch, "utf-8")!=b'\x00': # no idea why null byte, idgaf
            install_requires[idx]+=ch
print("Installation:")
print(install_requires)
setup(
    name='AndroidGuiBot',
    version=version,
    url='https://github.com/xmcp123/AndroidGUIBot',
    author='Mike',
    author_email='',
    description=('Framework for controlling Android emulator via screenshot/mouse/keyboard, or through ADB'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD',
    packages=['androidguibot'],
    install_requires=install_requires,
    test_suite='tests',
    keywords="gui automation android",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
