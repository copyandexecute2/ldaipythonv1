from setuptools import setup

setup(
    name='LDAIpy',
    version='0.1',
    author='Theblockcraft',
    author_email='gabriel.deat.mc@gmail.com',
    description='Eine Erweiterung für LDAI, erstellt mit Python.',
    packages=['ldai'],
    install_requires=[
        'pyserial',
        'sys',
        'os',
        'tkinter',
        'command'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
