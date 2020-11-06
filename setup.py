from setuptools import find_packages, setup

setup(
    name='structoscope',
    packages=find_packages(include=['structoscope']),
    version='0.1.0',
    description='A Python library for visualizing and inspecting data structures',
    author='Matteo Sandrin',
    license='MIT',
    install_requires=['graphviz, Pillow'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
