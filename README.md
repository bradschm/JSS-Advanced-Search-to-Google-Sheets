# JSS-Advanced-Search-to-Google-Sheets
Take any Computer/Mobile Advanced Search in the JSS and publish it to Google Sheets
Great for sharing reports with people that don't need access to your JSS
Run it on a schedule to deliver reports on time, every time!

# Features
Take any Advanced Computer or Mobile Device Search and turn it into a Google Spreadsheet.
Any columns that are included in the Display tab will be automatically included in the sheet.
Share the Google Sheet with only those who need the information.

# Requirements:
A little bit of time on your part - It's not too bad though, just a lot of things to setup the first time.
Google Apps for Domain/Education
Access to create an account, turn on developer console for an org, and Manage API Client Access
A JAMF Software Server (Tested against version 9.8)
An account with API read permissions to Mobile Device/Computer Advanced Searches and Mobiles Devices/Computers

## How to get this all setup ##
# Create a new Google Apps User
Go to admin.google.com and sign in with an admin account
Create an OU called Developers or similar
Create a new user for the project and put them in that organization  

# Give permissions to the organization
Go to Apps
Go to Additional Services
Go to Google Developers Console
Turn on for some organizations and select the Developers organization

# Create the developer project so you can get the OAuth key
Go to the Google Developers Console: https://console.developers.google.com/
Sign in with your new Google Apps Developer account
Go to Select a Project --> Create Project
Give it a meaningful name
Read and agree to the terms and click create
Go to API and Auth, Click on APIs
Enable Google Drive API
Click on Credentials, Click Add Credentials
Click on Service Account
Select p12 as the key type
Click create
Click close
You now have a service account, click on the email address
Copy the Client ID and email address to a safe location
The p12 key should download to your computer

# Authorize the API account
Go back to admin.google.com
Click on Security
Check Enable API Access
Scroll down to Advanced settings and click Manage API client Access
Paste the Client ID from the credentials page into Client Name
Paste https://spreadsheets.google.com/feeds/ into One or More API Scopes
Click Authorize
You should now see an entry for your Client ID and Spreadsheets (Read/Write)

# Setup a Google Sheet
Sign into drive.google.com as the api user or yourself and create a new sheet.
Share that sheet with the API user if you used another account
Give the Workbook a name
Give the Sheet a name
Get the spreadsheet key (Part of the URL that is before /edit )
Looks like this: 1pasdfsBr_8a3anlLDIdiSLENlsdnOK9s7bJqhdGow

# Create advanced search
Create an advanced search as desired, find the id (found in the URL)

# Get the script
Download this project
Create a folder next to the script called data
Create a folder inside data called key
Put your .p12 key into the key folder and call it sheets.p12
Open your favorite terminal
cd into project folder
Run: sudo pip install -r requirements.txt

# Lets set the variables
Set workbook key
Set worksheet name
Set google_api_user (This is the long email address we generated in the developer console)
Set google_user (This is the developer email address - what you logged into Sheets and Developer console with)
Set jss settings, host, username, password, etc
Set the as_id (Advanced Search ID)
Set the as_type by uncommenting

# Run it!
python jss-advanced_search-to-google_sheets.py

# TIPS #
Cron it! or launchd it!
Format your spreadsheet - updates will not modify format. Hidden columns will remain hidden. Bold cells will remain bold.
Conditional Formatting can be good for dealing with unknown table lengths

# Known Limitations
Can have more than 26 columns - should be easy to accomodate, just a day two thing...
I think you will have to have a Google Apps for Domain/Education account. This will not work with a personal account that I am aware of.
Right now there are a few columns that come down whether or not they are selected. This could be handled by the script.

# Warranty
I offer no warranty for this script and am not liable if I blow up your JSS or GAFE environment :)

# Next steps:
Make it so it can loop over multiple sheets and reports so only one script is needed to handle multiple reports.
Add more than 26 columns
Ability to hide UDID, name, and id fields unless specified by the report.
Logging

# Suggestion
Are welcome!
