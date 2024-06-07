from setuptools import setup, find_packages

setup(
    name='eduviz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'manim',  # et toutes autres dépendances nécessaires
        'numpy',
        'matplotlib',
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'eduviz=eduviz.cli:main',
        ],
    },
    author='Slainix',
    description='Un module Python pour créer des visualisations éducatives interactives.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/slainixgd/eduviz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
