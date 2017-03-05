import unittest
from loan_predictor import run_tester
import pandas as pd
datas=pd.read_csv("test_data.csv")


class ML(unittest.TestCase):

    def test_accuracy_score2(self):
        assert run_tester() == 1


unittest.main()
