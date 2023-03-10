from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''This fn will return list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
setup(
name='mlproject',#name of project
version='0.0.1',#whenever next update will come,automatic new packages will be built
author='Nilesh',
author_email='www.nilunaik1234@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')




)