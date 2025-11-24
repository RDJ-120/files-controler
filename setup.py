from setuptools import setup, find_packages

setup(
    name="files-controler",
    version="0.1.0",
    author="Mazen Yasser",
    description="A simple Python library to control and manage files easily.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
)