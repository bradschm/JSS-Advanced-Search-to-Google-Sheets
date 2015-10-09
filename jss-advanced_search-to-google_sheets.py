# JSS Advanced Search to Google Sheet
# Authored by Brad Schmidt on 10/8/2015
# Requires a Google developer account, project, and key. See DOCS for more information on how to obtain
# the necessary OAuth information for Google Sheets API to function
# The OAuth key will be stored in ./data/key/sheets.p12
# The credentials will be stored in ./data/sheets.dat

# Please fill out the variables below

# Variables
workbook_key = ""
worksheet_name = ""

# Oauth
google_api_user = ''
google_user = ''

# JSS Authentication
jss_host = "" # Include http:// or https:// leave off port number Example: https://your.jss.com
jss_port = "8443" # Port number
jss_path = "" # Context -- if you need it: Enter it with a forward slash. Example: If your JSS is https://your.jss.com:8443/dev you would enter /dev
jss_username = "" # Setup a user with API rights to read Advanced Computer and Mobile Reports as well as Computers and Mobile Devices
jss_password = "" # Password

# Advanced search ID and Type
as_id = ""

# Advanced search ID Type -- Uncomment one
#as_type = "Computer"
#as_type = "Mobile"

################################################################
######### You should not have to modify below this line ########
################################################################

################################################################
##################---Importing Libraries---#####################
################################################################
import sys
import httplib2
import string
import googleapiclient
import oauth2client
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.client import OAuth2WebServerFlow

# OS path to pickup files,etc
import os.path
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
# Handles json parsing
import json

# Allows us to work with the Google Sheet
import gspread

# requests makes the JSS connection
import requests

# Mobile or Computer Search - set values
def as_type_f(as_type):
    if as_type == "Computer":
        return "advancedcomputersearches","advanced_computer_search","computers"
    if as_type == "Mobile":
        return "advancedmobiledevicesearches","advanced_mobile_device_search","mobile_devices"
    else:
        print 'Failed to set as_type properly.\rPlease uncomment as_type = "Computer" or as_type = "Mobile"'

# Get the report data
def getReportData(as_path,as_key,as_rows):
    # Make the request of the JSS API
    r = requests.get(jss_host + ':' + jss_port + jss_path + '/JSSResource/' + as_path + '/id/' + as_id, headers={'Accept': 'application/json'}, auth=(jss_username,jss_password))
    #  logging.info("Response: %s" %r.text)

    # Get the device data we need
    report_data = r.json()[as_key]

    # Get the header values
    for c in report_data[as_rows]:
        columns = c.keys()

    # Return the data and the headings
    return report_data[as_rows],columns

# This function authenticates the Sheets session
def oauthSheets():
	####--logging.info("Authenticating using OAuth for Google Sheets")
	f = file('%s/%s' % (SITE_ROOT,'data/key/sheets.p12'), 'rb')
	key = f.read()
	f.close()
	http = httplib2.Http()
	storage = Storage(SITE_ROOT + '/data/sheets.dat')
	credentials = storage.get()
	if credentials is None or credentials.invalid:
		credentials = SignedJwtAssertionCredentials(google_api_user, key, scope='https://spreadsheets.google.com/feeds/',sub=google_user)
		storage.put(credentials)
	else:
		credentials.refresh(http)
	http = httplib2.Http()
	http = credentials.authorize(http)
	gc = gspread.authorize(credentials)
	return gc

def publish(report,columns):
	####--logging.info("Checking to see if the user has filled out the UA")
	# Oauth Sheet

	gc = oauthSheets()
    # Select the sheet
	wks = gc.open_by_key(workbook_key)
	worksheet = wks.worksheet(worksheet_name)

    # Clear out existing data from the sheet
    # Get length of spreadsheet
	rows = worksheet.col_values(1)
	number_of_rows = len(rows)

    # Get the width of the spreadsheet
	cols = worksheet.row_values(1)
	number_of_columns = len(cols)

    # If the sheet is blank skip over the clear portion. A range error will occur if it is blank
	if number_of_columns != 0 and number_of_rows != 0:

        # Now that we have the coordinates let's set the range
		cell_list = worksheet.range('A1:%s%s' % (string.uppercase[number_of_columns],number_of_rows))

        # Set each cell to ""
		for cell in cell_list:
			cell.value = ""

        # Update the cells all at once
		worksheet.update_cells(cell_list)

    # Setup the Header row
    # Get the number of columns provided by the Advanced Search
	number_of_columns = len(columns) - 1

    # Set the cell range
	cell_list = worksheet.range('A1:%s1' % string.uppercase[number_of_columns])

    # Create a list of column header values
	header_data = []
	for header in columns:
	 	header_data.append(header)

    # Iterates through each value in the list and each cell
	for heading, cell in zip(header_data,cell_list):
	 	cell.value = heading

    # Update the sheet with column headers
	worksheet.update_cells(cell_list)

    # Prepare the data from the Advanced Search
	search_data = []
	for line in report:
		for header in columns:
			cell = line.get(header)
 			search_data.append(cell)

    # Let's see how many rows are in the report
	rows = len(report)

    # Select a range
	cell_list = worksheet.range('A2:%s%s' % (string.uppercase[number_of_columns],rows + 1))

    # Set the cell value while iterting through values and cells
	for value, cell in zip(search_data,cell_list):
		cell.value = value

    # Update the spreadsheet with the report data
	worksheet.update_cells(cell_list)

# Is it Mobile or Computer, return approprtiate values for parsing the report
# Let's make sure the value was uncommented
try:
    as_type
    as_path,as_key,as_rows = as_type_f(as_type)
except NameError:
    print 'Failed to set as_type properly.\rPlease uncomment as_type = "Computer" or as_type = "Mobile"'
    sys.exit(1)

# Get the data from the advanced search
report,columns = getReportData(as_path,as_key,as_rows)

# Publish to Google Sheet
publish(report,columns)
