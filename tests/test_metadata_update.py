#!/usr/bin/env python # -*- coding: utf-8 -*- from __future__ import print_function
import os
from os.path import dirname, abspath
import json
from subprocess import check_output
import pytest
import requests
from test_byhand import read_api_list

#  This tests the metadata/update API call, which requires carefully-constructed excel workbooks 

DATADIR = dirname(abspath(__file__)) + "/data/"

APIS = read_api_list("API.server.list")
if 'MGRKEY' in os.environ:
    MGRKEY = os.environ['MGRKEY']
else:
    assert False, "This test does not work without MGRKEY"

def metagenome_get(metagenome, API_URL):
    CALL = 'curl -s -X GET "{API_URL}/metagenome/{}?verbosity=full&nocache=1" -H "Authorization: mgrast {MGRKEY}"'.format(metagenome, API_URL=API_URL, MGRKEY=MGRKEY)
    print(CALL)
    h = check_output(CALL, shell=True) 
    b = json.loads(h.decode("utf-8"))
    assert "metadata" in b.keys(), b
    assert b["metadata"] is not None
    return(b["metadata"]) 

def metadata_get(metagenome, API_URL):
    CALL = 'curl -s -X GET "{API_URL}/metadata/export/{}?verbosity=full&nocache=1" -H "Authorization: mgrast {MGRKEY}"'.format(metagenome, API_URL=API_URL, MGRKEY=MGRKEY)
    print(CALL)
    metadata = {}
    h = check_output(CALL, shell=True) 
    b = json.loads(h.decode("utf-8"))
    return(b) 
 
def metadata_update(proj, filename, metagenome, API_URL):
    h = check_output('curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome={METAGENOME}" -F "project={PROJECT}"'.format(FILENAME=filename, MGRKEY=MGRKEY, PROJECT=proj, METAGENOME=metagenome, API_URL=API_URL), shell=True)
    assert "ERROR" not in h.decode("utf-8")
    b = json.loads(h.decode("utf-8"))
    assert "added" in b.keys(), b.keys()
    assert len(b["added"]) >= 1, b["added"]
    print("UPDATE RESPONSE", h)
    return(h)
 
def metadata_update(proj, filename, metagenome, API_URL):
    h = check_output('curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome={METAGENOME}" -F "project={PROJECT}"'.format(FILENAME=filename, MGRKEY=MGRKEY, PROJECT=proj, METAGENOME=metagenome, API_URL=API_URL), shell=True)
    assert "ERROR" not in h.decode("utf-8")
    b = json.loads(h.decode("utf-8"))
    assert "added" in b.keys(), b.keys()
    assert len(b["added"]) >= 1, b["added"]
    print("UPDATE RESPONSE", h)
    return(h)

@pytest.mark.parametrize("API_URL", APIS)
def test_metadata_update_comma(API_URL):
    CALL = 'curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome=mgm4845280.3,mgm4845282.3,mgm4845278.3" -F "project={PROJECT}"'.format(FILENAME=DATADIR+"FIXTURE-THREE-nounicode.xlsx", MGRKEY=MGRKEY, PROJECT="mgp89432", API_URL=API_URL)
    h = check_output(CALL, shell=True)
    assert "ERROR" not in h.decode("utf-8")
    # confirm first change
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    m = metadata_get("mgm4845278.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    # Change to BBB
    CALL = 'curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome=mgm4845280.3,mgm4845282.3,mgm4845278.3" -F "project={PROJECT}"'.format(FILENAME=DATADIR+"FIXTURE-THREE-nounicode2.xlsx", MGRKEY=MGRKEY, PROJECT="mgp89432", API_URL=API_URL)
#    print(CALL)
    h = check_output(CALL, shell=True)
    assert "ERROR" not in h.decode("utf-8")
    # confirm second change 
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB"
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB"
    m = metadata_get("mgm4845278.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB"

@pytest.mark.parametrize("API_URL", APIS)
def test_metadata_update_double(API_URL):
    h = check_output('curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome={METAGENOME}" -F "metagenome={MG2}" -F "project={PROJECT}"'.format(FILENAME=DATADIR+"FIXTURE-THREE-nounicode.xlsx", MGRKEY=MGRKEY, PROJECT="mgp89432", METAGENOME="mgm4845280.3", MG2="mgm4845282.3", API_URL=API_URL), shell=True)
    assert "ERROR" not in h.decode("utf-8")
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    h = check_output('curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/update" -H "Authorization: mgrast {MGRKEY}" -F "metagenome={METAGENOME}" -F "metagenome={MG2}" -F "project={PROJECT}"'.format(FILENAME=DATADIR+"FIXTURE-THREE-nounicode2.xlsx", MGRKEY=MGRKEY, PROJECT="mgp89432", METAGENOME="mgm4845280.3", MG2="mgm4845282.3", API_URL=API_URL), shell=True)
    assert "ERROR" not in h.decode("utf-8")
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB", m
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB", m 
#curl -X POST -F "upload=@FIXTURE-THREE-unicode.xlsx" "http://api.mg-rast.org/metadata/update" -H "Authorization: mgrast $MGRKEY"  -F "metagenome=mgm4514697.3" -F "project=mgp89432"

def metadata_import(metagenome, proj, filename, API_URL):
    h = check_output('curl -s -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/import" -H "Authorization: mgrast {MGRKEY}" -F "metagenome={METAGENOME}" -F "project={PROJECT}"'.format(FILENAME=filename, METAGENOME=metagenome, API_URL=API_URL, MGRKEY=MGRKEY, PROJECT=proj), shell=True)
    assert "ERROR" not in h.decode("utf-8")
    return(h)

#curl -X POST -F "upload=@mgp87606.xls" "http://api.mg-rast.org/metadata/validate"
def validate_metadata(filename, API_URL):
    h = check_output('curl -X POST -F "upload=@{FILENAME}" "{API_URL}/metadata/validate"'.format(FILENAME=filename, API_URL=API_URL), shell=True)
    return h

def get_proj_metadata(proj, field, API_URL):
    TESTURL = "{API_URL}/project/{PROJ}".format(API_URL=API_URL, PROJ=proj)
    TESTDATA = {"verbosity":"full", "nocache":1}
    TESTHEADERS = {"Authorization": "mgrast {MGRKEY}".format(MGRKEY=MGRKEY)}
#    print(TESTURL, TESTDATA, TESTHEADERS)
    a = requests.get(TESTURL, headers=TESTHEADERS, params=TESTDATA)
    aa = json.loads(a.content.decode("utf-8"))
    return(field, aa["metadata"][field])

def set_proj_metadata(proj, terms, API_URL):
    SETURL = API_URL + "/project/mgp119/updatemetadata"
    TESTHEADERS = {"Authorization": "mgrast {MGRKEY}".format(MGRKEY=MGRKEY)}
    # Convert data into the peculiar syntax needed for requests.post to send
    # multipart/form-data without files:
    SETDATA = {k : (None, v)  for k, v in terms.items()}
#    print(SETURL, SETHEADERS, SETDATA)
    b = requests.post(SETURL, headers=TESTHEADERS, files=SETDATA)
#    print(b.content.decode("utf-8"))

@pytest.mark.parametrize("API_URL", APIS)
@pytest.mark.requires_auth
@pytest.mark.utf8
def test_metadata_update_xls_nounicode(API_URL):
    FIXTURE = DATADIR+"/FIXTURE-ONE-nounicode.xlsx"
    PROJECT = "mgp89431"
    FIELD = "project_description"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845247.3", API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "No unicode here."
    FIXTURE = DATADIR+"/FIXTURE-ONE-nounicode2.xlsx"
    PROJECT = "mgp89431"
    FIELD = "project_description"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845247.3", API_URL)
    assert b"ERROR" not in h
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "No unicode2 here."

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
@pytest.mark.editutf8
def test_metadata_update_xls_unicode(API_URL):
    FIXTURE = DATADIR+"/FIXTURE-ONE-unicode.xlsx"
    PROJECT = "mgp89431"
    FIELD = "project_description"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845247.3", API_URL)
    assert b"ERROR" not in h
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "Unicóde test.  10μm in size.   CJK unlikely to work here."
    m = metadata_get("mgm4845247.3", API_URL)
    assert m["project"]["data"][FIELD]["value"] == "Unicóde test.  10μm in size.   CJK unlikely to work here."
    FIXTURE = DATADIR+"/FIXTURE-ONE-unicode2.xlsx"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845247.3", API_URL)
    assert b"ERROR" not in h
    e, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "UNICÓDE"
    m = metadata_get("mgm4845247.3", API_URL)
    assert m["project"]["data"][FIELD]["value"] == "UNICÓDE"

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
@pytest.mark.editutf8
def test_metadata_update_xls_two(API_URL):
    FIXTURE = DATADIR+"/FIXTURE-THREE-nounicode.xlsx"
    PROJECT = "mgp89432"
    FIELD = "PI_organization_address"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845280.3,mgm4845282.3,mgm4845278.3", API_URL)
    assert b"ERROR" not in h
    # Now verify that metadata has been set
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_AAA"
    FIXTURE = DATADIR+"/FIXTURE-THREE-nounicode2.xlsx"
    h = metadata_update(PROJECT, FIXTURE, "mgm4845280.3,mgm4845282.3,mgm4845278.3", API_URL)
    assert b"ERROR" not in h
    # Now verify that metadata has been set
    m = metadata_get("mgm4845280.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB"
    m = metadata_get("mgm4845282.3", API_URL)
    assert m["sample"]["data"]["misc_param"]["value"] == "TEST_BBB"

@pytest.mark.utf8
@pytest.mark.parametrize("API_URL", APIS)
def test_metadata_validate_xls_nounicode(API_URL):
    FIXTURE = DATADIR+"/FIXTURE-ONE-nounicode.xlsx"
    h = validate_metadata(FIXTURE, API_URL)
    print(h)
    assert b"authentication failed" not in h
    assert b"ERROR" not in h
    j = json.loads(h.decode("utf-8"))
    assert j["is_valid"] == 1

@pytest.mark.utf8
@pytest.mark.parametrize("API_URL", APIS)
def test_metadata_validate_xls_unicode(API_URL):
    FIXTURE = DATADIR +"/FIXTURE-ONE-unicode.xlsx"
    h = validate_metadata(FIXTURE, API_URL)
    print(h)
    assert b"authentication failed" not in h
    assert b"ERROR" not in h
    j = json.loads(h.decode("utf-8"))
    assert j["is_valid"] == 1
