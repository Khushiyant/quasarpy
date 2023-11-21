import os
from setuptools import setup, find_packages
import quasar


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fobj:
    readme = fobj.read()

setup(name='quasar',
      version=quasar.__version__,
      author='Khushiyant',
      author_email='khushiyant2002@gmail.com',
      project_urls={
        'Source': '',
      },
      license='GNU',
      description='Python Smell Detector for Python',
      platforms='any',
      long_description=readme,
      packages=find_packages(),
      
      entry_points={
          'console_scripts': ['quasar = quasar:main'],
          'setuptools.installation': [
              'eggsecutable = quasar:main',
          ],
      },
      keywords='static analysis code complexity metrics',
      classifiers=[
          'Development Status :: 1 - Ideation',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: GNU License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Utilities',
      ]
)