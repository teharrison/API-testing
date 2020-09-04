import os
from subprocess import check_output
import pytest
import json

from test_byhand import read_api_list

#  This test was noted failing for some backend API servers but not others
#  Rotate through list of backend server hosts:ports in API.server.list
#  with paramterized tests

APIS = read_api_list("API.server.list")
print(APIS)

@pytest.mark.parametrize("API_URL", APIS)
def test_blast_result_http(API_URL):
    URL = API_URL + "/compute/blast/mgm4447943.3?md5=0001c08aa276d154b7696f9758839786"
    a = check_output('''curl  '{}' '''.format(URL), shell=True)
    assert b"ERROR" not in a
    b = a.decode("utf-8")
    c = json.loads(b) 
    assert "BLASTX" in c["data"]["alignment"] 
