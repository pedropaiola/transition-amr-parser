import os
from setuptools import setup, find_packages
try:  # for pip >=12
    from pip._internal.req import parse_requirements
    from pip._internal import download
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip import download

VERSION = '0.0.1'

install_reqs = parse_requirements(
    "requirements.txt", session=download.PipSession()
)
install_requires = [str(ir.req) for ir in install_reqs]

package_data = {}

setup(
    name='transition_amr_parser',
    version=VERSION,
    description="Trasition-based AMR parser tools",
    py_modules=['transition_amr_parser'],
    entry_points={
        'console_scripts': [
            'amr-learn = transition_amr_parser.learn:main',
            'amr-parse = transition_amr_parser.parse:main',
            'amr-oracle = transition_amr_parser.data_oracle:main'
        ]
    },
    packages=find_packages(),
    install_requires=install_requires,
    package_data=package_data,
)