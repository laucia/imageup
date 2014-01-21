from setuptools import setup, find_packages
 
setup(
    name='imageup',
    version='0.0.2',
    description='Basic Django admin image uploader',
    author='Lauris Jullien',
    author_email='lauris@captain-startup.com',
    url='http://github.com/laucia/imageup/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)