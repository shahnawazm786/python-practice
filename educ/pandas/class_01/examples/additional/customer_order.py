import pandas as pd

data = {
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry']
}

customer = pd.DataFrame(data)
print(customer)

data = {
    'order_id': ['OR1', 'OR3', 'OR23', 'OR42'],
    'cust_id': [102, 105, 101, 102],
    'amount': [1200, 650, 120, 989]
}
orders=pd.DataFrame(data)
print(customer)
print(orders)
merge_df=customer.merge(orders,on='cust_id')
print(merge_df)
sum_of_amount=merge_df['amount'].sum()
print(sum_of_amount)