# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.DataFrame(pd.read_csv(path))
df['state'] = df['state'].apply(lambda x: x.lower())
df['total'] = df['Jan'] + df['Feb'] + df['Mar']

sum_row = df.append({'Jan' : df['Jan'].sum(), 'Feb' : df['Feb'].sum(), 'Mar' : df['Mar'].sum(), 'total' : df['total'].sum()}, ignore_index=True)

df_final = sum_row

df_final
# Code ends here


# --------------
import requests
import pandas as pd

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1 = pd.read_html(response.content)[0]

df1.drop(index=[0,1,2,3,4,5,6,7,8,9,10], inplace = True)
df1 = df1.rename(columns = df1.iloc[0,:]).iloc[1:,:]
df1['United States of America']  = df1['United States of America'].apply(lambda x:x.replace(' ',''))
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr', np.nan)
df_final['abbr'] = df_final['state'].map(mapping)
df_final.head(5)
# Code ends here


# --------------
# Code stars here
df_final.replace(df_final.iloc[df_final[df_final['state'] == 'mississipi'].index[0]], df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS'), inplace = True)
df_final.replace(df_final.iloc[df_final[df_final['state'] == 'tenessee'].index[0]], df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN'), inplace = True)
# Code ends here


# --------------
# Code starts here
df_sub = df_final.groupby('abbr')[['Jan', 'Feb', 'Mar', 'total']].sum()
formatted_df = df_sub.applymap(lambda x: '$' + str(x)) 
# Code ends here


# --------------
# Code starts here
sum_row = pd.DataFrame(df_final[['Jan','Feb','Mar','total']].sum())
df_sub_sum = sum_row.transpose()
df_sub_sum = df_sub_sum.applymap(lambda x: '$' + str(x))

final_table = formatted_df.append(df_sub_sum, ignore_index = True)
final_table.rename(index = {13 : "Total"}, inplace = True) # row header rename

final_table
# Code ends here


# --------------
# Code starts here
#df_sub['total'] = df_sub['total'].sum()
df_sub['total'].plot.pie(figsize=(5, 5))
# Code ends here


