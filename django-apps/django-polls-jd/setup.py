from setuptools import setup, find_packages
import polls

setup(
    name='django-polls-jd',
    version=polls.__version__,
    description='Django app to create Web-based polls.',
    author='JDRanpariya',
    author_email='jdpatel.code@gmail.com',
    include_package_data=True,
    url='',
    packeages=find_packages(),
    classifiers=[
        'Develpement Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],

)
