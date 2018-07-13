#!/usr/bin/env python
#
# Insert a document(record) into MySQL upon completion
#

##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Log output to MySQL
#
# Inserts NZB Name into MySQL.  Options are database server, database port, 
# database username, database password, database.
#
# NOTE: This script requires Python to be installed on your system and a
# couple of python modules (pip install influxdb && pip install requests)
#
# Visit:  http://chrisbergeron.com/2018/07/12/nzbget-mysql/ for more information

##############################################################################
### OPTIONS                                                                ###

# MySQL Server (Examples: `localhost`, `db-01`, `db-01.chrisbergeron.com`) 
#Host=db-01

# MySQL Server port (default is 3306)
#Port=3306

# MySQL Username
#Username=myusername

# MySQL Password
#Password=mypassword

# MySQL Database
#Database=nzbs

# MySQL Table
#Table=mynzbs

### NZBGET POST-PROCESSING SCRIPT
##############################################################################

import os, sys
import datetime
# import requests
import pymysql.cursors
import pymysql
pymysql.install_as_MySQLdb()
from datetime import datetime

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_ERROR=94
POSTPROCESS_NONE=95

# Check if the script is called from nzbget 15.0 or later
if not 'NZBOP_NZBLOG' in os.environ:
    print('*** NZBGet post-processing script ***')
    print('This script is intended to be called from nzbget (15.0 or later).')
    sys.exit(POSTPROCESS_ERROR)

# Make sure all our options are set (Settings -> InfluxLog)
required_options = ('NZBPP_NZBNAME', 'NZBPO_HOST', 'NZBPO_PORT', 'NZBPO_USERNAME', 'NZBPO_PASSWORD', 'NZBPO_DATABASE', 'NZBPO_TABLE')
for	optname in required_options:
	if (not optname in os.environ):
		print('[ERROR] Option %s is missing in configuration file. Please check script settings' % optname[6:])
		sys.exit(POSTPROCESS_ERROR)

# Get environment variables/options from NZBGet
nzbname  = os.environ['NZBPP_NZBNAME']
DBServer = os.environ['NZBPO_HOST']
Port     = os.environ['NZBPO_PORT']
Username = os.environ['NZBPO_USERNAME']
Password = os.environ['NZBPO_PASSWORD']
Database = os.environ['NZBPO_DATABASE']
Table    = os.environ['NZBPO_TABLE']

# Replace periods with spaces in our filename log entry
nzbname=nzbname.replace('.', ' ')
timestamp=datetime.now()

# Connect to our DB
db = pymysql.connect(host=DBServer, user=Username, passwd=Password, db=Database)
cursor = db.cursor()

# Create our query
sql = "INSERT INTO " + Table + " VALUES (null, '" + nzbname + "', '" + str(timestamp) + "')"

# Debug
# print "SQL: ", sql

# Execute query
number_of_rows = cursor.execute(sql)
db.commit()

# Close DB connection
db.close()

# Log what we did in NZBGet
print "[INFO] Inserted", number_of_rows, "record(s) into MySQL:", nzbname
sys.stdout.flush()

# All OK, returning exit status 'POSTPROCESS_SUCCESS' (int <93>) to let NZBGet know
# that our script has successfully completed.
sys.exit(POSTPROCESS_SUCCESS)