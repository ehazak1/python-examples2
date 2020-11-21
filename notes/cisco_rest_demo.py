''' Call REST API described below to create and manipulate an IPv4 NAT pool

http://www.cisco.com/en/US/docs/routers/csr1000/software/restapi/RESTAPIintro.html#wp1057517

curl -v -X POST https://10.89.206.89/api/v1/auth/token-services \
        -H "Accept:application/json" -u "admin:admin" -d "" --insecure -3


curl -v -H "Accept:application/json" \
        -H "X-Auth-Token: [YOUR_TOKEN_HERE]=" \
        -H "content-type: application/json" \
        -X POST https://10.89.206.89/api/v1/nat-svc/pool \
        -d '{"nat-pool-id": "test4-nat-pool", "start-ip-address": "172.16.10.1", "end-ip-address": "172.16.10.63", "prefix-length": 32}' \
        --insecure -3


'''

import requests, json

output_template = "%s gave a %d with response data: %r"

# Get a token for subsequent interactions
token_request_headers = { 'Accept': 'application/json' }
t = requests.post('https://10.89.206.89/api/v1/auth/token-services', 
                  auth=('admin', 'admin'),
                  verify=False,
                  headers=token_request_headers)
token = t.json()['token-id']

# Create an IPv4 NAT pool
headers = {
              'Accept': 'application/json',
              'content-type': 'application/json',
              'X-Auth-Token': token,
}
data = {
           "nat-pool-id": "test4-nat-pool",
           "start-ip-address": "172.16.10.1",
           "end-ip-address": "172.16.10.63",
           "prefix-length": 32,
}
r = requests.post('https://10.89.206.89/api/v1/nat-svc/pool',
                  data=json.dumps(data),
                  verify=False,
                  headers=headers)
print output_template % ('POST', r.status_code, r.text)

# Get information about a specific IPv4 NAT pool
r = requests.get('https://10.89.206.89/api/v1/nat-svc/pool/test4-nat-pool',
                 verify=False,
                 headers=headers)
print output_template % ('GET', r.status_code, r.text)

# Delete a specific IPv4 NAT pool
r = requests.delete('https://10.89.206.89/api/v1/nat-svc/pool/test4-nat-pool',
                    verify=False,
                    headers=headers)
print output_template % ('DELETE', r.status_code, r.text)

