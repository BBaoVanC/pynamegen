import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynamegen",
    version="3.1.2.post2",
    author="BBaoVanC",
    author_email="pypi@bbaovanc.com",
    description="PyNameGen is a CLI for libnamegen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.bbaovanc.com/bbaovanc/pynamegen",
    packages=setuptools.find_packages(),
    scripts=["scripts/pynamegen"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'libprogress<4',
          'libnamegen<4',
    ],
    python_requires='>=3.7',
)
