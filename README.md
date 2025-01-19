# Rishi Mukundan - Master's Student 

#### Technical Skills: Python, R, SQL, STATA

## Education
- M.S., Health Data Science | University of California, San Francisco (_July 2024 - June 2026_)

- B.S., Molecular Biology | University of Washington (_September 2018 - March 2022_)

## Projects
### Analysis of Multiple Sclerosis Patient Data

How can we derive meaningful conclusions from messy data using **Python**?

Multi-step workflow consisting of data preparation/validation, statistical analysis, and informative visualizations. This allowed me to assess the interactions of age and education on patient walking speed. I was also able to pattern insurance/cost distribution across multiple demographic variables.

![MS Data](/Images/pairplot.png)

### DNA Sequencing and Cutsite Analysis

Constructed **Python** script that takes a FASTA file containing DNA sequence as input and outputs various operations on it (complement, reverse, reverse complement)

I also wanted to understand how to analyze the effect of restriction enzymes on DNA. So, I created a script that takes any enzyme cutsite pattern (ex. GGATCC for BamHI) and outputs the total number of cut sites, cut site pairs, and locations of pairs within a DNA sequence. This type of project has important implications in genetic engineering and enzyme function research.

#### Example usage
`````
python find_distant_cutsites.py data/random_sequence.fasta "G|GATCC"
`````

Output:
`````
Analyzing cut site: GGATCC
Total cut sites found: 976
Cut site pairs 80-120 kbp apart: 1423
First 5 pairs:
1. 15231 - 101589
2. 15231 - 118956
3. 28764 - 109102
4. 28764 - 126471
5. 42198 - 122609
`````

## Research
