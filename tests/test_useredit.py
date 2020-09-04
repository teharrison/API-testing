 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from subprocess import check_output
import pytest

from test_byhand import read_api_list

if 'MGRKEY' in os.environ:
    MGRKEY = os.environ['MGRKEY']
else:
    assert False, "This test does not work without MGRKEY"

APIS = read_api_list("API.server.list")

@pytest.mark.requires_auth
@pytest.mark.editutf8
@pytest.mark.parametrize("API_URL", APIS)
def test_setusername_return(API_URL):
    CMD = '''curl -s -X PUT '{API_URL}/user/testinguser' -d "firstname=Tésting" -d "lastname=Üser"  -H "Authorization: mgrast {MGRKEY}"   '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    o = check_output(CMD, shell=True)
    assert b"ERROR" not in o
    j = json.loads(o)
    assert j["lastname"] == "Üser"  # unicode in json response
    CMD = '''curl -s -X PUT '{API_URL}/user/testinguser' -d "firstname=Testing" -d "lastname=User"  -H "Authorization: mgrast {MGRKEY}"   '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    o = check_output(CMD, shell=True)
    assert b"ERROR" not in o
    j = json.loads(o)
    assert j["lastname"] == "User"  # unicode in json response

@pytest.mark.requires_auth
@pytest.mark.editutf8
@pytest.mark.parametrize("API_URL", APIS)
def test_setusername_set(API_URL):
    CMD = '''curl -s -X PUT '{API_URL}/user/testinguser' -d "firstname=W" -d "lastname=Trimble dépr"  -H "Authorization: mgrast {MGRKEY}"   '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    print(CMD)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"ERROR" not in o
    j = json.loads(o)
    CMD = '''curl -s -X GET '{API_URL}/user/testinguser' -H "Authorization: mgrast {MGRKEY}" '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"ERROR" not in o
    j = json.loads(o)
    assert j["lastname"] == "Trimble dépr"  # unicode in follow-up query for user data

@pytest.mark.requires_auth
@pytest.mark.editutf8
@pytest.mark.parametrize("API_URL", APIS)
def test_setusername_set_u0141(API_URL):
    CMD = '''curl -s -X PUT '{API_URL}/user/testinguser' -d "firstname=Mikołaj" -d "lastname=Wiśniewski"  -H "Authorization: mgrast {MGRKEY}"   '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    print(CMD)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"ERROR" not in o
    j = json.loads(o)
    CMD = '''curl -s -X GET '{API_URL}/user/testinguser' -H "Authorization: mgrast {MGRKEY}" '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"ERROR" not in o
    j = json.loads(o)
    assert j["lastname"] == "Wiśniewski"  # unicode in follow-up query for user data
    assert j["firstname"] == "Mikołaj"
    CMD = '''curl -s -X PUT '{API_URL}/user/testinguser' -d "firstname=Test" -d "lastname=User"  -H "Authorization: mgrast {MGRKEY}"   '''.format(API_URL=API_URL, MGRKEY=MGRKEY)
    o = check_output(CMD, shell=True)

