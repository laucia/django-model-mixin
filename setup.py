from setuptools import setup, find_packages
import modelmixin
setup(
    name='django-model-mixin',
    version=modelmixin.__version__,
    description='Useful and common Django Model mixins',
    author='Lauris Jullien',
    author_email='lauris.jullien@gmail.com',
    url='http://github.com/laucia/django-model-mixin/',
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
