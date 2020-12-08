from setuptools import setup, find_packages

setup(
    name="sipyco",
    version="1.1",
    author="M-Labs",
    url="https://m-labs.hk/artiq",
    description="Simple Python communications",
    license="LGPLv3+",
    install_requires=["setuptools", "numpy"],
    extras_require={
        "fast-b64": ["pybase64"],
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sipyco_rpctool = sipyco.sipyco_rpctool:main",
        ]
    },
)
