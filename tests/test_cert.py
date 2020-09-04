from time import sleep 

try:
    import urllib2 #python2
except:
    import urllib.request as urllib2 #python3

# Test that server certificates are ok
HEADERS = {'User-Agent':'Mozilla/5.0'}
def test_cert_shock():
    req = urllib2.Request("https://shock.mg-rast.org", headers=HEADERS)
    urllib2.urlopen(req)
    sleep(5)

def test_cert_awe():
    req = urllib2.Request("https://awe.mg-rast.org", headers=HEADERS)
    urllib2.urlopen(req)
    sleep(5)

def test_cert_mgrast():
    req = urllib2.Request("https://mg-rast.org", headers=HEADERS)
    urllib2.urlopen(req)
    sleep(5)

def test_cert_api():
    req = urllib2.Request("https://api.mg-rast.org", headers=HEADERS)
    urllib2.urlopen(req)
    sleep(5)

