# PyNameGen

[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=BBaoVanC/pynamegen)](https://dependabot.com)
[![CircleCI](https://circleci.com/gh/BBaoVanC/pynamegen/tree/master.svg?style=svg)](https://circleci.com/gh/BBaoVanC/pynamegen/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d8d75d1e33148d29c7224cdfb80749a)](https://www.codacy.com/manual/BBaoVanC/pynamegen?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BBaoVanC/pynamegen&amp;utm_campaign=Badge_Grade)

![PyPI](https://img.shields.io/pypi/v/pynamegen)
![PyPI - License](https://img.shields.io/pypi/l/pynamegen)

![GitHub issues](https://img.shields.io/github/issues-raw/BBaoVanC/pynamegen)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/BBaoVanC/pynamegen)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/BBaoVanC/pynamegen)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/BBaoVanC/pynamegen)

Robust CLI for [libnamegen](https://pypi.org/project/libnamegen/). Originally on my [NameGenerator](https://github.com/BBaoVanC/NameGenerator) project.

## Features

* Easy to use
* CLI with simple arguments
* Always tested before release
* Supports latest three versions of Python 3

---

## How to Install

Run the command `pip install pynamegen`. If you want to specify a specific Python version to use for pip, use a command such as `pip3` or `pip3.8`.

PyNameGen requires the packages [libnamegen](https://pypi.org/project/libnamegen/) and [libprogress](https://pypi.org/project/libprogress/), but those will automatically be installed by pip.

---

## FAQ

**What versions of Python are compatible?**

PyNameGen is built for Python 3. It is tested on the latest three versions on Python 3 by a few different continuous integration services.

---

## Documentation

### Command-Line Interface

Use defaults (100 names, debug enabled, classic method, write names to names.txt):

``` plaintext
$ pynamegen
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Show help menu (use any of the three options in brackets):

``` plaintext
$ pynamegen [--help | -h | help]
Usage:
    pynamegen [options]
Options:
    amt: Amount of names to generate
    debug: Whether or not to output debug information
    method: Which name generation method to use
Example:
    pynamegen amt=50 debug=True file=mynames.txt method=classic
```

Generate 250 names:

``` plaintext
$ pynamegen amt=250
Generating names...
[####################] 100% [250/250]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [250/250]...done
Saving file...
Finished!
```

Generate default amount of names with debug disabled:

``` plaintext
$ pynamegen debug=False
(no output)
```

Generate names and place in file usernames.txt:

``` plaintext
$ pynamegen file=usernames.txt
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Generate names and place in file users.txt inside the directory "example-names" **(Directory must already exist!)**

``` plaintext
$ pynamegen file=example-names/users.txt
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Generate 50 names with debug enabled and place in namelist.txt:

``` plaintext
$ pynamegen amt=50 debug=True file=namelist.txt
Generating names...
[####################] 100% [50/50]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [50/50]...done
Saving file...
Finished!
```

You can also generates the names to terminal output by setting the filename to `stdout`. If you do so, make sure to set debug to False! This makes it easy to use the CLI as a way to send generated names to a program without using the Python API.

Generate 5 names with the random method and output to terminal:

``` plaintext
$ pynamegen amt=5 method=random debug=False file=stdout
Kc3HcV3pq_n0
ncwUV_Twbx7s
jYs56B1y_WxU
YN5_cU6fhwXc
SI46Rnp9skAo
```

The output for the above command will differ because the generated names will not be the same as in this example.

The following example generates a name with the classic method and pipes it to the `cowsay` command (which just outputs text of a cow and a message box). You can pipe the generated name to any command; this is just an example.

``` plaintext
$ pynamegen amt=1 method=classic debug=False file=stdout | cowsay
 _______________________
< TheCauliflowerguy_408 >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

The default name generation method is `classic`, and looks like 'TheAssignmentanatorifier_90'.

The generation method `random` looks like 'XaYyaknkCoH8'.

You can change the generation method used by using the argument 'method=[method]' and replace [method] with the correct method.

``` plaintext
$ pynamegen method=random
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

If you choose `surprise` as the generation method, a generation method will be randomly selected.

``` plaintext
$ pynamegen method=surprise
Randomly selected method: classic
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

``` plaintext
$ pynamegen method=surprise
Randomly selected method: random
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

---

## License

_PyNameGen_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE`](https://github.com/BBaoVanC/pynamegen/blob/master/LICENSE)
