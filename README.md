# Connecting Flask API with Microsoft SQL Database

## Objective

This API project aimed to allow a user to remotely push data to a database via HTTP. The primary focus was to take JSON data from the HTTP POST message, convert the data, and write it to the Microsoft SQL Database. This hands-on experience was designed to deepen understanding of APIs, SQL databases, and using the HTTP POST method in scripts. 

### Skills Learned

- Unserstanding of configuring a database to store data.
- Proficiency in writing an API and interacting with it.
- Ability to write both "client" and "server" scripts for a project.
- Enhanced knowledge of Python library use.
- Development of critical thinking and problem-solving skills in cybersecurity and coding.

### Software Used

- <a href=https://www.microsoft.com/en-us/sql-server/sql-server-downloads>Microsoft SQL Server</a>
- <a href=https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms>SQL Server Management Studio (SSMS)</a>
- <a href=https://www.python.org/downloads/>Python 3.12</a>
- <a href=https://wingware.com/downloads>Wing 101 IDE</a>
- <a href=https://flask.palletsprojects.com/en/stable/installation/#python-version>Python Flask API</a>

## API Setup

### Install Microsoft SQL Server
Use the link above to download your preferred version of the database onto your server device. Once installed, a database and table should be configured to your personal specifications. This is where the data will be stored once the API and other infrastructure is in place. It is recommended that you add a user to the database specifically for this purpose and only give them write permissions to this specific database/table. SQL Server Management Studio (SSMS) is another utility that can help with managing the database depending on the size and use. 

### Install Python
Install Python from the official website on both the server and client machines. It may also be necessary to use pip to install the additionaly libraries that do not come with Python by default. 

### Download Application From This Repository
This repository contains two files that should be downloaded: 
- [Flask_API.py](/Flask_API.py) - Server side API. Should be run on the same machine as the SQL server.
- [Flask_Client.py](/Flask_Client.py) - Client side application. Should be run on client devices to push data.

### Modify Python Files To Fit Needs
The python files contain placeholders that will need to be updated with information for your purposes. 
- The database details are exclusively in the API program. This may include your database name, table name, username, and password. Environment variables could be used to store this information. 
- Database attributes to be populated in the database should be modified. This must be done in both programs and should match what is set up in the database. It is possible to modify the client script to gather information from the client machine and include this in the HTTP POST to the SQL server.
- The URL of the server should be modified in the client script so that it can connect with the API correctly. The port can be adjusted to your personal preference.

## Security

At the end of the day this is a program that relies heavily on networking. Because of this, it is very important to be conscious of security when using this program. However, this was not designed as a security tool and is exclusively used to transmit data. Here are a few recommendations that I followed in this project myself to make it _more_ secure:
- Make a separate account on Microsoft SQL Server
  - By making a new account, you can control what permissions that Python script can have
  - This prevents the user from being able to access other tables, read data, delete data, etc.
  - This helps to ensure the security of the database and that no data is removed or viewed if not authorized
- Store the SQL Server credentials outside of the program
  - This is best practice so that the program does not contain credentials
  - Recommended to be stored as environment variables
- Do not send sensitive data over the network
  - In the current configuration, the program transmits data in the clear using unencrypted HTTP
  - Because of this, data could be intercepted and read or modified
  - DO NOT transmit any data with this program that you do not want unauthorized individuals to have access to
 
## Contact
If you have questions/comments/concerns, please reach out to the creator at jmhrustich@proton.me.
