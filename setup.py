from distutils.core import setup

setup(
    name="lxml-stubs",
    version="0.1",
    package_data={"lxml-stubs": ["*.pyi"]},
    packages=["lxml-stubs"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=False
)
