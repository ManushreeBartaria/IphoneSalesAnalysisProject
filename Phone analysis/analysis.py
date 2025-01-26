import numpy as np
import pandas as pd
import plotly.express as px
data=pd.read_csv("apple_products.csv")
#print(data.describe())
sorted_onrating=data.sort_values(by=["Star Rating"], ascending=False)
top_10=sorted_onrating.head(10)
#print(top_10)
top5rating=top_10.head(5)
#print(top5rating[["Star Rating","Product Name"]])
#print(top_10["Product Name"].value_counts().index)
'''names=top_10["Product Name"].value_counts().index
ratings=top_10["Number Of Ratings"]
figure=px.bar(top_10, x=names,y=ratings,title="Top rated Iphone Analysis Chart")
figure.show()'''

rat=data["Number Of Ratings"]
sales=data["Sale Price"]
fig=px.line(data,x=rat ,y=sales, title="Relationship between ratings and sales price")
fig.show()