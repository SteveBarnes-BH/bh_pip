# About GE_Pip

## Why does it exist?

GE_Pip grew out of problems within the company exepericed with running the 
[python pip](https://en.wikipedia.org/wiki/Pip_(package_manager) tool to install and
update python packages _(mostly hosted at the Python Package Index <https://pypi.org/>)_.

These issues stem from the fact that the company uses various proxy settings which differ between:
 - Company Devisions
 - User Settings
 - Connection method, i.e.:
   - Internal LAN, 
   - Internal WiFi
   - F5
   - VPN
 - Peridic updates by the Corporate & Devision networking & IT teams.
 - _It sometimes seemed the colour of the users socks_

This led to various methods of attemping to bypass the problems upto and including some users
connecting their machines directly to the internet via mobile devices _a security risk in itself_ and
a __lot__ of wasted time.

It was eventually realised that the users ability to browse the web wasa controlled by an online  file called
`pac.pac` the URL of which was set within the Internet Explorer settings and the exact version of which was available
depended on the factors above, _(probably not the socks)_.

Manually fetching and parsing this file was not for everybody so GE_Pip was born.

## What does it do?

When GE_Pip.py is executed it follows the following process:

 1. Query the local internet explorer settings for the URL of the proxy configuration file.
 1. Fetch that file if possible.
 1. Scan it for all of the things that look like they might be proxy URLs
 1. For each of those proxy URLs try a pip command that requires a valid connection and report the result
 1. If no working connections were found try overriding a couple of environmental variables that have had an immpact in the past and try again.
 1. If still no valid connections try a set of fallback URLs that have worked in the past.
 1. If any valid connections were found:
   1. advise the user how to set these as default __but do not make and changes__.
   1. if additional operations were specified try to perform these.
 1. If none then tell the user.

## Running GE_Pip

### Running without additional operations

Running `GE_Pip.py` relies on you having `python` installed which since you are trying to use `pip` is a near cert!


To run it open a command prompt e.g. _Windows-R_ `cmd` on Windows and type:
```sh
python GE_Pip.py
```
If your associations are set you should be also able to simply double click in the file.

#### Example output:
```sh
Build Info: Built: 2021-01-14T15:58:38.048565 by 212303160
Checking for AutoConfigURL
Auto Config URL ['https://cloudproxy.setpac.ge.com/pac.pac', 'http://myapps.setpac.ge.com/pac.pac']
Getting Proxies from https://cloudproxy.setpac.ge.com/pac.pac
Save pack to pac_2021-01-16_08_04_14.708006.pac
Getting Proxies from http://myapps.setpac.ge.com/pac.pac
Save pack to pac_2021-01-16_08_04_15.132737.pac
Trying 9 possible proxies!
 - Trying pip with --proxy= Works!
 - Trying pip with --proxy=exol.proxy.ge.com:80 Fails! Returned: [Timeout]
 - Trying pip with --proxy=http://adproxy.o365.ge.com:443 Fails! Returned: [Error]
 - Trying pip with --proxy=adproxy.o365.ge.com:443 Fails! Returned: [Error]
 - Trying pip with --proxy=http://PITC-Zscaler-EMEA-London.proxy.bakerhughes.com:80 Works!
 - Trying pip with --proxy=PITC-Zscaler-EMEA-London.proxy.bakerhughes.com:80 Works!
 - Trying pip with --proxy=http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.ge.com:80 Works!
 - Trying pip with --proxy=PITC-Zscaler-EMEA-London3PR.proxy.corporate.ge.com:80 Works!
 - Trying pip with --proxy=http://exol.proxy.ge.com:80 Fails! Returned: [Timeout]

Working Proxies:

--proxy=
--proxy=http://PITC-Zscaler-EMEA-London.proxy.bakerhughes.com:80
--proxy=PITC-Zscaler-EMEA-London.proxy.bakerhughes.com:80
--proxy=http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.ge.com:80
--proxy=PITC-Zscaler-EMEA-London3PR.proxy.corporate.ge.com:80
N.B. It may be worth setting your pip default with:
        pip config unset global.proxy
GE_pip has dowloaded a semver wheel that you may wish to delete
Press enter to continue!
```

_The exact output that you receive will depend on the required settings of course._

### Running with additional operations

You can specify any valid pip command and if at least one working set of settings is found the command will
be attempted with those settings. This is handy if you are not in your usual environment and do not wish to change
any settings. An example wouuld be:
```cmd
python GE_Pip.py list -o
```
To list all outdated packages or

```cmd
python GE_Pip.py install -U ipython
```

## Which python & platform will it work on?

It is currently tested on Windows 10 with Python 32 & 64 bit with pythons 3.7, 3.8 & 3.9 but has been tested in the past with:

 - Windows 7 & 10 Python 2.6 through 2.7.13, 32 & 64 Bit.
 - Window 7 Python 3.5 through 3.7 32 & 64 Bit.
 - Windows 10 Python 2.7 32 bit
 - Windows 10 Python 3.8-3.9 32 & 64 Bit.
Note that it is compatible with the [Windows Python Launcher](https://docs.python.org/3/using/windows.html#launcher) `py.exe`

It has beeen tested and reported to work with reduced functionallity on both Linux  & OS-X platforms.

## Why doesn't it look like python in an editor or file viewer?

The actual GE_Pip.py file is infact a zip file containing both Python 2 & 3 versions of the code. This zip file is structed so that 
python can execute it directly, _Python has had this ability since version 2.6_. You can extract the source code if you wish.

## Where does it live?

Currently the home page for GE_Pip is: <https://github.build.ge.com/GE-Pip-Maintainers/ge_pip> this should be used for problem reporting.