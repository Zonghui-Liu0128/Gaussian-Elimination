try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='mpm_la',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Environment for MPM assessment 3.",
      long_description="Environment for MPM assessement 3.",
      url='https://github.com/ese-msc-2021',
      author="Imperial College London",
      author_email='rhodri.nelson@imperial.ac.uk',
      packages=['mpm_la'])
