from setuptools import setup

setup(name='jinjaninja',
      version='0.1.1',
      description='Jinja template style enforcement tool',
      url='https://github.com/ramonsaraiva/jinjaninja',
      author='Ramon Saraiva',
      author_email='ramonsaraiva@gmail.com',
      license='MIT',
      packages=['jinjaninja'],
      scripts=['jinjaninja/bin/jinja-ninja'],
      zip_safe=False)
