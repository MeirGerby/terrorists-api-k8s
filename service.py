import pandas as pd 
from db import DBCrud



class CsvFile():
    def __init__(self, file) -> None:
        self.file = pd.read_csv(file)

    def top_terorist(self):
        self.file.sort_values(by="danger_rate", ascending=False)
        top_terorist = self.file.head() 
        terorist = top_terorist.to_dict("series")
        DBCrud.insert_data({"terorist": str(terorist)})
        return top_terorist

