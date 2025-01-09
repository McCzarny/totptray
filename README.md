# totptray

[![Python package](https://github.com/McCzarny/totptray/actions/workflows/python-package.yml/badge.svg)](https://github.com/McCzarny/totptray/actions/workflows/python-package.yml)

https://pypi.org/project/totptray/

[![Build conda package](https://github.com/McCzarny/totptray/actions/workflows/conda-build.yml/badge.svg)](https://github.com/McCzarny/totptray/actions/workflows/conda-build.yml)

https://anaconda.org/mcczarny/totptray

## Description

A simple tray icon tool with a TOTP implementation. Creates a tray icon with a menu that allows to copy the current TOTP code for key passes to the script.

![Usage](/assets/usage.gif?raw=true)
## Usage
The tool expects one or more pairs in this format: `name=key`, e.g.:

```./totptray.py Google=000000000 Microsoft=000000000 TomTom=000000000```
