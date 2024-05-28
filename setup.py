from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='darkauth',
    version='1.0',
    author='Extahsi',
    author_email='losdiablostriple6@gmail.com',
    description='A package for authentication and web automation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/extahsi/darkauth",
    packages=find_packages(),
    install_requires=[
        'passlib',
        'selenium',
        'twilio',
        'numpy',
        'scikit-learn',
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
