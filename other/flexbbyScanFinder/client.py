import http.client
import json

url_1 = "https://demodf.flexbby.com/multistorage/reports/stored/documents/2017/05/29/144644_karuqfybnewrlbskrpatpqcudjcqnmmxmhvgouhd.pdf"
url_2 = "https://demodf.flexbby.com/multistorage/reports/stored/documents/2017/05/29/144650_wmthqgswkmiypywnbwndsmcxdnvrbgsxspijxdjk.PDF"

data = {
	'original': url_1,
	'document': url_2,
}
#
conn = http.client.HTTPConnection("localhost", 8000, timeout=60)
conn.request("POST", 'localhost', json.dumps(data))
print('\033[92m'+'Data was sent successfully....'+'\033[0m')
info = conn.getresponse()
data = info.read()
print('Reason : ' + info.reason)
print('Status : ' + info.stasus)
print('Data : ')
print(data)

