# Push Filtered Vulnerability Report to Jira as Issue
# Carlos Enamorado 


import requests
from requests.auth import HTTPBasicAuth
import json

# Jira API URL for creating issues
url = "https://[base_url]/rest/api/3/issue" # CHANGE THIS

# Your Jira credentials
auth = HTTPBasicAuth("[email_address", "[API_KEY]") # CHANGE THIS

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# Vulnerability scan details to be included in the Jira ticket
vuln_details = {
    "summary": "High Severity Vulnerability Detected on Server XYZ",
    "description": {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "Description of the vulnerability:"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "- CVE: CVE-2024-1234"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "- Severity: High"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "- Affected Asset: Server XYZ"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "Recommended Action: Apply patch X or mitigate with firewall rule Y."
                    }
                ]
            }
        ]
    },
    "priority": "High"
}

# Data payload for creating a Jira issue
payload = json.dumps({
  "fields": {
    "project": {
      "key": "VM"  # Replace with your Jira project key - In this case Vulnerability Management Board == 'VM'
    },
    "summary": vuln_details['summary'],
    "description": vuln_details['description'],
    "issuetype": {
      "name": "Task"  # Replace with the appropriate issue type, like "Bug," "Task," etc.
    },
    "priority": {
      "name": "High"  # Set the priority based on the scan severity
    }
  }
})

# Send the POST request to create the Jira issue
response = requests.post(url, headers=headers, auth=auth, data=payload)

# Check the response
if response.status_code == 201:
    print("Jira issue created successfully!")
    issue_key = response.json()['key']
    print(f"Issue key: {issue_key}")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)
