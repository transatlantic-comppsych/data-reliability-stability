#import necessary python libraries
import pandas as pd
import reliability_stability_pkg as rs
	
#import data set
data = pd.read_csv('BodyFat.csv')

#define columns based on input column headers
column_one = data.loc[:, 'WEIGHT']
column_two = data.loc[:, 'HEIGHT']

correlation_test_value = float('%.3f'%(rs.calc_correlation(column_one, column_two)))
assert correlation_test_value == 0.308
