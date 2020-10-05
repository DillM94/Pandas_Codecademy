import codecademylib
import pandas as pd

# 1 Loading 
inventory = pd.read_csv('inventory.csv')

# 2 Inspecting
#inventory.head(10)

# 3 Seperating Rows with Conditions
staten_island = inventory[inventory.location == 'Staten Island']

# 4 Seperating Rows
product_request = staten_island['product_description']

# 5 Multiple Conditions
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# 6 Adding Columns
inventory['in_stock'] = inventory.quantity.apply(lambda x: 
True if x > 0 
else False)

# 7 Interacting Columns
inventory['total_value'] = (inventory.price)*(inventory.quantity)

# 8 Marketing Lambda
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type, row.product_description)

# 9 Marketing Lambda
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)


## Final Check
print(inventory.head())