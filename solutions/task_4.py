import pandas as pd

csv = pd.read_csv('../fourth_task.txt',
                  sep=',', decimal='.', index_col='product_id')

print(csv.columns)
csv = csv.drop('expiration_date', axis=1)
print(csv.columns)

avg_rating = csv['rating'].mean()
print('Среднее по rating: ', avg_rating)

max_rating = csv['rating'].max()
print('Максимум по rating: ', max_rating)

min_price = csv['price'].min()
print('Минимум по price: ', min_price)

filtered = csv[csv['status'] != 'Shipping']

filtered.to_csv('../outputs/output_4.csv')

with open('../outputs/output_4.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f'Среднее по rating: {avg_rating}\n')
    output_file.write(f'Максимум по rating: {max_rating}\n')
    output_file.write(f'Минимум по price: {min_price}\n')
