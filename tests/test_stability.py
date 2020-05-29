#import necessary python libraries
from pathlib import Path
import pandas as pd
import sys
sys.path.insert(0, "data-reliability-stability/reliability_stability_pkg")
from reliability_stability_pkg import reliability_stability as rs
	
    
test_dir = Path(__file__).parent
#import data set
data = pd.read_csv(test_dir / 'BodyFat.csv')

#define columns based on input column headers
column_one = data.loc[:, 'BICEPS']
column_two = data.loc[:, 'FOREARM']
column_three = data.loc[:, 'WRIST']

(stability_12, stability_23, stability_13) = rs.calc_stability(column_one, column_two, column_three)
stability_12 = float('%.3f'%(stability_12))
stability_23 = float('%.3f'%(stability_23))
stability_13 = float('%.3f'%(stability_13))

def test_stability_values():
    assert stability_12 == 1.079
    assert stability_23 == 0.932
    assert stability_13 == 1.006
