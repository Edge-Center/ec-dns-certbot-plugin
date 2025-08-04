[![PyPI version](https://badge.fury.io/py/certbot-dns-ecenter.svg)](https://badge.fury.io/py/certbot-dns-ecenter)
[![Documentation Status](https://readthedocs.org/projects/ec-dns-certbot-plugin/badge/?version=latest)](https://ec-dns-certbot-plugin.readthedocs.io/en/latest/)
![Tests](https://github.com/Edge-Center/ec-dns-certbot-plugin/actions/workflows/ci.yml/badge.svg)
![Build](https://github.com/Edge-Center/ec-dns-certbot-plugin/actions/workflows/build.yml/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/Edge-Center/ec-dns-certbot-plugin)
![Code style: black](https://img.shields.io/github/license/Edge-Center/ec-dns-certbot-plugin)

The `certbot_dns_ecenter` plugin automates the process of
completing a `dns-01` challenge (`acme.challenges.DNS01`) by
creating, and subsequently removing, TXT records using the Edge-Center DNS
API.

Documentation
===============
For full documentation, including installation, examples, changelog please see [readthedocs page](https://ec-dns-certbot-plugin.readthedocs.io/en/latest/).

Install
===============

The plugin is not installed by default. It can be installed by command
below.

``` {.bash}
pip install certbot-dns-ecenter
```

Named Arguments
===============

| plugin flags | Description |
| ----------- | ----------- |
| `--dns-ecenter-credentials` | Edge-Center credentials INI file. (Required) |
| `--dns-ecenter-propagation-seconds` | The number of seconds to wait for DNS to propagate before asking the ACME server to verify the DNS record. (Default: 10) |


Credentials
===========

Use of this plugin requires a configuration file containing Edge-Center DNS
API credentials. You can use:
* Edge-Center API Token, obtained from your [profile panel](https://accounts.edgecenter.ru/profile/api-tokens)
or
* use Edge-Center Authentication credentials (email and password) for [login](https://auth.edgecenter.ru/login/signin) page.

Edge-Center API Token is **recommended** authentication option.

The token needed by Certbot for add temporary TXT record to zone what
you need certificates for.

Example `Edge-Center.ini` credentials file using restricted API Token (recommended)
```ini
# Edge-Center API token used by Certbot
dns_ecenter_apitoken = 0123456789abcdef0123456789abcdef01234567
```
Example `Edge-Center.ini` credentials file using authentication credentials (not recommended)
```ini
# Edge-Center API credentials used by Certbot
dns_ecenter_email = edge_center_user@example.com
dns_ecenter_password = 0123456789abcdef0123456789abcdef01234
```

The path to this file can be provided interactively or using the
`--dns-ecenter-credentials` command-line argument. Certbot records the
path to this file for use during renewal, but does not store the file\'s
contents.

> **WARNING**:
You should protect these API credentials as you would the password to
your Edge-Center account. Users who can read this file can use these
credentials to issue arbitrary API calls on your behalf. Users who can
cause Certbot to run using these credentials can complete a `dns-01`
challenge to acquire new certificates or revoke existing certificates
for associated domains, even if those domains aren\'t being managed by
this server.

Certbot will emit a warning if it detects that the credentials file can
be accessed by other users on your system. The warning reads \"Unsafe
permissions on credentials configuration file\", followed by the path to
the credentials file. This warning will be emitted each time Certbot
uses the credentials file, including for renewal, and cannot be silenced
except by addressing the issue (e.g., by using a command like
`chmod 600` to restrict access to the file).

Also you can override the default `api_url` or achieve even more flexibility
by specifying `auth` and `dns_api` urls separately.
Example `ecenter.ini` file:
```ini
# Edge-Center API urls used by Certbot
dns_ecenter_api_url = https://api.reseller.com
# implies that authapi available as /iam and dnsapi as /dns

# or
dns_ecenter_auth_url = https://api.example.org/iam
dns_ecenter_dns_api_url = https://dnsapi.example.com
```

Examples
========

To acquire a certificate for ``example.com``
```bash
certbot certonly --authenticator dns-ecenter --dns-ecenter-credentials=./ecenter.ini -d 'example.com'
```

To acquire a certificate for ``example.com``, waiting 80 seconds (recommended) for DNS propagation
```bash
certbot certonly --authenticator dns-ecenter --dns-ecenter-credentials=./ecenter.ini --dns-ecenter-propagation-seconds=80 -d 'example.com'
```

To acquire a ecdsa backed wildcard certificate for ``*.example.com``, waiting 80 seconds (recommended) for DNS propagation in isolated directory (e.g. as non-root user)
```bash
mkdir certbot && cd certbot
certbot certonly --authenticator dns-ecenter --dns-ecenter-credentials=./ecenter.ini --dns-ecenter-propagation-seconds=80 -d '*.example.com' --key-type ecdsa --logs-dir=. --config-dir=. --work-dir=.
```

For developers
========

How to run\develop plugin in docker
```bash
docker-compose run --rm --service-ports dev bash
# commands below run inside docker container
pip install -e .
touch ./ecenter.ini # add edgecenter dns api credentials
pip install certbot
certbot certonly --authenticator dns-ecenter --dns-ecenter-credentials=./ecenter.ini -d 'example.com'
```

Main docs file here: `certbot_dns_ecenter/__init__.py`
Build html docs files: `cd ./docs && sphinx-build -b html . _build/html`
Main plugin version here: `certbot_dns_ecenter/__version__.py`

How to run tests:
please see document `.github/workflows/ci.yml`
