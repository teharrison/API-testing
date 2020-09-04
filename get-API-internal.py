#!/usr/bin/env python

from __future__ import print_function
import re
import sys
import json
import random
from subprocess import check_output

if len(sys.argv) == 1:
    sys.stderr.write("missing required etcd host name\n")
    sys.exit(1)

etcdhost = sys.argv[1]

try:
    info = json.loads(check_output(["curl", "-s", "http://%s:2379/v2/keys/services/api-server/api/"%(etcdhost)]))
except:
    sys.stderr.write("unable to connect to etcd cluster using host=%s\n"%(etcdhost))
    sys.exit(1)

for entry in info["node"]["nodes"]:
    value = json.loads(entry["value"])
    ip = value["COREOS_PUBLIC_IPV4"]
    port = value["http"]
    print("http://%s:%d"%(ip, port))

sys.exit(0)

