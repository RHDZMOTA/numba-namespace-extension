from setuptools import setup, find_namespace_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
)
