from setuptools import setup, find_packages

setup(
    name='wwPDB validation tests',
    version='0.1',
    url='https://github.com/berrisfordjohn/wwpdb_validation',
    author='John Berrisford',
    author_email='berrisfordjohn@gmail.com',
    test_suite='tests',
    zip_safe=True,
    packages=['wwpdb_validation'],
    install_requires=['requests',
                      'onedep_api>=0.15'
                      ],
)
