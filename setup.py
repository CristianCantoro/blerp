from distutils.core import setup

setup(name='blerp',
      version='0.1',
      description='https://xkcd.com/1692/ --\n'
                  'blerp FILTERS LOCAL OR REMOTE FILES OR RESOURCES USING '
                  'PATTERNS DEFINED BY ARGUMENTS AND ENVIRONMENT VARIABLES. '
                  'THIS BEHAVIOR CAN BE ALTERED BY VARIOUS FLAGS.',
      author='Cristian Consonni, Randall Munroe',
      author_email='kikkocristian@gmail.com',
      depends=['docopt>=0.6.2'],
      url='https://github.com/CristianCantoro/blerp',
      scripts=['blerp']
      )
