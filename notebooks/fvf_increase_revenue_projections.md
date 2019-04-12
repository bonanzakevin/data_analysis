

```python
import pandas as pd
import numpy as np
import plotly_express as px
import colorlover as cl
import random
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as po
```


```python


categories = ["Computers/Tablets & Networking >> Software", "Parts & Accessories >> Car & Truck Parts", "Health & Beauty >> Vitamins & Dietary Supplements", "Fashion >> Men's Shoes", "Home & Garden >> Yard, Garden & Outdoor Living", "Fashion >> Women's Handbags & Bags", "Fashion >> Men's Clothing", "Health & Beauty >> Health Care", "DVDs & Movies >> DVD, HD DVD & Blu-ray", "Jewelry & Watches >> Watches"]
category_names = ["Software", "Car & Truck Parts", "Vitamins", "Men's shoes", "Home & Garden", "Handbags", "Men's clothing", "Health care","DVDs & Blu-ray",  "Watches"]
category_ids = [18793, 6030, 180959, 93427, 159912, 169291, 1059, 67588, 617, 14324]
top_sellers_fvf = { "Software" : .143, 
                   "Car & Truck Parts":.128, 
                   "Vitamins":.17, 
                   "Men's shoes":.168, 
                   "Home & Garden":.139, 
                   "Handbags": .098, 
                   "Men's clothing": .17, 
                   "Health care":.16, 
                   "DVDs & Blu-ray":.13, 
                   "Watches":.116
                  }


#Load Data from CSVs
df1 = pd.read_csv("../csv/offer_info.csv")
df2 = pd.read_csv("../csv/max_fvf.csv")


#Merge into a new dataframe
new_df = df1.merge(df2, how="left", left_on="seller_id", right_on="seller_id")

df3 = pd.read_csv("../csv/category_per_offer.csv")

q1_offers = new_df.merge(df3, how="left", left_on="id", right_on = "id")


#Replace category_id with category name
for name, cat_id in zip(category_names, category_ids):
    q1_offers.replace(cat_id, name, inplace=True)


#Add column for the actual FVF level that a 
q1_offers['fvf_level_paid'] = q1_offers['fvf']/q1_offers['amount']


sum_df = q1_offers.groupby('category_id').sum().drop(['id', 'seller_id'], axis=1).reset_index()
mean_df = q1_offers.groupby('category_id').mean().drop(['id', 'seller_id'], axis=1).reset_index()

for key, value in top_sellers_fvf.items():
    for category in mean_df['category_id']:
        if category == key:
            mean_df['fvf_diff'] = mean_df['max_fvf'] - value*100
```


```python
#If every seller increased their FVF by 1 level then how much would we make. 
#What if we only increased the FVF of 10% of sellers at random

#The goal is to show the projected value of sellers in these categories increase their max_fvf
#So I need to group the df by seller and sum the amount and fvf
#Then I need to randomly pick 10% of those sellers
#For each of those sellers orders we need to increase the max_fvf
#Then I multply that number by the average difference between their max_fvf and their fvf_level_paid
#Take this new_max_fvf and multiply it by the amount to get the new fvf per order
#compare those sums

updated_q1_offers = q1_offers.copy()


sellers_sum = q1_offers.groupby('seller_id').sum().reset_index()

sample = sellers_sum['seller_id'].sample(frac=0.01)


#update FVF for random sample of sellers
new_fvf = []
for i in range(len(updated_q1_offers)):
    if updated_q1_offers.seller_id[i] in sample.values:
        if updated_q1_offers.max_fvf[i] == 3.5:
            new_fvf.append(9.0)
        elif updated_q1_offers.max_fvf[i] == 9.0:
            new_fvf.append(13.0)
        elif updated_q1_offers.max_fvf[i] == 13.0:
            new_fvf.append(19.0)
        elif updated_q1_offers.max_fvf[i] == 19.0:
            new_fvf.append(30.0)
        else:
            new_fvf.append(updated_q1_offers.max_fvf[i])
    else: 
        new_fvf.append(updated_q1_offers.max_fvf[i])       

updated_q1_offers['new_fvf'] = new_fvf

#what is the difference between the fvf_level_paid and the max_fvf
updated_q1_offers['fvf_diff'] = updated_q1_offers['fvf_level_paid']/updated_q1_offers['max_fvf']

#what would the seller actually pay with the increased fvf_level
updated_q1_offers['actual_fvf'] = updated_q1_offers['new_fvf']*updated_q1_offers['fvf_diff']

#what is the new fvf revenue collected
updated_q1_offers['new_revenue'] = updated_q1_offers['amount']*updated_q1_offers['actual_fvf']

#How much different is that revenue from the previous
updated_q1_offers['revenue_increase'] = updated_q1_offers['new_revenue']-updated_q1_offers['fvf']


old_seller_value = q1_offers.groupby('category_id').sum()
new_seller_value = updated_q1_offers.groupby('category_id').sum()

print(new_seller_value.revenue_increase.sum())

```

    2689.7759751943945



```python
#Create Bar Chart
trace1 = go.Bar(
        x = mean_df.category_id,
        y = mean_df.max_fvf/100,
        text = (mean_df.max_fvf/100).map("{:,.2f}".format),
        textposition = 'auto',
        textfont=dict(
                color='black',
                size=14,
            ),
        marker = dict(
              color = cl.scales['10']['qual']['Paired']
            ),
        name = 'Average max_fvf for Sellers'
)

trace2 = go.Bar(
        x = mean_df.category_id,
        y = list(top_sellers_fvf.values()),
        text = list(top_sellers_fvf.values()),
            textposition = 'auto',
            textfont=dict(
                    color='black',
                    size=14,
                ),
        marker = dict(
              color = cl.scales['10']['div']['Spectral']
            ),
        name = 'Top Seller FVF level'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group',
    title = 'Average FVF level paid compared to top sellers'
)

fig = go.Figure(data=data, layout=layout)
po.plot(data)
```




    'file:///Users/kevin/data_analysis/notebooks/temp-plot.html'




```python
trace1 = go.Bar(
        x = mean_df.category_id,
        y = mean_df.fvf_level_paid,
        marker = dict(
              color = cl.scales['10']['qual']['Paired']
            ),
        name = 'FVF level paid'
)
trace2 = go.Bar(
        x = mean_df.category_id,
        y = mean_df.max_fvf/100,
        marker = dict(
              color = cl.scales['10']['div']['Spectral']
            ),
        name = 'Max_FVF'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
po.plot(data)
```




    'file:///Users/kevin/data_analysis/notebooks/temp-plot.html'




```python
import locale
trace1 = go.Bar(
        x = new_seller_value.index,
        y = new_seller_value.fvf,
        marker = dict(
            color = cl.scales['10']['qual']['Paired'],
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
    
        name = "Q1 FVF's"
)
trace2 = go.Bar(
        x = new_seller_value.index,
        y = new_seller_value.new_revenue,
        text = new_seller_value.revenue_increase.map("${:,.2f}".format),
        textposition = 'auto',
        textfont=dict(
                color='black',
                size=14,
            ),
        marker = dict(
            color = cl.scales['10']['div']['Spectral'],
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
            ),
        name = "Increased fvf"
)

data = [trace1, trace2]
layout = go.Layout(
    title="none",
    barmode='group',
    
)

fig = go.Figure(data=data, layout=layout)
py.plot(data)
```




    'https://plot.ly/~kevinbigfoot/137'




```python

```


```python

```
