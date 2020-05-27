#import necessary python libraries
import pandas as pd
import sys

#function to find the correlation between two variable columns
def calc_correlation(column_1, column_2): 
	#calculate mean and standard deviation of two columns
	c1_mean = column_1.mean(axis=0)
	c2_mean = column_2.mean(axis=0)
	c1_std = column_1.std(axis=0)
	c2_std = column_2.std(axis=0)

	# sum over difference from mean divided by standard deviation over column one and column two
	sum_total = 0 
	for idx in range(len(column_1)):
		sum_part = ((column_1[idx] - c1_mean)*(column_2[idx] - c2_mean))/(c1_std*c2_std)
		sum_total += sum_part
	
	#calculate correlation between column one and column two
	correlation = float(((1.0/((len(column_1))-1))*sum_total))
	return correlation

#function to find the reliability of a measure over three collection points
def calc_reliability(column_1, column_2, column_3):
	
	#find true correlations between measured values
	r12 = pd.DataFrame(column_1, column_2)
	r23 = float(calc_correlation(column_2, column_3))
	r13 = float(calc_correlation(column_1, column_3))

	#calculate reliability between three columns
	reliability = float(((r12*r23)/r13))
	return reliability

#function to find the stability of a measure over three collection points
def calc_stability(column_1, column_2, column_3):
	
	#find true correlations between measured values
	r12 = float(calc_correlation(column_1, column_2))
	r23 = float(calc_correlation(column_2, column_3))
	r13 = float(calc_correlation(column_1, column_3))

	#calculate stability over each time gap
	stability_12 = float(r13/r23)
	stability_23 = float(r13/r12)
	stability_13 = float((r13**2)/(r12*r23))
	
	return(stability_12, stability_23, stability_13)

def main():
	
	#import data set
	data = pd.read_csv(sys.argv[1])

	#define columns based on input column headers
	column_one = data.loc[:, sys.argv[2]]
	column_two = data.loc[:, sys.argv[3]]
	column_three = data.loc[:, sys.argv[4]]

	print(calc_reliability(column_one,column_two,column_three))
	print(calc_stability(column_one,column_two,column_three))


if __name__ == "__main__":
	main()

