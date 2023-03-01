import pandas as pd
import statsmodels.api as sm

def fit_linear_regression(X, y):
    """Fit an OLS model to X and y.

    Parameters
    ----------
    X : pandas.DataFrame
        Input features for the model.
    y : pandas.Series
        Target variable for the model.

    Returns
    -------
    statsmodels.regression.linear_model.RegressionResultsWrapper
        Fitted OLS model.
    """
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    return results

  

