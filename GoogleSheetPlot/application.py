from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd


class access_sheet:
    def __init__(self,
                 SI=None,
                 RN=None):
        """
        Access the google sheet
        Args:
            SI: google Spreadsheet-ID, generated ffrom link of the of the google
                spreadsheet saved in google drive.
            RN: Range Name of the google spreadsheet you want to use. Ex-A1:c100

        Returns:
            Parametres required to initialize the google sheet access process.
        """
        if SI==None:
            raise Exception("SAMPLE_SPREADSHEET_ID is missing.")
        if RN==None:
            raise Exception("SAMPLE_RANGE_NAME is missing.")
        self.SPREADSHEET_ID = SI
        self.RANGE_NAME = RN
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']# If modifying these scopes, delete the file token.pickle.
        self.values_input = None
        self.service = None
        self.creds = None

    def __call__(self):
        """
        Access the google sheet and return a dataframe.
        Returns:
            Accessed google sheet in dataframe format.
        """
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES) # here enter the name of your downloaded JSON file
                self.creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
        self.sheet = self.service.spreadsheets()
        result_input = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
        self.values_input = result_input.get('values', [])
        if not self.values_input and not values_expansion:
            print('No data found.')
        return self.values_input
