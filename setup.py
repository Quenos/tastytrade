from setuptools import find_packages, setup


f = open('README.rst', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='tastytrade',
    version='8.0',
    description='An unofficial SDK for Tastytrade!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    author='Graeme Holliday',
    author_email='graeme.holliday@pm.me',
    url='https://github.com/tastyware/tastytrade',
    license='MIT',
    install_requires=[
        'requests<3',
        'websockets>=11.0.3',
        'pydantic>=2.6.3',
        'pandas_market_calendars>=4.3.3'
    ],
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True
)
