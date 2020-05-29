#import necessary python libraries
from pathlib import Path
import pandas as pd
import reliability_stability as rs

test_dir = Path(__file__).parent
#import data set
data = pd.read_csv(test_dir / 'BodyFat.csv')

#define columns based on input column headers
column_one = 'HEIGHT'
column_two = 'WEIGHT'
column_three = 'BODYFAT'
column_four = 'WRIST'

assumption_test_value = float('%.3f'%(rs.assumption_test(data, column_one, column_two, column_three, column_four)))

def test_correlation_value():
    assert assumption_test_value == 0.738  
