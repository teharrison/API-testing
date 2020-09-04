#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import json
import requests
import pytest
from test_byhand import read_api_list
APIS = read_api_list("API.server.list")

if 'MGRKEY' in os.environ:
    MGRKEY = os.environ['MGRKEY']
else:
    assert False, "This test does not work without MGRKEY"

def get_proj_metadata(proj, field, API_URL):
    '''Connect to MG-RAST API, authorize, and read project metadata.'''
    TESTURL = API_URL + "/project/{PROJ}".format(PROJ=proj)
    TESTDATA = {"verbosity":"full", "nocache":1}
    TESTHEADERS = {"Authorization": "mgrast {MGRKEY}".format(MGRKEY=MGRKEY)}
#    print(TESTURL, TESTDATA, TESTHEADERS)
    a = requests.get(TESTURL, headers=TESTHEADERS, params=TESTDATA)
    aa = json.loads(a.content.decode("utf-8"))
    assert "ERROR" not in a.content.decode("utf-8")
    return(field, aa["metadata"][field])

def set_proj_metadata(proj, terms, API_URL):
    '''Connect to MG-RAST API, authorize, and change one or more fields
    of project metadata.'''
    SETURL = API_URL + "/project/{PROJ}/updatemetadata".format(PROJ=proj)
    SETHEADERS = {"Authorization": "mgrast {MGRKEY}".format(MGRKEY=MGRKEY)}
    # Convert data into the pecuilar syntax needed for requests.post to send
    # multipart/form-data without files:
    SETDATA = {key : (None, val)  for key, val in terms.items()}
#    print(SETURL, SETHEADERS, SETDATA)
    b = requests.post(SETURL, headers=SETHEADERS, files=SETDATA)
    print(b.content.decode("utf-8"))

@pytest.mark.requires_auth
@pytest.mark.parametrize("API_URL", APIS)
def test_project_updatemetadata(API_URL):
    '''Update a field of project metadata, confirm its value,
    update it again (with utf-8) and confirm its value.'''
    PROJECT = "mgp89431"  # This project is a testing fixture
    FIELD = "organization_url"
    set_proj_metadata(PROJECT, {FIELD: "TESTING"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING"
    set_proj_metadata(PROJECT, {FIELD: "TESTING2"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING2"

@pytest.mark.requires_auth
@pytest.mark.editutf8
@pytest.mark.parametrize("API_URL", APIS)
def test_project_updatemetadata_with_utf8(API_URL):
    '''Update a field of project metadata, confirm its value,
    update it again (with utf-8) and confirm its value.'''
    PROJECT = "mgp89431"  # This project is a testing fixture
    FIELD = "organization_url"
    set_proj_metadata(PROJECT, {FIELD: "TESTING"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING"
    set_proj_metadata(PROJECT, {FIELD: "TESTING2"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING2"
    set_proj_metadata(PROJECT, {FIELD: "Tésting2"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "Tésting2"

@pytest.mark.requires_auth
@pytest.mark.editutf8
@pytest.mark.parametrize("API_URL", APIS)
def test_project_updatemetadata_with_utf8_U_0634(API_URL):
    '''Update a field of project metadata, confirm its value,
    update it again (with utf-8) and confirm its value.'''
    PROJECT = "mgp89431"  # This  proejct is a testing fixture
    FIELD = "organization_url"
    set_proj_metadata(PROJECT, {FIELD: "TESTING"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING"
    set_proj_metadata(PROJECT, {FIELD: "TESTING2"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "TESTING2"
    set_proj_metadata(PROJECT, {FIELD: "Testing ش"}, API_URL)
    f, v = get_proj_metadata(PROJECT, FIELD, API_URL)
    print(f, v)
    assert v == "Testing ش"
