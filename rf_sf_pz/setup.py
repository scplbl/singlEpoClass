from setuptools import setup
setup(name='rf_sf_pz',
      version='0.1',
      description='Code that generates RF, SF and Photo-z plots',
      url='https://github.com/scplbl/lilys.class.src',
      author='Caroline Sofiatti',
      author_email='c.sofiatti@gmail.com',
      packages=['rf_sf_pz'],
      install_requirements=[
          'os.path',
          'numpy',
          'seaborn',
          'matplotlib.pyplot',
          'zIter',
          'load',
      ],
      zip_safe=False)