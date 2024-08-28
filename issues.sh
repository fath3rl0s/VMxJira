#!/bin/bash
# Push a filtered Vulnerability Scan to Jira using BASH 
# Update 'url', 'email', 'api_token' variables before running
# This assumes a certain JSON structure from Vuln Scan but can be modified as well



# Jira API URL for creating issues
url="https://[base_url]/rest/api/3/issue" # CHANGE THIS

# Jira credentials
email="[email_address]" # CHANGE THIS
api_token="$JIRA_API" # CHANGE THIS ENV VAR (API KEY)

# JSON payload
payload=$(cat <<EOF
{
  "fields": {
    "project": {
      "key": "VM"
    },
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
              "text": "BASH SCRIPT TESTING:"
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
    "issuetype": {
      "name": "Task"
    },
    "priority": {
      "name": "High"
    }
  }
}
EOF
)

# Ensure the JSON is compacted (no newlines or extra spaces)
compact_payload=$(echo "$payload" | jq -c .)

# Make the POST request using curl
response=$(curl -s -w "\n%{http_code}" \
  --user "$email:$api_token" \
  -X POST \
  -H "Content-Type: application/json" \
  --data "$compact_payload" \
  "$url")

# Extract response and status code
http_body=$(echo "$response" | sed '$d')
http_status=$(echo "$response" | tail -n1)

# Check the response status code
if [ "$http_status" -eq 201 ]; then
  issue_key=$(echo "$http_body" | jq -r '.key')
  echo "Jira issue created successfully! Issue key: $issue_key"
else
  echo "Failed to create issue. Status code: $http_status"
  echo "$http_body"
fi
