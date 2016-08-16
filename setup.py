from setuptools import setup, find_packages

setup(name='webserver',
      version='1.0.0',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'webserver = webserver.MichalWebServer:webserver_start'
          ]
      },
      )