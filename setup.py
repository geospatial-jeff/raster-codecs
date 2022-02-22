from typing import List

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

inst_reqs: List[str] = ["numcodecs", "imagecodecs"]
dev_reqs: List[str] = ["pytest", "pytest-cov"]

extra_reqs = {
    "dev": dev_reqs,
}

setup(
    name="numcodecs-raster",
    version="0.1.0",
    python_requires=">=3.7",
    description="numcodecs-raster",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="raster zarr dask xarray numcodecs imagecodecs",
    author="Jeff Albrecht",
    author_email="geospatialjeff@gmail.com",
    url="https://github.com/geospatial-jeff/numcodecs-raster",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
