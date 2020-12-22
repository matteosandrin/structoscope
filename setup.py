from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='structoscope',
    packages=find_packages(include=['structoscope']),
    version='0.2.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A Python library for visualizing and inspecting data structures',
    url="https://github.com/matteosandrin/structoscope",
    author='Matteo Sandrin',
    license='MIT',
    install_requires=['graphviz', 'Pillow', 'matplotlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
