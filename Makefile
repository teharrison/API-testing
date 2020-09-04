
test_json:
	py.test --json=report.json tests/test_byhand.py

test:
	py.test -m "not requires_auth"  --deselect tests/test_api.py

testauth:
	py.test   --deselect tests/test_api.py

testall:
	py.test

test_api:
	./API-testing.py -p > tests/test_api.py

utf:
	py.test -k utf
