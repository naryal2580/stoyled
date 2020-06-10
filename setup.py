from setuptools import setup, find_packages

with open("./README.md") as f:
    long_description = f.read()

setup(
    name='stoyled',
    version='0.6',
    author="Captain Nick Lucifer",
    author_email="naryal2580@gmail.com",
    url="https://github.com/naryal2580/stoyled",
    download_url='https://github.com/naryal2580/stoyled/tarball/master',
    description="Simple Fancy Standard Outputs for python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=['stoyled'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    python_requires='>=3',
 )
