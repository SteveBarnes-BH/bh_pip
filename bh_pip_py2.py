#!/usr/bin/env python2
# encoding:utf-8
"""
  Author:  Steve Barnes --<Steven.Barnes@bakerhughes.com>
  Purpose: Find & optionally set a proxy python 2 version
  Created: 26/09/2019

  The idea of this script is to try various proxy settings to
  locate the one that currently works and optionally set it as
  the default proxy for pip.
"""
from __future__ import print_function
import sys
import os
import re
import subprocess
import time
import urllib2
import zipfile
import tempfile

if sys.platform == "win32":
    import winreg

try:
    from build_info import BUILD_INFO
except Exception:
    BUILD_INFO = "Unknown"

from defaults import (DEFAULT_PAC_URLS, DEFAULT_PROXIES, DESCRIPTION)

_COPYRIGHT = """
BAKER HUGHES INTERNAL COPYLEFT LICENSE

Copyright (c) [2020] [Baker Hughes, Energy Innovation Center]

The Baker Hughes Internal Copyleft License is a free, copyleft license for software and other digital works.

The purpose is to promote internal open-source practices by ensuring Baker Hughes employees are supported, protected, and empowered while using and/or modifying internal software. The primary obligations are to share any modifications with the rest of the company and to not disclose covered works to persons or groups outside the company.

TERMS AND CONDITIONS

If you are an employee of Baker Hughes or one of its wholly owned subsidiaries (“BH”), you can access, modify, and use this software and its associated documentation (“Software”), free of charge, but subject to the following conditions:

The Software may only be disclosed to BH employees and subsidiaries.

The Software is used within BH as part of a research, development, component, service, product, etc.

The Software is not incorporated into other software, if the other software's title passes to a non-BH entity.

Any modifications to the Software do not incorporate BH trade secrets or other confidential materials.

Any modifications to the Software must be shared on a generally available internal platform.

Any modifications to the Software must include this same license document.

The consumer of this Software is responsible for verifying their application requirements, as there is no warranty, representation, or indemnity.

Divestitures and similar separations from BH require negotiation for usage and/or copies of the Software.

This license terminates if you or your employer separates from BH.
"""

ENVSTR = "https_proxy"
ENVSTR2 = "http_proxy"

if sys.platform == "win32":
    # The following will only work on Windows platforms
    def get_pac_urls_from_ie():
        """ Get the list of possible proxies from the IE settings."""
        auto_config_url = DEFAULT_PAC_URLS
        print("Checking for AutoConfigURL")
        a_reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        a_key = winreg.OpenKey(
            a_reg, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        )
        _, valuecount, _ = winreg.QueryInfoKey(a_key)
        for i in range(valuecount):
            try:
                name, val, _ = winreg.EnumValue(a_key, i)
                if name == "AutoConfigURL":
                    auto_config_url = val
            except EnvironmentError:
                return DEFAULT_PAC_URLS
        if isinstance(auto_config_url, list): # cope with multiple returns
            return auto_config_url
        return [
            auto_config_url,
        ]


else:
    # Non-Windows alternative
    def get_pac_urls_from_ie():
        """ On non windows platforms this isn't an option so use fixed """
        print("Not on Windows so using default pac file URL")
        return DEFAULT_PAC_URLS


def get_proxies_from_ie():
    """ Get the list of possible proxies from the IE settings."""
    proxy_re = re.compile(r'"PROXY\s+(.+:\d+).*"')
    proxy_list = []
    urls = get_pac_urls_from_ie()
    if urls is None:
        return proxy_list
    for url in urls:
        print("Getting Proxies from %s" % url)
        pac = ""
        try:
            pack = urllib2.urlopen(url, timeout=2)
            pac = pack.read().decode("utf-8")
            del pack
        except (IOError, urllib2.URLError):  # urllib.URLError:
            print("Failed to read from %s" % url)
        proxy_list.extend(proxy_re.findall(pac))
        for proxy in proxy_list:
            if not proxy.lower().startswith("http"):
                proxy_list.append("http://" + proxy)
    return list(set(proxy_list))


def getenv(no_env=False):
    """ Get a copy of the environment optionally removing ENVSTR. """
    myenv = os.environ.copy()
    removes = [ENVSTR.lower(), ENVSTR2.lower()]
    todel = []
    if no_env:
        for key in myenv.keys():
            if key.lower() in removes:
                todel.append(key)
    for key in todel:
        del myenv[key]
    return myenv


def get_pysocks():
    """ Conditionally Get PySocks. """
    container, final = os.path.split(__file__)
    if os.path.isfile(container):
        extract_pysocks(container)
    else:
        print(container, "is not a file.")


def extract_pysocks(container):
    """ Extract PySocks from container."""
    tempdir = tempfile.gettempdir()
    print("Trying to open", container)
    try:
        zfile = zipfile.ZipFile(container)
    except Exception as exc:
        print(exc)
        return
    filelist = [fn for fn in zfile.namelist() if fn.startswith("PySocks")]
    print(filelist)


def test_a_proxy_no_to(proxy, no_env=False):
    """ Test a single proxy."""
    result = -9
    myenv = getenv(no_env)

    print(" - Trying pip with --proxy=%s" % proxy, end=" ")
    sys.stdout.flush()
    commands = [
        sys.executable,
        "-mpip",
        "download",
        "semver",
        "--no-cache-dir",
        "--retries=2",
        "--proxy=%s" % proxy,
    ]
    try:
        fnull = open(os.devnull, "w")
        result = subprocess.check_call(
            commands,
            env=myenv,
            stdout=fnull,
            stderr=fnull,
            # timeout=10.0,
        )
    except (subprocess.CalledProcessError,):
        print("Fails!")
    else:
        if result == 0:
            print("Works!")
    sys.stdout.flush()
    return result == 0


def test_a_proxy(proxy, no_env=False):
    """ Test a single proxy."""
    myenv = getenv(no_env)
    result = "Not Tested"

    print(" - Trying pip with --proxy=%s" % proxy, end=" ")
    sys.stdout.flush()
    commands = [
        sys.executable,
        "-mpip",
        "search",
        "pip",
        "--retries=2",
        "--proxy=%s" % proxy,
    ]
    try:
        fnull = open(os.devnull, "w")
        proc = subprocess.Popen(commands, env=myenv, stdout=fnull, stderr=fnull,)
        tries = 0
        while tries < 150 and proc.poll() is None:
            time.sleep(0.10)
            tries += 1
        result = proc.returncode
        # print(repr(result))
        if result is None:
            result = "Timeout Expired"
            proc.kill()
    except subprocess.CalledProcessError:
        print("Fails! [Error]")

    if result == 0:
        print("Works!")
    else:
        print("Fails! Returned:", result)
    sys.stdout.flush()
    return result == 0


def test_proxies(no_env=False, use_defaults=False):
    """ Test the proxies and return those that work. """
    working = []
    if use_defaults:
        proxy_list = DEFAULT_PROXIES
    else:
        proxy_list = [
            "",  # Start with no command line proxy
        ]
        proxy_list.extend(get_proxies_from_ie())
    if no_env:
        print(
            "Trying as if:\n\tSET %s=\n\tSET %s=\nhad been done!"
            % (ENVSTR.upper(), ENVSTR2.upper()),
        )
    print("Trying %d possible proxies!" % len(proxy_list))
    sys.stdout.flush()
    working = [proxy for proxy in proxy_list if test_a_proxy(proxy, no_env)]
    if working and no_env:
        print("Now works suggest changing environment proxies")
    sys.stdout.flush()
    return working


def report_working(working, set_no_env):
    """ Report which proxies are working."""
    print("\nWorking Proxies:")
    print("\n--proxy=", "\n--proxy=".join(working))
    if set_no_env:
        print("\n\nSuggest Clearing environmental proxies with:")
        for envsetting in [ENVSTR, ENVSTR2]:
            print("    SET %s= " % envsetting.upper())
        print("or equivelent!")
    print("N.B. It may be worth setting your pip default with:")
    proxy = working[0]
    if proxy:
        print("\tpip config set global.proxy %s" % proxy)
        print("conda may benefit from:")
        print("\tconda config --set proxy_servers.http" % proxy)
    else:
        print("\tpip config unset global.proxy")
    sys.stdout.flush()


def main(pause=False):
    """ The main function to find a working proxy and use it."""
    print(__file__)
    print("Build Info:", BUILD_INFO)

    set_no_env = False
    envs_found = False
    working = []
    for envsetting in [ENVSTR, ENVSTR2]:
        envprox = os.getenv(envsetting)
        if envprox:
            envs_found = True
            print("Testing %s from envionment:\n   " % envsetting, end=" ")
            sys.stdout.flush()
            if test_a_proxy(envprox):
                working.append(envprox)

    if not working:  # So try the proxies we can find
        working = test_proxies()

    if not working and envs_found:  # Still no but env settings found
        working = test_proxies(True)
        set_no_env = len(working) > 0
    if not working:  # So try the default proxies
        print("Testing Fallback Proxies")
        working = test_proxies(False, True)

    if not working and envs_found:  # Still no but env settings found
        working = test_proxies(True, True)
        set_no_env = len(working) > 0

    if working:
        errcode = 0  # OK!
    else:
        errcode = "No Working Proxies Found"

    if len(sys.argv) > 2 and working:
        print("Now trying your command(s)")
        myenv = getenv(set_no_env)
        proxy = working[0]
        print("Using: --proxy=%s" % proxy)
        sys.stdout.flush()
        commands = [sys.executable, "-mpip"]
        commands.extend(sys.argv[1:])
        commands.append("--proxy=%s" % proxy)
        errcode = subprocess.call(commands, env=myenv)

    if working:
        report_working(working, set_no_env)
    else:
        print(errcode)

    if pause:
        dummy = raw_input("Press enter to continue!")
    sys.exit(errcode)


if __name__ == "__main__":
    print("Python 2 Proxy Checker")
    if "--help" in sys.argv:
        print(DESCRIPTION)
    else:
        main()
