# Early Prediction of Sepsis in the ICU using Machine Learning: A Systematic Review.

This repository gathers data and code used for the paper: "Early Prediction of Sepsis in the ICU using Machine Learning: A Systematic Review." (link and details t.b.a) 


## Data  

Under ```/data```, various data tables can be found. For the first query, the annotated query table of the Google scholar literature search can be found under ```annotated_query1.csv``` whereas the consensus table is named ```consensus_query1.csv```.  
Additional literature searches can be found under the file names: ```query_Scopus.csv, query_WoS.csv, query_embase.csv, query_pubmed.csv```.  
 

## Code   

```scripts/kappa.py``` reads the consensus table, cleans the study inclusion ratings into binary decisions 'Yes' and 'No', and computes the kappa statistic.  

Furthermore, under ```scripts``` we exemplify code that was used to generate the latex tables.  



