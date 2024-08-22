#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import random

# Sales Data
dates = pd.date_range(start="2023-01-01", end="2024-01-01", freq="M")
products = ["Product_A", "Product_B", "Product_C", "Product_D"]
stores = ["Store_1", "Store_2", "Store_3", "Store_4"]

sales_data = []

for date in dates:
    for store in stores:
        for product in products:
            sales = random.randint(50, 500)
            sales_data.append([date, store, product, sales])

sales_df = pd.DataFrame(sales_data, columns=["Date", "Store", "Product", "Sales"])
sales_df.to_csv("sales_data.csv", index=False)

# Inventory Data
inventory_data = []

for date in dates:
    for store in stores:
        for product in products:
            inventory = random.randint(100, 1000)
            inventory_data.append([date, store, product, inventory])

inventory_df = pd.DataFrame(inventory_data, columns=["Date", "Store", "Product", "Inventory"])
inventory_df.to_csv("inventory_data.csv", index=False)

# Customer Data
customer_data = []

for date in dates:
    for store in stores:
        footfall = random.randint(1000, 10000)
        satisfaction = random.uniform(3.0, 5.0)
        customer_data.append([date, store, footfall, satisfaction])

customer_df = pd.DataFrame(customer_data, columns=["Date", "Store", "Footfall", "Satisfaction"])
customer_df.to_csv("customer_data.csv", index=False)


# In[2]:


import pandas as pd

# Load Data
sales_df = pd.read_csv("sales_data.csv")
inventory_df = pd.read_csv("inventory_data.csv")
customer_df = pd.read_csv("customer_data.csv")

# Display summary statistics
print(sales_df.describe())
print(inventory_df.describe())
print(customer_df.describe())


# In[ ]:




