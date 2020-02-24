#!/usr/bin/env python2
# encoding:utf-8
"""
  Author:  Steve Barnes --<Steven.Barnes@bhge.com>
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

if sys.platform == "win32":
    import winreg


_COPYRIGHT = """
    Baker Hughes Confidential
    [Unpublished] Copyright 2019-2020.  Baker Hughes LLC.

    NOTICE:  All information contained herein is, and remains the property of
    Baker Hughes LLC, its suppliers, and affiliates, if any.
    The intellectual and technical concepts contained herein are proprietary to
    Baker Hughes LLC and its suppliers and affiliates and may be
    covered by U.S. and Foreign Patents, patents in process, and are protected
    by trade secret and copyright law.
    Dissemination of this information or reproduction of this material is
    strictly forbidden unless prior written permission is obtained from
    Baker Hughes, LLC.
"""

ENVSTR = "https_proxy"


if sys.platform == "win32":
    # The following will only work on Windows platforms
    def get_pac_url_from_ie():
        """ Get the list of possible proxies from the IE settings."""
        auto_config_url = None
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
                pass
        return auto_config_url


else:
    # Non-Windows alternative
    def get_pac_url_from_ie():
        """ On non windows platforms this isn't an option so use fixed """
        print("Not on Windows so using default pac file URL")
        return "https://cloudproxy.setpac.ge.com/pac.pac"


def get_proxies_from_ie():
    """ Get the list of possible proxies from the IE settings."""
    proxy_re = re.compile(r'"PROXY\s+(.+:\d+).*"')
    proxy_list = []
    url = get_pac_url_from_ie()
    if url is None:
        return proxy_list
    print("Getting Proxies from %s" % url)
    pac = ""
    try:
        pack = urllib2.urlopen(url, timeout=2)
        pac = pack.read().decode("utf-8")
        del pack
    except (IOError, urllib2.URLError):  # urllib.URLError:
        print("Failed to read from %s" % url)
    proxy_list = proxy_re.findall(pac)
    for proxy in proxy_list:
        if not proxy.lower().startswith("http"):
            proxy_list.append("http://" + proxy)
    return proxy_list


def getenv(no_env=False):
    """ Get a copy of the environment optionally removing ENVSTR. """
    myenv = os.environ.copy()
    todel = []
    if no_env:
        for key in myenv.keys():
            if ENVSTR.lower() == key.lower():
                todel.append(key)
    for key in todel:
        del myenv[key]
    return myenv


def test_a_proxy_no_to(proxy, no_env=False):
    """ Test a single proxy."""
    result = -9
    myenv = getenv(no_env)

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
        FNULL = open(os.devnull, "w")
        result = subprocess.check_call(
            commands,
            env=myenv,
            stdout=FNULL,
            stderr=FNULL,
            # timeout=10.0,
        )
    except (subprocess.CalledProcessError,):  # subprocess.TimeoutExpired):
        print("Fails!")
    else:
        if result == 0:
            print("Works!")
    return result == 0


def test_a_proxy(proxy, no_env=False):
    """ Test a single proxy."""
    myenv = getenv(no_env)
    result = None

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
        FNULL = open(os.devnull, "w")
        proc = subprocess.Popen(
            commands,
            env=myenv,
            stdout=FNULL,
            stderr=FNULL,
            # timeout=10.0,
        )
        tries = 0
        while tries < 100 and proc.poll() is None:
            time.sleep(0.20)
            tries += 1
        result = proc.returncode
        # print(repr(result))
        if result is None:
            print("Fails! Timeout Expired")
            proc.kill()
            result = -42
        elif result != 0:
            print("Fails")
    except (subprocess.CalledProcessError,):  # subprocess.TimeoutExpired):
        print("Fails!")
    else:
        if result == 0:
            print("Works!")
    return result == 0


def test_proxies(no_env=False):
    """ Test the proxies and return those that work. """
    working = []
    proxy_list = [
        "",  # Start with no command line proxy
    ]
    proxy_list.extend(get_proxies_from_ie())
    print("Trying %d possible proxies!" % len(proxy_list))
    working = [proxy for proxy in proxy_list if test_a_proxy(proxy, no_env)]
    return working


def main(pause=False):
    """ The main function to find a working proxy and use it."""
    envprox = os.getenv(ENVSTR)
    set_no_env = False
    if envprox:
        print("Testing HTTPS_PROXY from envionment:\n   ", end=" ")
        sys.stdout.flush()
        if test_a_proxy(envprox):
            working = [envprox]
        else:
            working = test_proxies()
            if not working:
                print("Trying as if SET %s=" % ENVSTR.upper())
                sys.stdout.flush()
                working = test_proxies(True)
                if working:
                    set_no_env = True
                    print("Now works suggest using:")
                    print("    SET %s= " % ENVSTR.upper())
                    sys.stdout.flush()
    else:
        working = test_proxies()

    if working:
        errcode = 0  # OK!
    else:
        errcode = "No Working Proxies Found"

    if len(sys.argv) > 2 and working:
        myenv = getenv(set_no_env)
        proxy = working[0]
        print("Using: --proxy=%s" % proxy)
        sys.stdout.flush()
        commands = [sys.executable, "-mpip"]
        commands.extend(sys.argv[1:])
        commands.append("--proxy=%s" % proxy)
        errcode = subprocess.call(commands, env=myenv)

    if working:
        print("\nWorking Proxies:")
        print("\n".join(working))
        if set_no_env:
            print("\n\nSuggest Clearing %s with:" % ENVSTR)
            print("    SET %s= " % ENVSTR.upper())
        print("N.B. It may be worth setting your pip default with:")
        proxy = working[0]
        if proxy:
            print("\tpip config set global.proxy %s" % proxy)
        else:
            print("\tpip config unset global.proxy")

    if pause:
        inp = input("Press enter to continue!")
    sys.exit(errcode)


if __name__ == "__main__":
    main()
