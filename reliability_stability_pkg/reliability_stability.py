#import necessary python libraries
import pandas as pd
import sys

#function to find the correlation between two variable columns
def calc_correlation(data, column_a, column_b):
	
	# check if data is a DataFrame
	if isinstance(data, pd.DataFrame):
	
		# calculate correlation between two columns
		correlation = data.corr().loc[column_a,columna_b]
	
		# return correlation between two columns
		return correlation

#function to find the reliability of a measure over three collection points
def calc_reliability(data, column_1, column_2, column_3):
	
	#find true correlations between measured values
	r12 = calc_correlation(data, column_1, column_2)
	r23 = calc_correlation(data, column_2, column_3)
	r13 = calc_correlation(data, column_1, column_3)

	#calculate reliability between three columns
	reliability = (r12*r23)/r13)
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

def main():
	
	#import data set
	data = pd.read_csv(sys.argv[1])

	#define columns based on input column headers
	column_one = data.loc[:, sys.argv[2]]
	column_two = data.loc[:, sys.argv[3]]
	column_three = data.loc[:, sys.argv[4]]

	print(calc_reliability(data, column_one, column_two, column_three))
	print(calc_stability(data, column_one, column_two, column_three))


if __name__ == "__main__":
	main()
