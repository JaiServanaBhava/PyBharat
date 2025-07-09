from setuptools import setup, find_packages

setup(
    name="pybharat",
    version="0.0.1",
    author="Jai Servana Bhava",
    author_email="jai005servanbhava@gmail.com",
    description="PyBharat is a cultural-flavored Python library that blends Indian heritage with powerful programming tools. It offers utilities, data, and functions rooted in India — from national symbols, festivals, and state details to greeting styles, traditional mantras, and more.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JaiServanaBhava/PyBharat",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
