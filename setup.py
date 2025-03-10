from setuptools import setup, find_packages

setup(
    name="clihttp",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "clihttp=clihttp.cli:main",  # CLI command
        ],
    },
    author="K5HV",
    description="A simple Python module to make HTTP requests using command line.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kshvsec/clihttp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
