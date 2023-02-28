import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, mean_squared_error
import unittest
import fit_regression

class TestFitRegression(unittest.TestCase):
    def test_fit_linear_regression(self):
        X = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
        })
        y = pd.Series([7, 8, 9])
        model = fit_regression.fit_linear_regression(X, y)
        self.assertIsInstance(model, fit_regression.LinearRegression)
        self.assertAlmostEqual(model.intercept_, -6.0)
        self.assertAlmostEqual(model.coef_[0], 2.5)
        self.assertAlmostEqual(model.coef_[1], 1.5)