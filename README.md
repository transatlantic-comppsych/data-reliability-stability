# Reliability Stability

## Description

reliability-stability is a simple python package, which takes a csv or other pandas compatable data file and gives the reliability and stability of three columns for test-retest reliability and stability. 

[![nimh-mbdu](https://circleci.com/gh/nimh-mbdu/data-reliability-stability.svg?style=shield)](https://app.circleci.com/pipelines/github/nimh-mbdu/data-reliability-stability)

The reliability and stability calculations, as well as an assumption test, are based on the 1969 paper from Heise, D. R. ['Separating Reliability and Stability in Test-Retest Correlation'](https://doi.org/10.2307/2092790).

## Installation

pip install reliability stability:

```
>>> pip install reliability-stability-calc
```

## Usage

reliability stability is a python package with fuctions defined to: 
1. calculate correlation between two data columns (calc_correlation)
2. calculate the test-retest reliability between three data columns (calc_reliability)
3. calculate the test-retest stability between three data columns (calc_stability)
4. perform an assumption test with a fourth column (assumption_test)
5. implement a bootstap test to test assumptions (bootstrap_assumption_test)

## Citations

Heise, D. R. (1969). Separating reliability and stability in test-retest correlation. American Sociological Review, 34(1), 93–101. https://doi.org/10.2307/2092790
