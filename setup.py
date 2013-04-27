from setuptools import setup

setup(
    name='django-feedme',
    version='0.1',
    packages=['feedme'],
    zip_safe = False,
    include_package_data=True,
    url='http://github.com/dstegelman/django-feedme',
    license='MIT',
    author='Derek Stegelman',
    author_email='email@stegelman.com',
    description='Django Google Reader Replacement',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
        ],
    install_requires = ['django_compressor==1.3']
    )