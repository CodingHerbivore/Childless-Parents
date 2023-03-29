import pandas as pd

# Should I add visible to this list?
fields = ['Item Type', 'Product ID', 'Product Name', 'Product Code/SKU']
dataframe1 = pd.read_csv('Full product export-2023-03-28.csv', usecols=fields)

print('The following Product IDs are missing Skus, indicating that they could be parents missing children:')

# The row_iterator last/next idea is taken from https://stackoverflow.com/questions/23151246/iterrows-pandas-get-next-rows-value
row_iterator = dataframe1.iterrows()
_, last = next(row_iterator)
for i, row in row_iterator:
    # Generally, a product that is missing a SKU is a parent, so the next row should be a SKU or Rule, not another product
    if last['Item Type'] == 'Product' and pd.isnull(last['Product Code/SKU']):
        if row['Item Type'] == 'Product':
            print(str(last['Product ID']) + '-' + last['Product Name'] )
    last = row

print('Done')