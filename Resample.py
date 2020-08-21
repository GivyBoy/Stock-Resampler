"""This program is to be used to resample  stock data. For example, if you have daily data and want weekly data."""
import pandas as pd

class Stock_scaler:
    def __init__(self, dataframe):
        logic = {'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Adj Close': 'last', 'Volume': 'sum'}
        self.dataframe = dataframe
        self.logic = logic

    def fix_data(self):
        self.dataframe.set_index('Date', inplace=True)
        self.dataframe.index = pd.to_datetime(self.dataframe.index)

    def weekly_data(self):
        self.dataframe.set_index('Date', inplace=True)
        self.dataframe.index = pd.to_datetime(self.dataframe.index)
        return self.dataframe.resample('W').apply(self.logic)

    def monthly_data(self):
        self.dataframe.set_index('Date', inplace=True)
        self.dataframe.index = pd.to_datetime(self.dataframe.index)
        return self.dataframe.resample('M').apply(self.logic)

    def yearly_data(self):
        self.dataframe.set_index('Date', inplace=True)
        self.dataframe.index = pd.to_datetime(self.dataframe.index)
        return self.dataframe.resample('Y').apply(self.logic)
