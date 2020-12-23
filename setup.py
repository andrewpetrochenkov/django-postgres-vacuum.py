import setuptools

setuptools.setup(
    name='django-postgres-vacuum',
    version='2020.12.24',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
