from setuptools  import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Docstring for get_requirements
    this function will return the list of requiremnets
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject_vithyaa',
version='0.0.1',
author='Vithyaa',
author_email='2005ckv@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),



)