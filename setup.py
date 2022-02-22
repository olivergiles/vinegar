from setuptools import find_packages
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='vinegar',
      version="1.0",
      description="CLI to convert data into pickled pandas DataFrames.",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown',
      entry_points='''
      [console_scripts]
      vinegar=vinegar.vinegar:vinegar
      ''')
