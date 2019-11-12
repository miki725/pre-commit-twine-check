#!/usr/bin/env python
import os
import pathlib
import shutil
import subprocess
import sys


def shell(cmd):
    print(f"+ {cmd}")
    try:
        return subprocess.check_output(cmd, shell=True).decode("utf-8")
    except Exception as e:
        print(e.output.decode("utf-8"))
        sys.exit(1)


def main():
    try:
        shutil.rmtree("dist")
    except FileNotFoundError:
        pass
    print(shell("python setup.py sdist"))
    distribution = [i for i in pathlib.Path("dist").iterdir() if i.is_file()][0]
    print(shell(f"twine check {distribution}"))


if __name__ == "__main__":
    main()
