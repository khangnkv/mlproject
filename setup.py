from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',  # Change to your project name
    version='0.1.0',  # Set an appropriate version
    description='A Machine Learning Project with Deep Learning and Data Visualization',
    long_description=open('README.md').read(),  # Reads the content of README.md
    long_description_content_type='text/markdown',  # Make sure README is in markdown format
    author='Khang Vinh Khac Nguyen',
    author_email='khangnkv@gmail.com',  # Change to your email
    url='https://github.com/khangnkv/mlproject',  # Your GitHub repo URL
    packages=find_packages(),  # Automatically discovers your package
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Ensure you're targeting a compatible Python version
    install_requires= get_requirements("requirements.txt"),  # Add dependencies from requirements.txt
)
