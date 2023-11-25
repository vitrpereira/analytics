import gspread
import pandas as pd

class SpreadsheetConnector:

    def ss_connect(self, spreadsheet_url):
        gc = gspread.service_account(filename="creds.json")

        sht2 = gc.open_by_url(f'{spreadsheet_url}')

        df = pd.DataFrame(sht2.sheet1.get_all_values())
        
        return df