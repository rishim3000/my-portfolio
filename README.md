# Master's Student 

#### Technical Skills: Python, R, SQL, STATA

## Work Experience
### Analytics Intern, Data and AI Team @ Reveleer
- Evaluated and summarized performance of NLP models, delivering technical insights to both engineering teams and business leaders
  
- Identified **high-impact ICD-10 codes and HCCs**, designing a framework to prioritize quality assurance pain points
  
- Developed and deployed **RF-DETR object detection computer vision model** to accurately detect tables used in HEDIS quality metric reporting

  ![IoU images](/Images/IoU.png)


## Education
- M.S., Data Science | University of California, San Francisco (_July 2024 - June 2026_)

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
### Tennis Match Outcome Prediction using Machine Learning Techniques

Can we leverage machine learning tools to predict who wins a tennis match, utilizing performance metrics?

I developed a predictive model in **R** using Random Forest and XGBoost models based on historical match statistics. I also optimized computational efficiency while emphasizing performance, by experimenting with model complexity.

Achieved a peak accuracy of **80%**, with similar sensitivity and specificity values.

![Tennis Data](/Tennis_Predictions/images/1st_ace_scatter.png)

## Research

- Stuber Lab - University of Washington

[Publication](https://www.biorxiv.org/content/10.1101/2021.09.02.458782v1)

We researched the transcriptional dynamics within the Medial Preoptic Area (MPOA) in pubescent mice, with the goal of clarifying the molecular underpinnings behind adolescent brain development. We determined, using scRNAseq tecnniques, that selective deletion of the Esr1 gene was found to inhibit normal progression of puberty. Further work on regulatory mechanisms will give us a better understanding of how neural plasticity is affected during puberty.

![Mouse Brain](/Images/Mouse-Fox3-NFL-small.png)

- Dravid Lab - Creighton University

We aimed to understand the unique function of the GluD1 protein in maintaining neural connectivity, which allowed for higher cognitive function. We constructed mutant GluD1 vectors, inserting mutations that affected the binding interface. We then transfected these vectors into HEK cells, producing our mutant protein samples. Binding efficacy was then analyzed using SPR. This work could lead to important advancements in drug discovery, for neurodegenerative disorders such as Alzheimer's.

![GluD1](/Images/interface.jpg)

