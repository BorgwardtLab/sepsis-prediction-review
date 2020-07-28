from sklearn.metrics import cohen_kappa_score as k
import pandas as pd
import numpy as np
from IPython import embed
import os 
import sys

def clean_rating(series):
    """ 
    takes pd series (1 column) and returns cleaned rating np array only containing 'Yes' and 'No'.
    """
    rating = []
    for i, row in enumerate(series):
        if 'Yes' in row:
            rating.append('Yes')
        elif 'No' in row:
            rating.append('No')
        else:
            raise ValueError(f'In row {i}, invalid rating found: {row}')
    return np.array(rating)


if __name__ == "__main__":

    data_path = os.path.join('data', 'annotated_query1.csv')

    df = pd.read_csv(data_path)

    #only select the inclusion decisions:
    df2 = df[['MM', 'CRJ']]

    #clean ratings (only containign Yes and No)
    r_MM = clean_rating(df['MM'])
    r_CRJ = clean_rating(df['CRJ'])
    
    #compute kappa:
    kappa = k(r_MM, r_CRJ)
    print(f'Kappa = {kappa}')

