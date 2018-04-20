# Mojom Syntax Highlighting

This repository contains the code for syntax highlighting rules for Mojom
file for Sublime Text (and I guess editor that support .tmLanguage syntax).

## Building

The syntax files are written in YAML (easier to read and write than Plist
or JSON) and are converted to Plist format with the script in tools. The
script uses `ruamel.yaml` to parse the YAML file, so installing it first
is required to build.

If you have `pip` installed, then you can install it simply via:
```shell
$ pip install --user ruamel.yaml
```

Then, assuming you have GNU `make` installed, you can build by typing:
```shell
$ make Mojom.sublime-package
```

## Disclaimer

This is not an officially supported Google product.
