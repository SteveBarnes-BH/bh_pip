[![BH-INTERNAL-COPY-LEFT](https://img.shields.io/badge/license-BH--INTERNAL--COPY--LEFT-018374)](LICENSE.md) 
# ge_pip
A pip wrapper that does its best to cope with the BH proxy settings

Original Author: Steve Barnes (212303160) Steven.Barnes@BakerHughes.com 

## Licence: 
See [BH-INTERNAL-COPY-LEFT-LICENSE](LICENSE.md)

This code is free to use for all within the BH and Related Companies.
This code is supplied without any warranty and any support is given on an ad-hock basis.

This code should work with python 2.7 and >3.5

## Usage
This code can be used either as simply:

    python bh_pip.py

Where it will try to establish a working set of settings for pip and recommend them to you OR

    python bh_pip.py pip_comnads...

Where it will do the above then use the recommended settings to run the command(s). This is
useful when you don't wish to change your settings but need a one off run of pip but it is 
not working in the current situation.

## What & Why Is It?
The python `pip` package manager tool is a marvellous tool with the ability to perform a variety of
package maintainance activities. Of course to do many of these it needs to connect to the internet
so as to perform operations such as downloading and installing packages, checking the current status
of installed packages, etc. However, access to the internet is subject to a number of controls for
the sake of security, etc. The access to the internet from a corporate environment is generally via
"proxies" and the setting of these is generally hidden from users, controlled by various administators
and can be context dependent. 

The mechanisms for setting any machines proxy settings include:

 - Environmental Variables HTTP_PROXY & HTTPS_PROXY
 - Application Specific Settings _via configuration files or registry settings_
 - Centrally controlled scripts _specifically the JavaScript pac.pac file used by most browsers_

Which of these contains the current correct settings for the current moment in time can change depending on:
 - Machine specific settings
 - User settings
 - Admin settings _may change without the user knowing_
 - Which corporate group or company the user belongs to
 - How the user is logged on
 - Which pac.pac file is in use and its contents
 - How the user is connected - may be any of wired (in office), wireless (in office), home network, public network, mobile connection
 - Any tunnelling systems in use such as F5, MyApps, MyApps+, personal VPN, etc.
 
Additionaly pip has a number of mechanisms for picking up the settings to use, _with a non-inituative set of precidences_.

This all adds up to the potential for the users to often find that they cannot use pip which can block progress or lead to less than optimal maintainance & installation practices. Probably the number one topic of conversation in the Python Yammer groups within GE has been "pip is not working for me/us" and many hours of work have been lost attempting to resolve such issues. BH_pip was born out of this.

## How does it do what it does?
The possible proxy settings are taken from a number of sources, including whichever pac.pac file Internet Explorer would currently use, a list of historic proxies, etc..
Basically GE_pip simply tries pip search with various settings, starting from the current settings and each of the candidate proxies checks if it gets an error or not. If any of the proxy settings work then the user is informed which to use and how to do so. If none work then the same is tried with the environmental settings disabled.

Finally, _if the user supplied any pip commands_, those commands are executed with the working set of settings (if  any).

## Why & How does the published file support __both__ Python 2 & 3? 
The why is that some people & projects are still using python 2. The how is by having versions of the code for both variants and a `__main__.py` that invokes the appropriate one based on the executable in use. This could have been shipped as a package of multiple files or as a zip file. Python, however, can execute code from within a zip file, and will automatically run `__main__.py` within that file. Better yet it doesn't care about the file extension so changing the zip file extension to `.py` automatically associates the file with the system python on most platforms.

## Cross Platform Usage
GE_pip should work on non-Windows systems but it must be noted that it has not been tested by the author on any of them.
