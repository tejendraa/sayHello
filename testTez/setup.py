from setuptools import setup

setup(
    name='testTez', # pip install testTez
    description='api wrapper for testTez',
    long_description="long_description",
    version=0.1,
    author='Tejendra',
    author_email='tpareek32@gmail.com',
    url='https://github.com/tejendraa/sayHello/testTez',
    license='MIT',
    install_requires=['requests >= 2.6.0', ],
    py_modules=['testTez'],
    packages=['testTez'],
    zip_safe=False)