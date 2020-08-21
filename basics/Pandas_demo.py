import numpy as np
import pandas as pd
import os
from pandas import Series, DataFrame

# file I/O
path = "/Users/yujiehao/works/data/pandas/"
file_name = 'ad_feature.csv'

df = pd.read_csv(path + file_name, sep=',', header=0)  # read data

df[:100].to_csv(path + 'ad_feature_output.csv', index=False)
df[:100].to_html(path + 'ad_feature_output.html', index=False)

writer = pd.ExcelWriter(path + 'ad_feature_output.xlsx')
df[:100].to_excel(writer, 'Sheet1', index=False)
df[100:200].to_excel(writer, 'Sheet2', index=False)
writer.save()

# Essential Basic Functionality
print('\ndf.shape: ' + str(df.shape))  # rows, columns
print('\ndf.columns: ' + str(df.columns))
print('\ndf.head(10): ' + str(df.head(10)))  # top 10 rows
print('\ndf.tail(10): ' + str(df.tail(10)))  # last 10 rows
print('\ndf[\'price\'].describe(): ' + str(df['price'].describe()))
print('\ndf[\'cate_id\'].describe(): ' + str(df['cate_id'].describe()))

print("\nIteration")
for row in df[:10].itertuples():
    print(row.cate_id, row.price)

print("\nsort_values()")
print(str(df[:10].sort_values(by='price')))

print("\nsort_values(), multi-column")  # sort by 1st col first, if same value, sort by 2nd col...
print(str(df[:10].sort_values(by=['price', 'brand'], ascending=False)))

print("\nfiltering")
print(str(df[(df['price'] > 1000) & (df['price'] <= 1005)]))

# Groupby
print("\ngroup by")
df = pd.read_csv(path + file_name, sep=',', header=0, nrows=1000)
# cate_group = df.groupby(['cate_id', 'customer'])
cate_group = df.groupby(['cate_id'])
print('\ntype(cate_group)' + str(type(cate_group)))
print('\ncate_group.size():\n' + str(cate_group.size()))  # size is executed inside the same group
print('\ncate_group[].mean().head():\n' + str(cate_group[['price', 'brand']].mean().head()))
print('\nreset_index:\n' + str(df.groupby('cate_id')['brand'].mean().reset_index(drop=False).head))

# Merge, Concatenate
df = pd.read_csv(path + file_name, sep=',', header=0)
df1 = df[['adgroup_id', 'price']]
df2 = df[['adgroup_id', 'cate_id', 'brand']]
print('\ndf1.head()\n' + str(df1.head()))
# print('\ndf2.head()\n' + str(df2.head()))
print('\ndf2[1:6]\n' + str(df2[1:6]))

df3 = pd.merge(df1, df2, on='adgroup_id', how='inner')
print('\ndf3.head()\n' + str(df3.head()))

print('\npd.concat()\n' + str(pd.concat([df[:4], df[10:15]], axis=0)))
print('\npd.concat()\n' + str(pd.concat([df[:4], df[10:15]], axis=1)))

df6 = pd.concat([df[:4], df[10:15].reset_index(drop=True)], axis=1)
print('\npd.concat()\n' + str(df6))
print('\ndf.columns\n' + str(df.columns))

print('\ndf6[\'cate_id\']\n' + str(df6['cate_id']))

# Missing Value
print('\ndf.shape\n' + str(df.shape))
print('\ndf.dropna().shape\n' + str(df.dropna().shape))
print('\ndf.fillna(0).head(10))\n' + str(df.fillna(0).head(10)))
print('\ndf.fillna(df[\'brand\'].mean()).head(10)\n' + str(df.fillna(df['brand'].mean()).head(10)))

print('\ndf.fillna(method=\'ffill\').head(10))\n' + str(df.fillna(method='ffill').head(10)))
price_des = df['price'].describe()
print('\nprice_des:\n' + str(price_des))

valid_max = price_des['50%'] + 3 * (price_des['75%'] - price_des['50%'])
valid_min = price_des['50%'] - 3 * (price_des['50%'] - price_des['25%'])
df['price'] = df['price'].clip(valid_min, valid_max)
print('\ndf[\'price\'].describe()\n' + str(df['price'].describe()))
