import pandas as pd
from IPython import embed
import sys

all_cols = ['Study', 'Dataset', 'Study type', 'Prediction task',
       'Sepsis definition', 'Sepsis definition exact',
       'Case/Control alignment', 'Inclusion Criteria available',
       'Inclusion Criteria', 'number of sepsis encounters',
       'number of non-sepsis encounters', 'prevalence (%)', 'Age',
       'Sex (% female)', 'Ethnicity (% non-caucasian)',
       'Used cohort available', 'Code for analysis', 'Code for label',
       'Library versions available', 'Code Licence available', 'Model',
       'Model explanation', 'Evaluation metrics', 'AUC', 'Hours before Onset ',
       'External Validation', 'Missing Data Handling', 'Data Types',
       'Number of variables', 'Circularity addressed', 'Comments (optional)']

used_cols = ['Study', 'Dataset', 
       'Sepsis definition', 'number of sepsis encounters',
       'prevalence (%)', 'Used cohort available',
       'Code for analysis', 'Code for label', 'Model', 
       'AUC', 'Hours before Onset ', 
       'External Validation', 
       'Data Types', 'Number of variables']

f = 'data/study_overview.csv' #'data/study_overview5.csv'
df = pd.read_csv(f, header=1)

df = df[used_cols]

# convert n_sepsis to int despite nans:
df['number of sepsis encounters'] = df['number of sepsis encounters'].astype(pd.Int32Dtype())
df['prevalence (%)'] = df['prevalence (%)'].round(1) 

df = df.sort_values(by=['Study'])
df = df.reset_index(drop=True)
df.index += 1

#Replace NaNs column-wise (as e.g. integer cols cannot be replaced with strings)
for col in df.columns:
    try:
        df[col] = df[col].fillna('--')
    except:
        continue

#to ensure full strings are used in .to_latex() -- and not truncated ones:
pd.options.display.max_colwidth = 90

df.to_latex('data/table1.tex')

