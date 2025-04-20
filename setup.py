from setuptools import setup, find_packages

setup(
    name="qbitaro",
    version="0.1.0",
    description="A lightweight quantum simulator for teleportation and superdense coding.",
    author="Satya Panda",
    author_email="colabre2020@gmail.com",
    url="https://github.com/colabre2020/qbitaro.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)
