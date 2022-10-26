from setuptools import find_packages
from setuptools import setup
from certbot_dns_ecenter.__version__ import VERSION


install_requires = [
    'certbot>=1.23.0',
    'setuptools>=39.0.1',
]

docs_extras = [
    'Sphinx>=1.0',
    'sphinx_rtd_theme',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='certbot-dns-ecenter',
    version=VERSION,
    description="Edge-Center DNS Authenticator plugin for Certbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Edge-Center/ec-dns-certbot-plugin',
    author="Edge-Center",
    author_email='support@edgecenter.ru',
    license='Apache License 2.0',
    python_requires='>=3.8',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-ecenter = certbot_dns_ecenter.dns_ecenter:Authenticator',
        ],
    },
)
