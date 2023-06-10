from __future__ import annotations
from typing import TYPE_CHECKING
import io
import os
from setuptools import find_packages, setup

if TYPE_CHECKING:
    from typing import Any

install_requires = ["pillow"]

extras_require = {
    "test": ["pytest", "pytest-html"],
}


def read(*filenames, **kwargs):
    """Read contents of multiple files and join them together"""
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


pkg_info: dict[str, Any] = {}
exec(read("gadalang_imaging/__version__.py"), pkg_info)

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()


setup(
    name="gadalang-imaging",
    version=pkg_info["__version__"],
    author=pkg_info["__author__"],
    author_email=pkg_info["__author_email__"],
    url=pkg_info["__url__"],
    project_urls={
        "Bug Tracker": "https://github.com/gadalang/gadalang-imaging/issues",
        "Source Code": "https://github.com/gadalang/gadalang-imaging/",
    },
    description="Collection of nodes for image processing with gada",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    package_data={"gadalang_imaging": ["gada.yml"]},
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
