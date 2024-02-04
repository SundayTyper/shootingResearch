""" Module defines a dataclass for anaylsis. Relies on pandas library"""
import pandas as pd

class GetDataSet:
    """create class to hold data for anaylsis. Generate data by importing from CSV"""
    def __init__(self, csv_file):
        data = pd.read_csv(csv_file)
        data = data.fillna(False)
        data = data.astype('string')
        self.data_set = data.to_numpy()
