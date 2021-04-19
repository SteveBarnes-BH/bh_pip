
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

DEFAULT_PAC_URLS = [
    "https://cloudproxy.setpac.ge.com/pac.pac",
    "http://myapps.setpac.ge.com/pac.pac",
]
DEFAULT_PROXIES = [
    "http://PITC-Zscaler-Americas-Alpharetta3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-Americas-Cincinnati3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-US-Milwaukee.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-EMEA-Amsterdam3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-ASPAC-Singapore3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-ASPAC-Bangalore3PR.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-ASPAC-Tokyo3PR.proxy.corporate.ge.com:80",
    "http://grc-americas-pitc-sanraz.proxy.corporate.gtm.ge.com:80",
    "http://grc-americas-sanra-pitc-wkcz.proxy.corporate.gtm.ge.com:80",
    "http://grc-americas-pitc-sanraz.proxy.corporate.gtm.ge.com:80",
    "http://PITC-Zscaler-Global-CloudHubs.proxy.corporate.ge.com:80",
    "http://PITC-Zscaler-AmericasZ.proxy.corporate.ge.com:80",
    "http://gateway.ge.zscalertwo.net:80",
]

DESCRIPTION = """
This utility tries to find the settings for pip to work from behind a proxy by:
 1. On Windows Platforms checking the settings for a .pac file the parsing it for
    possible proxies.
 2. On other platforms using a list of proxies that have worked in the past.
 3. Trying to use pip with the various proxies and environmental settings to
    download a small target file (the semver wheel).
 4. Telling the user the results.
"""
 