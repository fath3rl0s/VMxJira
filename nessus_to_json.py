import xmltodict
import json

# Convert .nessus report to a JSON Format
# You can modify the fields extracted in the for loop
# You can use this to further filter the report and use in with the 'issues.py' or 'issues.sh' scripts to parse
# Carlos Enamorado


# Map severity levels to human-readable labels
severity_map = {
    "0": "None",
    "1": "Low",
    "2": "Medium",
    "3": "High",
    "4": "Critical"
}

# Load and parse the .nessus file
def parse_nessus_file(file_path):
    with open(file_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    return data_dict

# Ensure the item is always a list, even if there is only one
def ensure_list(item):
    if isinstance(item, list):
        return item
    return [item]

# Extract and filter relevant data based on severity
def filter_high_critical_vulnerabilities(data_dict):
    vulnerabilities = []

    # Ensure ReportHost is a list
    report_hosts = ensure_list(data_dict['NessusClientData_v2']['Report']['ReportHost'])

    # Loop through each ReportHost
    for report_host in report_hosts:
        report_items = ensure_list(report_host.get('ReportItem', []))

        # Loop through each ReportItem
        for report_item in report_items:
            severity = report_item['@severity']
            # Filter for High (3) and Critical (4) severities
            # You can modify to extract fields wanted by commenting out
            if severity in ["3", "4"]:
                vulnerabilities.append({
                    "host": report_host.get('@name'),
                    "severity": severity_map.get(severity, "Unknown"),
                    "port": report_item.get('@port'),
                    #"service_name": report_item.get('@svc_name'),
                    #"protocol": report_item.get('@protocol'),
                    #"plugin_id": report_item.get('@pluginID'),
                    "plugin_name": report_item.get('@pluginName'),
                    "plugin_family": report_item.get('@pluginFamily'),
                    "description": report_item.get('description', 'N/A'),
                    "solution": report_item.get('solution', 'N/A'),
                    "plugin_output": report_item.get('plugin_output', 'N/A'),
                })

    return vulnerabilities

# Save the filtered data as JSON
def save_json(data, output_path):
    with open(output_path, 'w') as json_file:
       #for index, item in enumerate(data):
        json.dump(data, json_file, indent=4)
            #if index < len(data) -1:
                #json_file.write("\n\n")
    print(f"Filtered JSON output saved to {output_path}")

if __name__ == "__main__":
    # Path to your .nessus file
    nessus_file_path = 'dvwa.nessus'
    
    # Parse the file
    nessus_data = parse_nessus_file(nessus_file_path)
    
    # Filter for high and critical vulnerabilities
    filtered_vulnerabilities = filter_high_critical_vulnerabilities(nessus_data)
    
    # Save the filtered output as JSON
    output_path = 'filtered_high_critical_vulnerabilities.json'
    save_json(filtered_vulnerabilities, output_path)
