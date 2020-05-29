#import necessary python libraries
from pathlib import Path
import pandas as pd
import reliability_stability as rs

test_dir = Path(__file__).parent
#import data set
data = pd.read_csv(test_dir / 'BodyFat.csv')

#define columns based on input column headers
column_one = 'WEIGHT'
column_two = 'HEIGHT'

correlation_test_value = float('%.3f'%(rs.calc_correlation(data, column_one, column_two)))

def test_correlation_value():
    assert correlation_test_value == 0.308    
    
