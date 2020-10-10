# GoogleSheetPlot
This library helps a user to select a google sheet from their Google drive and plots a chart with the values on the sheet. The user only needs to select the column for the x-axis and the y-axis.
<br>
## Install
'''
pip install GoogleSheetPlot
'''
## How to initialize
Add the desired google sheet to the google drive then, get the last section the google drive link as Spreadsheet-ID.
<br>
Example - if google drive link is "https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit?usp=sharing", then google SPREADSHEET_ID = "1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc".
<br>
Then the user needs to assign the range of the google sheet.
<br>
Example - RANGE_NAME = 'A1:C80'

'''
from GoogleSheetPlot import GoogleSheetPlot
SAMPLE_SPREADSHEET_ID = '1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc'
SAMPLE_RANGE_NAME = 'A1:C80'
gsp = GoogleSheetPlot()
df = gsp.getDataFrame(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
'''
here "df" represents the accessed google sheet in dataframe format.
<br>
Please download the "credentials.json" file in your working repository by clicking the "Enable Google Sheets API" button
by visiting the page [Turn on the Google Sheets API](https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the).
## Plot the graph
Just give the valid column names(X and Y axis)with the type of plot you want to get.
Your plot gets saved with the format "col1_col2_category.png".
'''
gsp.getPlot("average_sales", "offer_price","line")
'''
## Example
Please go through the Example.ipynb file in the Example folder.
