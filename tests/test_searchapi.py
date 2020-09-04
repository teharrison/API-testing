 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import check_output
import json

# subset of ~20 example invokations from the API-explorer page  (all GET)
# http://www.mg-rast.org/mgmain.html?mgpage=api
# mangled by hand into tests

API_URL = "http://api-dev.mg-rast.org"
def test_searchapi_marine_salt():
    CALL = '''curl  -F "limit=10" -F "order=created_on" -F "direction=asc" -F "biome=marine" -F "material=saline" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_us_marine():
    CALL = '''curl  -F "limit=5" -F "order=created_on" -F "direction=asc" -F "country=usa" -F "biome=marine" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_searchunicode():
    CALL = '''curl  -F "limit=5" -F "all=*é*" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 800  # There are at least this many.. 

def test_searchapi_hmp():
    CALL = '''curl  -F "limit=10" -F "order=created_on" -F "direction=asc" -F "project_name=hmp" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_big():
    CALL = '''curl  -F "limit=10" -F "order=created_on" -F "direction=asc" -F "project_name=hmp" -F "bp_count_raw=[1000000000 TO *]" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_country():
    CALL = '''curl  -F "limit=10" -F "order=created_on" -F "direction=asc" -F "sequence_type=mt" -F "country=uk OR france OR italy OR germany OR spain" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_animalgut():
    CALL = '''curl  -F "limit=10" -F "order=created_on" -F "direction=asc" -F "all=gut" -F "biome=animal" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_m5nr_accession():
    CALL = '''curl  -F "limit=5" -F "order=created_on" -F "direction=asc" -F "location=chicago" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_pi():
    CALL = '''curl  -F "limit=5" -F "order=created_on" -F "direction=asc" -F "PI_firstname=noah" -F "PI_lastname=fierer" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80

def test_searchapi_building():
    CALL = '''curl  -F "limit=25" -F "order=created_on" -F "direction=asc" -F "feature=building" "{}/search"'''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 80
