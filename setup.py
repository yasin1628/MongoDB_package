from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MongoDB_Connect',
    version='0.0.1',
    author='Yaseen AHmad',
    author_email='ahmadyaseen1628@gmail.com',
    description= 'A python package for conection with database',
    install_requires=get_requirements('./requirements_dev.txt'),
    url='https://github.com/yasin1628/MongoDB_package.git',
    project_url='https://github.com/yasin1628/MongoDB_package/issues',
    package_dir={"":"src"},
    packages=find_packages(where="src")
)