import pandas as pd

connections_db = [
    {
        'user_name': 'etl_user',
        'password': '123',
        'host': '127.0.0.1'
    },
    {
        'user_name': 'test_user',
        'password': '456',
        'host': '127.0.0.1'

}
]

df1 = pd.DataFrame(connections_db)
print(df1)
print(type(df1))
df1.to_csv('from_pandas.csv', index=False)
df2 = pd.read_csv('from_pandas.csv')
print(df2)
print(type(df2))