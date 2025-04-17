from setuptools import setup, find_packages

setup(
    name="alma",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    author="Aniketapu99",
    description="ALMA - Arnaud Legoux Moving Average for pandas",
)
