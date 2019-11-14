import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Follow this tutorial to get credential JSON file.
# https://gspread.readthedocs.io/en/latest/oauth2.html
CREDENTIAL_FILENAME='gspread-...-.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIAL_FILENAME, scope)

gc = gspread.authorize(credentials)

# Open a spreadsheet by name
spreadsheet = gc.open("Where is the money Lebowski?")
worksheet = spreadsheet.sheet1

# Update a specific cell
worksheet.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = worksheet.range('A1:B7')

for cell in cell_list:
    cell.value = random.randint(0, 100)
