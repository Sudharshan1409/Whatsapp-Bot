import pandas as pd

df = pd.read_csv('selected_contacts.csv')

for name in df['Name']:
    print(name)
