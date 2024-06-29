import pandas as pd
import streamlit as st

import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns


apptitle = 'DSSI Toy App'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('My Academic Progress')
# st.write('Reference: https://docs.streamlit.io/en/stable/api.html#display-data')
# st.balloons()

df = pd.read_excel("C:/Users/weiji/My Drive/MTECH EBAC/Y2S1 - Big Data Analytics/Big Data Implementation/dssi-streamlit-main/dssi-streamlit-main/scores.xlsx")
df_filter = df.dropna()
df_filter['Date_combined'] = df_filter['Year'].astype('int').astype("str") + "-" + df_filter['Q'].astype("str")
fig, ax = plt.subplots(figsize=(6, 3))
subjects_choice = ['All','English','Math','Science','Chinese']
subject_selected = st.selectbox("Subject_to_choose", subjects_choice)

if subject_selected == 'All':
    subjects = ['English','Math','Science','Chinese']
else:
    subjects = [subject_selected]
for subject in subjects:
    df_filter.plot(x='Date_combined', y=subject, ax=ax, kind='line', marker='o', title=f'{subject_selected} scores over time')
    x = df_filter['Date_combined']
    y = df_filter['English']

# for i in range(len(x)):
#     plt.text(x=x[i], y=y[i], s=f'{y[i]}')

plt.show()
st.pyplot(fig)
st.dataframe(df_filter, use_container_width=True)

