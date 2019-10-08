# File called _pytest for PyCharm compatability

import pandas as pd

from eland.tests.common import TestData

from pandas.util.testing import (assert_equal, assert_frame_equal)

import ast

class TestDataFrameToCSV(TestData):

    def test_to_csv_head(self):
        ed_flights = self.ed_flights().head()
        pd_flights = self.pd_flights().head()

        ed_flights.to_csv('results/test_to_csv_head.csv')
        # Converting back from csv is messy as pd_flights is created from a json file
        pd_from_csv = pd.read_csv('results/test_to_csv_head.csv', index_col=0, converters={
            'DestLocation': lambda x: ast.literal_eval(x),
            'OriginLocation': lambda x: ast.literal_eval(x)})
        pd_from_csv.index = pd_from_csv.index.map(str)
        pd_from_csv.timestamp = pd.to_datetime(pd_from_csv.timestamp)

        assert_frame_equal(pd_flights, pd_from_csv)

    def test_to_csv_full(self):
        # Test is slow as it's for the full dataset, but it is useful as it goes over 10000 docs
        ed_flights = self.ed_flights()
        pd_flights = self.pd_flights()

        ed_flights.to_csv('results/test_to_csv_full.csv')
        # Converting back from csv is messy as pd_flights is created from a json file
        pd_from_csv = pd.read_csv('results/test_to_csv_full.csv', index_col=0, converters={
            'DestLocation': lambda x: ast.literal_eval(x),
            'OriginLocation': lambda x: ast.literal_eval(x)})
        pd_from_csv.index = pd_from_csv.index.map(str)
        pd_from_csv.timestamp = pd.to_datetime(pd_from_csv.timestamp)

        assert_frame_equal(pd_flights, pd_from_csv)


