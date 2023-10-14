from setuptools import setup

setup(
    name="ldaprelayscan",
    version="1.0.0",
    description="Check for LDAP protections regarding the relay of NTLM authentication.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/zyn3rgy/LdapRelayScan",
    install_requires=[
        "asn1crypto==1.5.1",
        "asyauth==0.0.13",
        "asysocks==0.2.5",
        "cffi==1.15.1",
        "cryptography==41.0.3",
        "dnspython==2.4.2",
        "ldap3==2.9.1",
        "minikerberos==0.4.0",
        "msldap==0.4.7",
        "oscrypto==1.3.0",
        "prompt-toolkit==3.0.39",
        "pyasn1==0.5.0",
        "pycparser==2.21",
        "pycryptodomex==3.18.0",
        "pycryptodome==3.18.0",
        "six==1.16.0",
        "tqdm==4.66.1",
        "unicrypto==0.0.10",
        "wcwidth==0.2.6",
        "winacl==0.1.7"
    ],
    packages="",
    python_requires='>=3.6',
    entry_points={
    'console_scripts': [
        'ldaprelayscan=LdapRelayScan:main',
        ]
    }
)