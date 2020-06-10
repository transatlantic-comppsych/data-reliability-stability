import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="reliability-stability-calc",
    version="0.0.4",
    author="Lily Eisner",
    author_email="lillian.eisner@gmail.com",
    description="Calculation for relibability and stability three data sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nimh-mbdu/data-reliability-stability",
    #packages=setuptools.find_packages(),
    packages=['reliability_stability'],
    install_requires=[
        'pandas',
        'numpy',
        'nibabel',
        'Click'
    ],
    entry_points='''
        [console_scripts]
        parse_nidb_metadata=nidb_to_bids.parse_nidb_metadata:extract_nidb_metadata
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: POSIX",
    ],
)
