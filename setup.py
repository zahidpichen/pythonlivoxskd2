from setuptools import setup, find_packages

setup(
    name='python-livoxsdk2',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Python wrapper for Livox SDK2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/python-livoxsdk2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pybind11>=2.6.0',
        'numpy>=1.19.0',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)