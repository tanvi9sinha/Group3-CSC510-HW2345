from setuptools import setup

setup(
    name='Group3-CSC510-HW2345',
    version='0.1',
    description='Homework-Github repository',
    author='Shreya Maheshwari',
    author_email='smahesh4@ncsu.edu',
    packages=['src', 'tests', 'data'],
        long_description="""\
            Creating github repository files.
            .gitignore
            CODE-OF-CONDUCT.md
            CONTRIBUTING.md
            LICENSE.md
            CITATION.md
            INSTALL.md
            README.md
            setup.py
            src/
              __init__.py
              Cols.py
              Data.py
              Num.py
              Row.py
              Sym.py
              cli.py
              main.py
              misc.py
            data/
              __init__.py
              data.csv
            tests.py
              __init__.py
              test_engine.py
        """,
        classifiers=[
            "License :: MIT License",
            "Programming Language :: Python",
            "Development Status :: Planning",
            "Intended Audience :: Developers",
            "Topic :: Software Engineering (CSC510)",
        ],
        keywords='requirements license python gitignore',
        license='MIT',
        )

