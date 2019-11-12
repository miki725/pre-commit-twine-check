import os

from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), "rb") as fid:
        return fid.read().decode("utf-8")


setup(
    name="pre-commit-twine-check",
    description="twine check pre-commit-hook",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    url="https://github.com/miki725/pre-commit-twine-check",
    license="MIT",
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=["twine"],
    entry_points={"console_scripts": ["twine-check = twine_check.__main__:main"]},
    keywords=" ".join(["twine", "pre-commit"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
    ],
)
