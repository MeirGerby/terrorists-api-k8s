import pandas as pd 



class CsvFile():
    def __init__(self, file) -> None:
        self.file = pd.read_csv(file)

    def top_terorist(self):
        self.file.sort_values(by="danger_rate", ascending=False)
        top_terorist = self.file.head() 
        print(top_terorist)
        return top_terorist

