import re
import json
import os
from os.path import dirname, abspath
from subprocess import check_output
import pytest

from test_byhand import read_api_list

DATADIR = dirname(abspath(__file__)) + "/data/"

if 'MGRKEY' in os.environ:
    MGRKEY = os.environ['MGRKEY']
else:
    assert False, "This test does not work without MGRKEY"

APIS = read_api_list("API.server.list")

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_upload0(API_URL):
    CMD = '''curl -s -X POST -H "Authorization: mgrast " -F "upload=@{}/metadata.simple.xlsx" "{}/inbox"'''.format(DATADIR, API_URL)
    print(CMD)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"authentication fail" in o
    assert b"ERROR" in o

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_upload_auth0(API_URL):
    CMD = '''curl -s -X POST -H "auth: {}" -F "upload=@{}/metadata.simple.xlsx" "{}/inbox"'''.format(MGRKEY, DATADIR, API_URL)
    print(CMD)
    o = check_output(CMD, shell=True)
    print(o)
    assert b"authentication fail" not in o
    assert b"ERROR" not in o

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_upload1(API_URL):
    CMD = '''curl -s -X POST -H "Authorization: mgrast {}" -F "upload=@{}/metadata.simple.xlsx" "{}/inbox"'''.format(MGRKEY, DATADIR, API_URL)
    print(CMD)
    o = check_output(CMD, shell=True)
    print(o)

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_upload_and_validate(API_URL):
    CMD = '''curl -s -X POST -H "Authorization: mgrast {}" -F "upload=@{}/metadata.simple.xlsx" "{}/inbox"'''.format(MGRKEY, DATADIR, API_URL)
    print(CMD)
    o = check_output(CMD, shell=True)
    assert b"ERROR" not in o
    j = json.loads(o)
    ID = re.findall(r"\((.*)\)", j["status"])[0]
    print(ID)
    assert "metadata.simple.xlsx" in j["status"]
    CMD = '''curl -X GET -H "Authorization: mgrast {}" "{}/inbox/validate/{}"'''.format(MGRKEY, API_URL, ID)
    o2 = check_output(CMD, shell=True)
    assert b"ERROR" not in o2
    j2 = json.loads(o2)
    assert j2["status"] == "valid metadata"


@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_fastq_upload_and_validate(API_URL):
    CMD = '''curl -s -X POST -H "Authorization: mgrast {}" -F "upload=@{}/Sample.DM.fastq.gz" "{}/inbox"'''.format(MGRKEY, DATADIR, API_URL)
    print(CMD)
    o = check_output(CMD, shell=True)
    assert b"ERROR" not in o
    j = json.loads(o)
    ID = re.findall(r"\((.*)\)", j["status"])[0]
    print(ID)
    assert "Sample.DM.fastq" in j["status"]
    CMD = '''curl -X GET -H "Authorization: mgrast {}" "{}/inbox/stats/{}"'''.format(MGRKEY, API_URL, ID)
    o2 = check_output(CMD, shell=True)
    print(o2)
    j2 = json.loads(o2)
    assert "status" in j2.keys()
    assert "timestamp" in j2.keys()
    assert "awe_id" in j2.keys()

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_searchapi_loggedin_morethan_loggedout(API_URL):
    return
#    CALL = '''curl -s -F "limit=5" -F "order=created_on" -F "direction=asc" -F "feature=building" "{}/search"'''.format(API_URL)
#    a = check_output(CALL, shell=True)
#    assert not b"ERROR" in a
#    b = a.decode("utf-8")
#    c = json.loads(b)
#    hits = c["total_count"]
#    CALL = '''curl -s -F "limit=5" -F "order=created_on" -F "direction=asc" -H "Authorization: mgrast {}" "{}/search"'''.format(MGRKEY, API_URL)
#    a = check_output(CALL, shell=True)
#    assert not b"ERROR" in a
#    b = a.decode("utf-8")
#    c = json.loads(b)
#    hits_loggedin = c["total_count"]
#    assert hits_loggedin >= hits

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_searchapi_loggedin_morethan_loggedoutb_pub1(API_URL):
    CALL = '''curl  -s -F "limit=5" -F "public=1" -F "order=created_on" -F "direction=asc" -F "feature=building" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    hits = c["total_count"]
    CALL = '''curl  -s -F "limit=5" -F "public=1" -F "order=created_on" -F "direction=asc" -H "Authorization: mgrast {}" "{}/search"'''.format(MGRKEY, API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    print(b)
    c = json.loads(b)
    hits_loggedin = c["total_count"]
    assert hits_loggedin >= hits

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_searchapi_loggedin_morethan_loggedoutb_pub0(API_URL):
    CALL = '''curl  -s -F "limit=5" -F "public=0" -F "order=created_on" -F "direction=asc" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    hits = c["total_count"]
    CALL = '''curl  -s -F "limit=5" -F "public=0" -F "order=created_on" -F "direction=asc" -H "Authorization: mgrast {}" "{}/search"'''.format(MGRKEY, API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    hits_loggedin = c["total_count"]
    assert hits_loggedin >= hits
