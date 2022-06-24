from setuptools import find_packages
from setuptools import setup

setup(
    name='rackfan',
    description='CLI utility to control NZXT grid+ fan',
    long_description=open('README.md').read(),
    url='https://github.com/anroots/rackfan',
    project_urls={
        'Source Code': 'https://github.com/anroots/rackfan'
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    setup_requires='setuptools',
    packages=find_packages(exclude=['tests*']),
    version='0.2.0',
    author='Ando Roots',
    author_email='ando@sqroot.eu',
    install_requires=[
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'rackfan = rackfan.rackfan:main',
        ],
    },
)