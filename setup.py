from setuptools import find_packages
from setuptools import setup

setup(
    name='pre_commit_hooks',
    description='Some out-of-the-box hooks for pre-commit.',
    version='1.0.0',
    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'flake8'
    ],
    classifiers=[
            'License :: OSI Approved :: MIT License'
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
    ],
    extras_require={':python_version<"3.5"': ['typing']},
    entry_points={
        'console_scripts': [
            'reformat=pre_commits.reformat:main'
        ]
    }
)
