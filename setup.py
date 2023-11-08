from setuptools import setup
import re,io

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('twirp/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

with open('README.md', encoding='utf-8') as f:
      long_description = f.read().strip()

setup(name="twirp",
      version=__version__,
      description="Twirp server and client lib",
      long_description=long_description,
      long_description_content_type='text/markdown',
      licesnse='unlicense',
      packages=['twirp'],
      install_requires=[
            'requests',
            'structlog',
            'protobuf'
      ],
      test_requires=[
      ],
      zip_safe=False)
