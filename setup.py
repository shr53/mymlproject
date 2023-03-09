from setuptools import find_packages,setup # Here find_packages will findout all the packages available in our application
from typing import List

#get_requirements function definition
HYPEN_E='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will reture list of requirements
    '''
    requirements=[] #list
    with open(file_path) as file_obj: #open the file path which is given
        requirements=file_obj.readlines() # To read the lines from the file
        requirements=[req.replace("\n","") for req in requirements] #replace \n with blank space

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements



#Below section will contain the metadata information about this application
setup(
#name of the application
name='mymlproject',
version='0.0.1',
author='Shivani Raval',
author_email='shivani20raval@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') #installation of all the required libraries

)


