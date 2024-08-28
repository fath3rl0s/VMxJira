# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# Grabs Jira Board Details
# Carlos Enamorado
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://[base_url]/rest/agile/1.0/board" # CHANGE THIS

auth = HTTPBasicAuth("[email_address]", "[API_KEY]") # CHANGE THIS: EMAIL AND API KEY

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# Load JSON Data
data = json.loads(response.text)

#Filter the JSON to find the object with the specific ID
target_id = 206 # CHANGE TO FIT YOUR ENV

result = next((item for item in data ['values'] if item['id'] == target_id), None)

if result:
    print(json.dumps(result, sort_keys=True, indent=4, separators=(",", ": ")))
else:
    print(f"No object found with id {target_id}")
