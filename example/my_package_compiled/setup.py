from setuptools import setup, find_namespace_packages
from numba_namespace_extension.registry import Registry

setup(
    name="my_package_compiled",
    version="0.1.0",
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
    ext_modules=Registry.from_json("registry.json").ext_modules()
)
