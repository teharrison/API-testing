from subprocess import check_output
import json
import pytest
from test_byhand import read_api_list

# subset of ~20 example invokations from the API-explorer page  (all GET)
# http://www.mg-rast.org/mgmain.html?mgpage=api
# mangled by hand into

APIS = read_api_list("API.server.list")

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_annotation_similarity(API_URL):
 # This one gives a similarity table -- need to truncate!
    CALL = '''curl '{}/annotation/similarity/mgm4447943.3?id=mgm4447943.3&identity=80&no_cutoffs=0&source=KO&type=function' | head  '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"mgm4447943.3" in a

#def test_apix_compute_alpha2():
#    CALL = '''curl '{}/compute/alphadiversity/mgm4447943.3?id=mgm4447943.3&asynchronous=0&level=order' '''
#    a = check_output(CALL, shell=True)
#    assert not b"ERROR" in a
@pytest.mark.parametrize("API_URL", APIS)
def test_apix3(API_URL):
    CALL = '''curl '{}/compute/blast/mgm4447943.3?id=mgm4447943.3&asynchronous=0&md5=0001c08aa276d154b7696f9758839786&rna=0' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "QAEGDTEK-----DRGRMIRVA" in aa["data"]["alignment"]

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_darkmatter_id(API_URL):
    CALL = '''curl '{}/darkmatter/mgm4447943.3?id=mgm4447943.3' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "download/mgm4447943.3?file=750.1" in aa["url"]

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_download_id_350(API_URL):
    CALL = '''curl '{}/download/mgm4447943.3?id=mgm4447943.3&file=350.1&link=0' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b">GF8803K01A0000" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_download_history(API_URL):
    CALL = '''curl '{}/download/history/mgm4447943.3?id=mgm4447943.3&delete=0&force=0' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "data" in aa.keys()

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_download(API_URL):
    CALL = '''curl '{}/download/mgm4447943.3?id=mgm4447943.3&stage=650' | head '''.format(API_URL)
    CALL = '''curl '{}/download/mgm4447943.3?id=mgm4447943.3&file=650.1' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"GF8803K01A004I" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_accession(API_URL):
    CALL = '''curl '{}/m5nr/accession/YP_003268079.1?id=YP_003268079.1' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"sulfatase" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["total_count"] > 0

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_md5(API_URL):
    CALL = '''curl '{}/m5nr/md5/000821a2e2f63df1a3873e4b280002a8?id=000821a2e2f63df1a3873e4b280002a8&format=fasta&sequence=0&source=RefSeq' | head '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"YP_001476369.1" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_function(API_URL):
    CALL = '''curl '{}/m5nr/function/sulfatase?text=sulfatase&exact=0&id_only=0&inverse=0&source=GenBank' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["total_count"] > 100

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_organism(API_URL):
    CALL = '''curl '{}/m5nr/organism/akkermansia?text=akkermansia&exact=0&inverse=0&source=KEGG&tax_level=strain' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"Akkermansia muciniphila" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix12(API_URL):
    CALL = '''curl '{}/m5nr/sequence/MSTAITRQIVLDTETTGMNQIGAHYEGHKIIEIGAVEVVNRRLTGNNFHVYLKPDRLVDPEAFGVHGIADEFLLDKPTFAEVADEFMDYIRGAELVIHNAAFDIGFMDYEFSLLKRDIPKTNTFCKVTDSLAVARKMFPGKRNSLDALCARYEIDNSKRTLHGALLDAQILAEVYLAMTGGQTSMAFAMEGETQQQQGEATIQRIVRQASKLRVVFATDEEIAAHEARLDLVQKKGGSCLWRA?text=MSTAITRQIVLDTETTGMNQIGAHYEGHKIIEIGAVEVVNRRLTGNNFHVYLKPDRLVDPEAFGVHGIADEFLLDKPTFAEVADEFMDYIRGAELVIHNAAFDIGFMDYEFSLLKRDIPKTNTFCKVTDSLAVARKMFPGKRNSLDALCARYEIDNSKRTLHGALLDAQILAEVYLAMTGGQTSMAFAMEGETQQQQGEATIQRIVRQASKLRVVFATDEEIAAHEARLDLVQKKGGSCLWRA&source=TrEMBL' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"DNA polymerase III epsilon subunit" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_function_id_POST(API_URL):
    CALL = "curl -s " + API_URL + '''/m5nr/function_id -d '{"compress":0,"data":["2442,5432"]}' '''
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "data" in aa.keys()
    assert b"1,4-beta-D-glucan-cellobiohydrolyase" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_organism_POST(API_URL):
    CALL = "curl -s " + API_URL + '''/m5nr/organism -d '{"data":["akkermansia","yersinia"],"exact":0,"inverse":0,"order":"accession","source":"KEGG","tax_level":"strain"}' '''
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["data"][0]["source"] == "KEGG"

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_m5nr_sequence_POST(API_URL):
    CALL = "curl -s " + API_URL +  '''/m5nr/sequence -d '{"data": ["MAGENHQWQGSIL","MAGENHQWQGSIL"]}' '''
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    assert b"nuclear hormone receptor" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_matrix_organism(API_URL):
    CALL = '''curl '{}/matrix/organism?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&evalue=15&filter_level=function&filter_source=Subsystems&group_level=family&hide_metadata=0&hit_type=all&result_type=abundance&source=RefSeq' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_matrix_function(API_URL):
    CALL = '''curl '{}/matrix/function?id=mgm4447943.3&id=mgm4447192.3&id=mgm4447102.3&filter_level=strain&filter_source=RefSeq&group_level=level3&hide_metadata=0&identity=80&result_type=abundance&source=Subsystems' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "status" in aa.keys()

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_export_project(API_URL):
    CALL = '''curl '{}/metadata/export/mgp128?id=mgp128' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert "The oral metagenome in health and disease" in aa["name"]

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_metagenome_search(API_URL):
    CALL = '''curl '{}/metagenome?direction=asc&limit=20&match=all&order=name&status=both&verbosity=minimal' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["total_count"] > 1000

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_metagenome(API_URL):
    CALL = '''curl '{}/metagenome/mgm4447943.3?id=mgm4447943.3&nocache=0&verbosity=metadata' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["md5_checksum"] == "c031de380d7961aa820c108443205220"

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_project_search(API_URL):
    CALL = '''curl '{}/project?limit=20&order=name&verbosity=minimal' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert aa["total_count"] > 1000

@pytest.mark.parametrize("API_URL", APIS)
def test_apix_project_mgp128(API_URL):
    CALL = '''curl '{}/project/mgp128?id=mgp128&verbosity=full' '''.format(API_URL)
    a = check_output(CALL, shell=True)
    assert not b"ERROR" in a
    aa = json.loads(a.decode("utf-8"))
    assert len(aa["metagenomes"]) > 4
