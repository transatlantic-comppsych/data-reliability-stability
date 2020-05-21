#import necessary python libraries
import pandas as pd
import reliability_stability_pkg as rs
	
#import data set
data = pd.read_csv('BodyFat.csv')

#define columns based on input column headers
column_one = data.loc[:, 'BICEPS']
column_two = data.loc[:, 'FOREARM']
column_three = data.loc[:, 'WRIST']

(stability_12, stability_23, stability_13) = rs.calc_stability(column_one, column_two, column_three)
stability_12 = float('%.3f'%(stability_12))
stability_23 = float('%.3f'%(stability_23))
stability_13 = float('%.3f'%(stability_13))

assert stability_12 == 1.079
assert stability_23 == 0.932
assert stability_13 == 1.006
