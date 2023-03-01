import numpy as np
import pandas as pd

from sklearn.datasets import make_classification, make_regression
import unittest
from fit_regression.fit_regression import fit_linear_regression,fit_logistic_regression

class TestFitRegression(unittest.TestCase):
    def test_fit_linear_regression(self):
        np.random.seed(123)
        X, y, = make_regression(n_samples=100, n_features=3, noise=0.1, random_state=123)
        X = pd.DataFrame(X, columns=['A', 'B', 'C'])
        y = pd.Series(y + X['A'] * 2 + X['B'] * 3 + X['C'] * 4 + 5, name='target')
        model = fit_linear_regression(X, y)
        self.assertAlmostEqual(model.params[0],4.9833992456725476)
        self.assertAlmostEqual(model.params[1], 79.75818359288121, places=1)
        self.assertAlmostEqual(model.params[2], 77.65486075313702, places=1)
        self.assertAlmostEqual(model.params[3], 27.265924552530194, places=1)
        
if __name__ == '__main__':
    unittest.main()




    
    
