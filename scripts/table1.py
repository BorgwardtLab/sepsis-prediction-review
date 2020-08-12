import pandas as pd
from IPython import embed
import sys

all_cols = ['Study', 'Dataset', 'Study type', 'Prediction task',
       'Sepsis definition', 'Case/Control alignment',
       'Inclusion Criteria available', 'Inclusion Criteria', 'n_sepsis ',
       'n_not_sepsis', 'prevalence (%)', 'Age', 'Sex (% female)',
       'Ethnicity (% non-caucasian)', 'Data of used cohort available',
       'Code for analysis', 'Code for label', 'Library versions available',
       'Code Licence available', 'Model', 'Model explanation',
       'Evaluation metrics', 'External Validation', 'Missing Data Handling',
       'Data Types', 'Number of variables', 'Circularity addressed',
       'Comments (optional)']

used_cols = ['Study', 'Dataset', 
       'Sepsis definition', 'n_sepsis ',
       'prevalence (%)', 'Data of used cohort available',
       'Code for analysis', 'Code for label', 'Model', 
       'External Validation', 
       'Data Types', 'Number of variables']

f = 'data/study_overview2.csv'
df = pd.read_csv(f, header=1)

df2 = df[used_cols]

df2.to_latex('data/table1.tex')

embed()
