from setuptools import setup

setup(
    name='dariusVision',
    version='0.1',
    description='A package for computer vision',
    packages=['dariusVision'],
    install_requires=[
        'numpy',
        'opencv'
    ],
    author='gbox3d',
    author_email='gbox3d@gmail.com',
    url='https://github.com/yourusername/mypackage',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)