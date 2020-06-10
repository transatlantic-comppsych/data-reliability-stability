#import necessary python libraries
import pandas as pd
import sys
import numpy as np
from matplotlib import pyplot

#function to find the correlation between two variable columns
def calc_correlation(data, column_a, column_b):

	# check if data is a DataFrame
	if isinstance(data, pd.DataFrame):
	
		# calculate correlation between two columns
		correlation = data.corr().loc[column_a, column_b]

		# return correlation between two columns
		return correlation

#function to find the reliability of a measure over three collection points
def calc_reliability(data, column_1, column_2, column_3):
	
	#find true correlations between measured values
	r12 = calc_correlation(data, column_1, column_2)
	r23 = calc_correlation(data, column_2, column_3)
	r13 = calc_correlation(data, column_1, column_3)

	#calculate reliability between three columns
	reliability = (r12*r23)/r13
	return reliability

#function to find the stability of a measure over three collection points
def calc_stability(data, column_1, column_2, column_3):
	
	#find true correlations between measured values
	r12 = calc_correlation(data, column_1, column_2)
	r23 = calc_correlation(data, column_2, column_3)
	r13 = calc_correlation(data, column_1, column_3)

	#calculate stability over each time gap
	stability_12 = r13/r23
	stability_23 = r13/r12
	stability_13 = (r13**2)/(r12*r23)
	
	return(stability_12, stability_23, stability_13)

#function to check the assumptions on the reliabililty and stability tests
def assumption_test(data, column_1, column_2, column_3, column_4):
    
    # calculate correlation for outside columns and inside columns
    r14 = calc_correlation(data,column_1,column_4)
    r23 = calc_correlation(data,column_2,column_3)
    
    # calculate correlation for leaved columns
    r13 = calc_correlation(data,column_1,column_3)
    r24 = calc_correlation(data,column_2,column_4)

    # calculate products of correlations
    product_1 = r14*r23
    product_2 = r13*r24
    
    # adjust correlation products and transform with fisher's z-transformation
    if product_1 > 0:
        adjusted_product_1 = np.arctanh(np.sqrt(np.absolute(product_1)))
    else:
        adjusted_product_1 = -(np.arctanh(np.sqrt(np.absolute(product_1))))
    
    if product_2 > 0:
        adjusted_product_2 = np.arctanh(np.sqrt(np.absolute(product_2)))
    else:
        adjusted_product_2 = -(np.arctanh(np.sqrt(np.absolute(product_2))))
    
    # return the difference in the adjusted product correlations
    return adjusted_product_1 - adjusted_product_2

# function to bootstrap the assumption test
def bootstrap_assumption_test(data,column_1,column_2,column_3,column_4,bootstrap_num,alpha):
    
    # configure bootstrap
    n_iterations = bootstrap_num
    n_size = int(len(data) * 0.50)
    
    # run bootstrap
    assumption_test_stats = list()
    for i in range(n_iterations):
        
	# prepare test sets
        test_data = data.sample(n=n_size,replace=True)
        
        # run assumption test on subset test data
        assumption_value = assumption_test(test_data,column_1,column_2,column_3,column_4)
        assumption_test_stats.append(assumption_value)
        
    # plot assumption test scores
    pyplot.hist(assumption_test_stats)
    pyplot.show()
    
    # calculate confidence intervals 
    lower_bound = ((1.0-alpha)/2.0) * 100
    lower = max(0.0, np.percentile(assumption_test_stats, lower_bound))
    upper_bound = (alpha+((1.0-alpha)/2.0)) * 100
    upper = min(1.0, np.percentile(assumption_test_stats, upper_bound))
    print(str(alpha*100) + ' confidence interval ' + str(lower) + ' and ' + str(upper))

def main():
	
	#import data set
	data = pd.read_csv(sys.argv[1])

	#define columns based on input column headers
	column_one = sys.argv[2]
	column_two = sys.argv[3]
	column_three = sys.argv[4]
	column_four = sys.argv[5]

	print(calc_reliability(data, column_one, column_two, column_three))
	print(calc_stability(data, column_one, column_two, column_three))


if __name__ == "__main__":
	main()
