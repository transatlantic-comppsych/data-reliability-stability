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

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <span resource="[_:publisher]" rel="dct:publisher">
    <span property="dct:title">Lillian Eisner</span></span>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Reliability Stability</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="[_:publisher]">
  United States</span>.
</p>

reliability stability is a python package with fuctions defined to: 
1. calculate correlation between two data columns (calc_correlation)
2. calculate the test-retest reliability between three data columns (calc_reliability)
3. calculate the test-retest stability between three data columns (calc_stability)
4. perform an assumption test with a fourth column (assumption_test)
5. implement a bootstap test to test assumptions (bootstrap_assumption_test)

Refer to the [documentation](https://github.com/nimh-mbdu/data-reliability-stability/wiki) for more examples and narrative guides.

## Citations

Heise, D. R. (1969). Separating reliability and stability in test-retest correlation. American Sociological Review, 34(1), 93–101. https://doi.org/10.2307/2092790
