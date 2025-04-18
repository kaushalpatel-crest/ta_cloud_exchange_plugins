"""
BSD 3-Clause License

Copyright (c) 2021, Netskope OSS
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""Okta CRE plugin constants."""

DEFAULT_WAIT_TIME = 60
MAX_RETRY_COUNT = 4
PLATFORM_NAME = "Okta"
MODULE_NAME = "CRE"
PLUGIN_VERSION = "1.1.0"
EVENTS_PROVIDER = "Netskope Security Events Provider"
ALLOWED_SCORE_LEVELS = ["none", "low", "medium", "high"]
PAGE_LIMIT_APP = 200
INTEGER_THRESHOLD = 4611686018427387904
OKTA_DATE_FORMAT = r"%Y-%m-%dT%H:%M:%S.%fZ"
USERS_ENTITY = "Users"
APPLICATIONS_ENTITY = "Applications"
USERS_FIELD_MAPPING = {
    "User ID": {"key": "id"},
    "Primary Email": {"key": "profile.email"},
    "Login Username (email)": {"key": "profile.login"},
    "Second Email": {"key": "profile.secondEmail"},
    "First Name": {"key": "profile.firstName"},
    "Last Name": {"key": "profile.lastName"},
    "Status": {"key": "status"}
}
APPLICATION_FIELD_MAPPING = {
    "ID": {"key": "id"},
    "Name": {"key": "name"},
    "Label": {"key": "label"},
    "Status": {"key": "status"},
    "SignOnMode": {"key": "signOnMode"},
}
NORMALIZATION_MAPPING = {
    "NONE": None,
    "LOW": 875,
    "MEDIUM": 625,
    "HIGH": 375,
}
