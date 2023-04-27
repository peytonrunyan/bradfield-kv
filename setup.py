from setuptools import setup, find_packages

setup(
    name="kvstore",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.4.0",
    ],
    entry_points={
        "console_scripts": [
            "kv = kvstore.cli:main",
        ],
    },
)