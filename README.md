# JSS-Advanced-Search-to-Google-Sheets
Take any Computer/Mobile Advanced Search in the JSS and publish it to Google Sheets<br>
Great for sharing reports with people that don't need access to your JSS<br>
Run it on a schedule to deliver reports on time, every time!<br>

## Features
<ul><li>Take any Advanced Computer or Mobile Device Search and turn it into a Google Spreadsheet.</li>
<li>Any columns that are included in the Display tab will be automatically included in the sheet.</li>
<li>Share the Google Sheet with only those who need the information.</li></ul>

## Requirements:
A little bit of time on your part - It's not too bad though, just a lot of things to setup the first time.<br>
Google Apps for Domain/Education<br>
Access to create an account, turn on developer console for an org, and Manage API Client Access<br>
A JAMF Software Server (Tested against version 9.8)<br>
An account with API read permissions to Mobile Device/Computer Advanced Searches and Mobiles Devices/Computers<br>

# How to get this all setup
## Create a new Google Apps User<br>
Go to admin.google.com and sign in with an admin account<br>
Create an OU called Developers or similar<br>
Create a new user for the project and put them in that organization  <br>

## Give permissions to the organization
Go to Apps<br>
Go to Additional Services<br>
Go to Google Developers Console<br>
Turn on for some organizations and select the Developers organization<br>

## Create the developer project so you can get the OAuth key
Go to the Google Developers Console: https://console.developers.google.com/<br>
Sign in with your new Google Apps Developer account<br>
Go to Select a Project --> Create Project<br>
Give it a meaningful name<br>
Read and agree to the terms and click create<br>
Go to API and Auth, Click on APIs<br>
Enable Google Drive API<br>
Click on Credentials, Click Add Credentials<br>
Click on Service Account<br>
Select p12 as the key type<br>
Click create<br>
Click close<br>
You now have a service account, click on the email address<br>
Copy the Client ID and email address to a safe location<br>
The p12 key should download to your computer<br>

## Authorize the API account
Go back to admin.google.com<br>
Click on Security<br>
Check Enable API Access<br>
Scroll down to Advanced settings and click Manage API client Access<br>
Paste the Client ID from the credentials page into Client Name<br>
Paste https://spreadsheets.google.com/feeds/ into One or More API Scopes<br>
Click Authorize<br>
You should now see an entry for your Client ID and Spreadsheets (Read/Write)<br>

## Setup a Google Sheet
Sign into drive.google.com as the api user or yourself and create a new sheet.<br>
Share that sheet with the API user if you used another account<br>
Give the Workbook a name<br>
Give the Sheet a name<br>
Get the spreadsheet key (Part of the URL that is before /edit )<br>
Looks like this: 1pasdfsBr_8a3anlLDIdiSLENlsdnOK9s7bJqhdGow<br>

## Create advanced search
Create an advanced search as desired, find the id (found in the URL)<br>

## Get the script
Download this project<br>
Create a folder next to the script called data<br>
Create a folder inside data called key<br>
Put your .p12 key into the key folder and call it sheets.p12<br>
Open your favorite terminal<br>
cd into project folder
Run: ```sudo pip install -r requirements.txt```

## Lets set the variables
Set workbook key<br>
Set worksheet name<br>
Set google_api_user (This is the long email address we generated in the developer console)<br>
Set google_user (This is the developer email address - what you logged into Sheets and Developer console with)<br>
Set jss settings, host, username, password, etc<br>
Set the as_id (Advanced Search ID)<br>
Set the as_type by uncommenting<br>

## Run it!
```python jss-advanced_search-to-google_sheets.py```

## TIPS 
Cron it! or launchd it!<br>
Format your spreadsheet - updates will not modify format. Hidden columns will remain hidden. Bold cells will remain bold.<br>
Conditional Formatting can be good for dealing with unknown table lengths<br>

## Known Limitations
Can have more than 26 columns - should be easy to accomodate, just a day two thing...<br>
I think you will have to have a Google Apps for Domain/Education account. This will not work with a personal account that I am aware of.<br>
Right now there are a few columns that come down whether or not they are selected. This could be handled by the script.<br>

## Warranty
I offer no warranty for this script and am not liable if I blow up your JSS or GAFE environment :)<br>

## Next steps:
Make it so it can loop over multiple sheets and reports so only one script is needed to handle multiple reports.<br>
Add more than 26 columns<br>
Ability to hide UDID, name, and id fields unless specified by the report.<br>
Logging<br>

## Suggestion
Are welcome!<br>
