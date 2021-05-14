from setuptools import setup, find_packages
classifiers = [
    'Development Status :: S - Production/Stable',
    'Intended Audience :: Education',
    'Operating system :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Pyhton :: 3.9'
]
setup(
    name='Calculator'
    version='0.0.1',
    description='Please read the README file'
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read()
    url=''
    author='Advait Shiralkar',
    author_email=''
    License='MIT'
    classifiers=classifiers,
    keywords='calculator'
    packages=find_packages()
    install_requires['']
)
    
