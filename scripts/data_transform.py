import pandas as pd 
import json
import datetime as dt 
from datetime import timedelta, datetime

class DataTransform:
    def __init__(self):
        ...

    def json_parser(self, df = None) -> json:
        try:
            if df is None:
                raise ValueError("Missing required argument 'df'")
            else:
                json_df = df.to_json()
                parsed = json.loads(json_df)
                return parsed
        except ValueError as ve:
            print(ve)
    
    def current_date(self) -> datetime.date:
        return datetime.date(datetime.today())