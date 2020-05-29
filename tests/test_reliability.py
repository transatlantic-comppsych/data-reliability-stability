#import necessary python libraries
from pathlib import Path
import pandas as pd
import reliability_stability as rs
	
test_dir = Path(__file__).parent
#import data set
data = pd.read_csv(test_dir / 'BodyFat.csv')

#define columns based on input column headers
column_one = 'BICEPS'
column_two = 'FOREARM'
column_three = 'WRIST'

reliability_test_value = float('%.3f'%(rs.calc_reliability(data, column_one, column_two, column_three)))

def test_reliability_value():
    assert reliability_test_value == 0.628
