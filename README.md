![Python](https://img.shields.io/badge/python-3.7.4-green.svg)
![Version](https://img.shields.io/badge/version-0.0.3-orange.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Prompt API - BIN Checker - Python Package

`pa-bin-checker` is a simple python wrapper for [bincheck-api][bincheck-api].

## Requirements

1. You need to signup for [Prompt API][promptapi-signup]
1. You need to subscribe [bincheck-api][bincheck-api], test drive is **free!!!**
1. You need to set `PROMPTAPI_TOKEN` environment variable after subscription.

then;

```bash
$ pip install pa-bin-checker
```

---

## Example Usage

```python
from bin_checker import get_bin

bin_information = get_bin('302596')  # example BIN
if bin_information.get('error', False):
    print(bin_information['bank_name'])  # you have a dict!
```

You’ll have a dict of data:

```python
{
    'bank_name': 'Diners Club International',
    'country': 'United States Of America',
    'url': 'www.dinersclub.com',
    'type': 'Credit',
    'scheme': 'Discover',
    'bin': '302596',
}
```

If you receive an error, payload will contain `error` key. Example error
response:

```python
{
    'error': 'You need to set PROMPTAPI_TOKEN environment variable',
}
```

---

## Development

Create your virtual environment, then use `rake` tasks:

```bash
$ rake -T

rake build           # Build package
rake bump[revision]  # Bump version
rake clean           # Remove/Delete build..
rake default         # Default task => :install
rake install         # Install package for local development purpose
rake test            # Run test
rake upload:main     # Upload package to main distro (release)
rake upload:test     # Upload package to test distro
```

To install and test package locally, just call `rake` or `rake install`.
Tests are available under `tests/` folder. Run `rake test` to run tests.

---

## License

This project is licensed under MIT

---

## Contributer(s)

* [Prompt API](https://github.com/promptapi) - Creator, maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/promptapi/bin-checker-py/fork)
1. Create your `branch` (`git checkout -b my-feature`)
1. `commit` yours (`git commit -am 'Add awesome features...'`)
1. `push` your `branch` (`git push origin my-feature`)
1. Than create a new **Pull Request**!

---

[bincheck-api]:     https://promptapi.com/marketplace/docs/bincheck-api
[promptapi-signup]: https://promptapi.com/#signup-form
