from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Experimental project for Software Engineering",
      url="",
      author="Kieran Cosson",
      author_email="kieran.cosson@ucdconnect.ie",
      licence="MIT",
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )
