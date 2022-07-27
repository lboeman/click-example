from setuptools import setup

setup(
    name="cli-example",
    version="0.0.1",
    pymodules=["cli"],
    install_required=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "cli-example = cli.main:cli",
        ],
    },
)
