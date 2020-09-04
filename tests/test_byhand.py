# -*- coding: utf-8 -*-

import os
from subprocess import check_output
import json
import pytest


# These tests should be quick

# Rotate through API servers listed in API.server.list

def read_api_list(filename):
    server_list = []
    if not os.path.isfile(filename):
        return ["http://api.mg-rast.org", "https://api.mg-rast.org"]
    for l in open(filename).readlines():
        server_list.append(l.strip())
    return server_list

APIS = read_api_list("API.server.list")

@pytest.mark.parametrize("API_URL", APIS)
def test_project_utf8(API_URL):
    URL = API_URL + '/project/mgp128?verbosity=full'
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")   # fails if Latin-1
    assert "ERROR" not in b

@pytest.mark.parametrize("API_URL", APIS)
def test_project_noerror(API_URL):
    URL = API_URL + '/project/mgp128?verbosity=full'
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_project_validjson(API_URL):
    URL = API_URL + '/project/mgp128?verbosity=full'
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")   # fails if Latin-1
    assert "ERROR" not in b
    c = json.loads(b)  # fails if JSON corrupt
    assert "project/mgp128" in c["url"]

@pytest.mark.parametrize("API_URL", APIS)
def test_metagenome_noerror(API_URL):
    URL = API_URL + "/metagenome/mgm4447943.3?verbosity=metadata"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
    b = a.decode("utf-8")   # fails if Latin-1
    c = json.loads(b)  # fails if JSON corrupt
    assert "metagenome/mgm" in c["url"]

@pytest.mark.parametrize("API_URL", APIS)
def test_metagenome_utf8(API_URL):
    URL = API_URL + "/metagenome/mgm4447943.3?verbosity=metadata"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")   # fails if Latin-1
    assert "ERROR" not in b

@pytest.mark.parametrize("API_URL", APIS)
def test_metagenome_validjson(API_URL):
    URL = API_URL + "/metagenome/mgm4447943.3?verbosity=metadata"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")   # fails if Latin-1
    c = json.loads(b)
    assert len(c["name"]) > 4

@pytest.mark.parametrize("API_URL", APIS)
def test_metadata_export_utf8(API_URL):
    URL = API_URL + "/metadata/export/mgp128"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")   # fails if Latin-1
    assert "mgp128" in b

@pytest.mark.parametrize("API_URL", APIS)
def test_download_partial(API_URL):
    URL = API_URL + "/download/mgm4447943.3?file=350.1"
    a = check_output('''curl -sS '{}' | head -n 100 '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"GF8803K01A00MJ" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_annotation_similarity_GET(API_URL):
    URL = API_URL + "/annotation/similarity/mgm4447943.3?identity=80&type=function&source=KO"
    a = check_output('''curl -sS '{}' | head -n 10 '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"\t" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_annotation_similarity_POST(API_URL):
    a = check_output('''curl -sS -d '{"md5s":["000a8d74068603c9e8674bff9970f367","0001c08aa276d154b7696f9758839786"]}' ''' + API_URL + '''/annotation/similarity/mgm4447943.3 ''', shell=True)
    assert b"ERROR" not in a
    assert b"\t" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_annotation_sequence_GET(API_URL):
    URL = API_URL + "/annotation/sequence/mgm4447943.3?evalue=10&type=organism&source=SwissProt"
    a = check_output('''curl -sS '{}' | head -n 10 '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"\t" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_blast_result(API_URL):
    URL = API_URL + "/compute/blast/mgm4447943.3?md5=0001c08aa276d154b7696f9758839786"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"alignment" in a

#def test_post1(API_URL):
#    CMD = '''curl -sS -X POST -d '{"source":"KO","type":"function","md5s":["000821a2e2f63df1a3873e4b280002a8","15bf1950bd9867099e72ea6516e3d602"]}' "https://api.mg-rast.org/annotation/sequence/mgm4447943.3"'''     # EMPTY RETURN DATA

@pytest.mark.parametrize("API_URL", APIS)
def test_annotation_sequence_post(API_URL):
    URL = API_URL + "/annotation/sequence/mgm4447943.3"
    CMD = '''curl -sS -X POST -d '{"source":"SwissProt","type":"organism","md5s":["000821a2e2f63df1a3873e4b280002a8","15bf1950bd9867099e72ea6516e3d602"]}' "''' + URL + '''"'''
    a = check_output(CMD, shell=True)
    assert b"ERROR" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_errs_matrix_function(API_URL):
    URL = API_URL + "/matrix/function?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=level3&source=Subsystems&identity=80"
    print(URL)
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
@pytest.mark.parametrize("API_URL", APIS)
def test_errs_profile(API_URL):
    URL = API_URL + "/profile/mgm4447943.3?source=RefSeq&format=biom"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_errs_matrix_organism(API_URL):
    URL = API_URL + "/matrix/organism?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=family&source=RefSeq&evalue=15"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
@pytest.mark.parametrize("API_URL", APIS)
def test_errs_library(API_URL):
    URL = API_URL + "/library/mgl52924?verbosity=full"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
@pytest.mark.parametrize("API_URL", APIS)
def test_errs_metadata(API_URL):
    URL = API_URL + "/metadata/ontology?name=biome&version=2017-04-15"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
@pytest.mark.parametrize("API_URL", APIS)
def test_errs_darkmatter(API_URL):
    URL = API_URL + "/darkmatter/mgm4447943.3?"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
@pytest.mark.parametrize("API_URL", APIS)
def test_errs_download_history(API_URL):
    URL = API_URL + "/download/history/mgm4447943.3"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"mgm4447943.3.299.screen.passed.fna" in a 
@pytest.mark.parametrize("API_URL", APIS)
def test_err_post_parsing_err(API_URL):
    CURLCMD = '''curl -sS -d '{"data":"000821a2e2f63df1a3873e4b280002a8","format":"fasta","sequence":0,"source":"InterPro"}' ''' + API_URL + '''/m5nr/md5'''
    a = check_output(CURLCMD, shell=True)
    assert b"ARRAY ref" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_err_post_parsing_correct(API_URL):
    CURLCMD = '''curl -sS -d '{"data":["000821a2e2f63df1a3873e4b280002a8"],"format":"fasta","sequence":0,"source":"InterPro"}' ''' + API_URL + '''/m5nr/md5'''
    a = check_output(CURLCMD, shell=True)
    assert b"ARRAY ref" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_err_post_parsing_correct2(API_URL):
    CURLCMD = '''curl -X POST -sS -d '{"data":["000821a2e2f63df1a3873e4b280002a8"],"format":"fasta","sequence":0,"source":"InterPro"}' ''' + API_URL + '''/m5nr/md5'''
    a = check_output(CURLCMD, shell=True)
    assert b"ARRAY ref" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_err_parse_md5_blast(API_URL):
    URL = API_URL + "/compute/blast/mgm4447943.3?asynchronous=0&md5=0001c2703270cc7aec519107b8215b11&rna=0"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a

@pytest.mark.parametrize("API_URL", APIS)
def test_mixs_schema(API_URL):
    URL = API_URL + "/mixs/schema"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
    assert b"PI_organization_country" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_mg_search_feces(API_URL):
    CURLCMD = '''curl -sS -F "limit=5" -F "order=created_on" -F "direction=asc" -F "feature=feces" "{}/search"'''.format(API_URL)
    a = check_output(CURLCMD, shell=True)
    b = a.decode("utf-8")
    c = json.loads(b)
    assert c["total_count"] > 800

@pytest.mark.parametrize("API_URL", APIS)
def test_mg_search_utf8_debug(API_URL):
    URL = API_URL + "/search?all=é&debug=true"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")
    assert "é" in b

@pytest.mark.parametrize("API_URL", APIS)
def test_mg_search_utf8_debug_uA722(API_URL):
    URL = API_URL + "/search?all=א&debug=true"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")
    assert "א" in b


@pytest.mark.parametrize("API_URL", APIS)
def test_mg_search_utf8(API_URL):
    URL = API_URL + "/search?all=é"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")
    assert "é" in b
    c = json.loads(b)
    assert "é" in c["url"]   # If API corrupts unicode inputs, this fails

@pytest.mark.parametrize("API_URL", APIS)
def test_mg_search_utf8_uA722(API_URL):
    URL = API_URL + "/search?all=א"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")
    assert "א" in b
    c = json.loads(b)
    assert "א" in c["url"]   # If API corrupts unicode inputs, this fails

@pytest.mark.parametrize("API_URL", APIS)
def test_matrix_distinct_hashes(API_URL):
    URL = API_URL + "/matrix/organism?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&group_level=family&source=RefSeq&evalue=15"
    a = check_output('''curl -sS '{}' '''.format(URL), shell=True)
    b = a.decode("utf-8")
    c = json.loads(b)
    URL2 = API_URL + "/matrix/organism?id=mgm4447943.3&group_level=family&source=RefSeq&evalue=15"
    a2 = check_output('''curl -sS '{}' '''.format(URL2), shell=True)
    b2 = a2.decode("utf-8")
    c2 = json.loads(b2)
    assert c["id"] != c2["id"]   # hashes must be distinct
