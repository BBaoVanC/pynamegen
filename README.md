# PyNameGen

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

The default name generation method is classic, and looks like 'TheAssignmentanatorifier_90'.

The generation method random looks like 'XaYyaknkCoH8'.

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

---

## License

_PyNameGen_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE.txt`](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
