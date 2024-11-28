'''
Flask Client Application by jmhrusti

This python script serves to allow a user to push data in JSON form to the corresponding Flask API.

** Note: This application does utilize unencrypted HTTP to push data. Avoid sending sensitive data using this application, including username/passwords, keys, PII, etc.
* Note: Ensure all below libraries are installed with pip.

'''
import requests
import json

# Set URL for the Flask API. Can use IP or domain name
url = 'http://localhost:5000/add'

# Define the data to be sent to the API. Script can be modified to gather information and include that in the submission.
data = {
    'ExAttribute1': 'value1',                                                   # Can add as many attributes as desired. Ensure that they match up with the API program and database
    'ExAttribute2': 'value2',
    'ExAttribute3': 'value3'
}

# Convert the data to JSON
json_data = json.dumps(data)

# Send data vai POST request to the API
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# Print response from the server
print(response.status_code)
print(response.json())
