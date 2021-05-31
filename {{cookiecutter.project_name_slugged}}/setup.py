from setuptools import find_packages, setup

__package_name__ = "{{cookiecutter.project_name_snake}}"
__version__ = "0.0.1"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name=__package_name__,
    description="PySpark ETL Repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    packages=find_packages(exclude=("tests", "tests.*")),
    license="MIT",
    author="{{cookiecutter.author}}",
    install_requires=requirements,
    python_requires=">={{cookiecutter.python_version}}",
)
