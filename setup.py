import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_deepracer_control_v2",
    version="0.1.4",
    author="jacobcantwell",
    author_email="jacob.cantwell.deepracer@gmail.com",
    description="aws_deepracer_control_v2 is a fork of awsdeepracer_control from lshw54",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jacobcantwell/aws_deepracer_control_v2",
    project_urls={
        "Bug Tracker": "https://github.com/jacobcantwell/aws_deepracer_control_v2/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4>=4.8.2",
        "bs4>=0.0.1",
        "lxml>=4.4.2",
        "PyYAML>=5.3",
        "requests>=2.22.0",
        "requests-toolbelt>=0.9.1",
        "urllib3>=1.25.8",
    ],
)