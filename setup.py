from setuptools import setup, find_packages
from pathlib import Path


# Read the long description from README.md
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8")

# Read install requirements
reqs_path = Path(__file__).parent / "reqs.txt"
install_requires = reqs_path.read_text(encoding="utf-8").splitlines()

setup(
    name="markdowner",
    version="0.1.0",
    description="\
        A Python package to automate your project/repo README file builds.\
    ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="James Reeves",
    author_email="james@codebrojim.com",
    url="https://github.com/CodeBroJim/markdowner",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "md=readme_builder.main:cli",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
