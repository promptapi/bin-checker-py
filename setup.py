import pathlib

from setuptools import find_packages, setup

CURRENT_WORKING_DIRECTORY = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (CURRENT_WORKING_DIRECTORY / 'README.md').read_text(encoding='utf-8')

setup(
    name='pa-bin-checker',
    version='0.0.1',
    description="Python wrapper for Prompt API's BIN Checker API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/promptapi/bin-checker-py',
    author='Prompt API',
    author_email='hello@promptapi.com',
    license='MIT',
    python_requires='>=3.7',
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['tests']),
    extras_require={
        'development': ['vb-console'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='promptapi, bin, checker',
    install_requires=['requests'],
    project_urls={
        'Prompt API': 'https://promptapi.com',
        'BIN Checker API': 'https://promptapi.com/marketplace/description/bincheck-api',
        'Source': 'https://github.com/promptapi/bin-checker-py',
    },
)
