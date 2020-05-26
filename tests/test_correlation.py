#import necessary python libraries
from pathlib import Path
import pandas as pd

test_dir = Path(__file__).parent
#import data set
data = pd.read_csv(test_dir / 'BodyFat.csv')
reliability_stability_pkg = test_dir / 'reliability_stability.py'

import reliability_stability_pkg as rs

#define columns based on input column headers
column_one = data.loc[:, 'WEIGHT']
column_two = data.loc[:, 'HEIGHT']

correlation_test_value = float('%.3f'%(rs.calc_correlation(column_one, column_two)))
assert correlation_test_value == 0.308
