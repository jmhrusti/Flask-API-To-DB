'''
Flask Database API by jmhrusti

This python script serves to allow a user to push data in JSON form to this Flask API. The script then adds a new entry to the connected database populated with the data sent to the API. This is used in conjunction with Microsoft SQL Server

*** Note: This application does utilize unencrypted HTTP to push data. Avoid sending sensitive data using this application, including username/passwords, keys, PII, etc.
** Note: Ensure all below libraries are installed with pip.
* Note: A driver for the database may need to be installed. Find drivers at learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16


   Copyright 2024 jmhrusti

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


'''
# Import libraries 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import urllib

app = Flask(__name__)

# Import urllib.parse module for URL encoding
params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=<HOSTNAME-HERE>\\SQLEXPRESS;DATABASE=<DATABASE-HERE>;UID=<DATABASE-USERNAME-HERE>;PWD=<DATABASE-USER-PASSWORD-HERE>') # May be wise to store credentials as environment variables

# Create SQLAlchemy connection string using above encoded parameters
connection_string = f'mssql+pyodbc:///?odbc_connect={params}'

# Configure Flask application to use the specified database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

# Initialize SQLAlchemy object with the Flask application
db = SQLAlchemy(app)


# Set up the table for the user's database
class Table(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)            # Assigns unique ID number to each DB tuple. Auto incrementation is turned on as this is the primary key for the table
    ExAttribute1 = db.Column(db.String(50))                                     # Add as many attributes as needed. Ensure that they match up with the attributes contained within the database
    ExAttribute2 = db.Column(db.String(50))
    Exattribute3 = db.Column(db.String(50))

# Accept data via HTTP POST
@app.route('/add', methods=['POST'])
def add_entry():
    data = request.json
    new_entry = Table(
        ExAttribute1=data['ExAttribute1'],
        ExAttribute2=data['ExAttribute2'],
        ExAttribute3=data['ExAttribute3'],
    )
    db.session.add(new_entry)                                                   # Adds new entry to the database
    db.session.commit()
    return jsonify({"message": "Entry added successfully!", "id": new_entry.ID}), 201

# For test purposes only. By navigating to http://localhost:5000/test on the machine hosting the API, you should see the message "Test endpoint is working!" in your browser
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test endpoint is working!"})


if __name__ == '__main__':
    # Running on 0.0.0.0 means that this application is open both internally (localhost) and externally. Port is set to 5000 by default - must be changed in both this and client script if updated
    app.run(host='0.0.0.0', port=5000)
