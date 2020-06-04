# Reliability Stability Description

## Description

reliability-stability is a simple package takes a csv or other pandas compatable data file and gives the reliability and stability of three columns. The reliability and stability calculations, as well as an assumption test, are based on the 1969 paper from Heise, D. R. ['Separating Reliability and Stability in Test-Retest Correlation'](https://doi.org/10.2307/2092790).

## Continuous Integration

[![nimh-mbdu](https://circleci.com/gh/nimh-mbdu/data-reliability-stability.svg?style=shield)](https://app.circleci.com/pipelines/github/nimh-mbdu/data-reliability-stability)

Continuous Integration - "circleci passing" indicates that the project's tests all pass as expected. If you see that the build for a project is "broken" it means the software does not work as advertised! This is a clear sign that you should not be using it (until it gets fixed!) ... check the repo's issues to see if it's a known problem, if not, report it! We use CircleCI for our CI.

## Installation

pip install reliability stability:

>>> pip install reliability-stability-calc

## Citations

Heise, D. R. (1969). Separating reliability and stability in test-retest correlation. American Sociological Review, 34(1), 93–101. https://doi.org/10.2307/2092790
