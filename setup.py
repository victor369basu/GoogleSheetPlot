"""Setup for the GoogleSheetPlot package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Victor Basu",
    author_email="basu369victor@gmail.com",
    name='GoogleSheetPlot',
    license="MIT",
    description='GoogleSheetPlot is a python package allow the user to select a google sheet from their Google drive and plots a chart with the values on the sheet.',
    version='v0.0.00',
    long_description=README,
    url='https://github.com/victor369basu/GoogleSheetPlot',
    download_url = "https://github.com/victor369basu/GoogleSheetPlot/tree/master/dist/GoogleSheetPlot-0.0.0.tar.gz",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['requests',
                      'pandas',
                      'matplotlib',
                      'google-api-python-client',
                      'google-auth-httplib2',
                      'google-auth-oauthlib',
                      'pickle'
                     ],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
