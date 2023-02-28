import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

def fit_linear_regression(X, y):
    """Fit a linear regression model to X and y.

    Parameters
    ----------
    X : pandas.DataFrame
        Input features for the model.
    y : pandas.Series
        Target variable for the model.

    Returns
    -------
    sklearn.linear_model.LinearRegression
        Fitted linear regression model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model