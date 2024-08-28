# Vulnerability Management x Jira Ticketing
Push a filtered JSON report to Jira
- Takes a High to Critical finding and creates a Task in Jira
- Comes in both BASH 🐧  and Python 🐍
- 🚧WIP🚧 

# How to Use
1. Take your .nessus and convert to JSON and filter based on criticality (High and Critical) using the 'nessus_to_json.py'
2. Push the Jira using 'issues.py' or 'issues.sh'
3. The 'auth' files are used to list available board details
