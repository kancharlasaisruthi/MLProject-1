from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
# This is a setup file for a Python project that uses setuptools to manage dependencies and package information.
def get_requirements(file_path):
    """
    This function reads the requirements from a file and returns a list of packages.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    # Remove any leading/trailing whitespace characters and empty lines
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sruthi',
    author_email='saikancharla08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)