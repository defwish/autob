import pandas as pd

data = pd.read_csv('Data.csv')
cantitati = pd.read_csv('Cantitati.csv')
comenzi = pd.read_csv('Comenzi.csv')
sucursale = pd.read_csv('Sucursale.csv')

comenzi_data = pd.merge(comenzi, data, on='numar_factura')

comenzi_data_quantities = pd.merge(comenzi_data, cantitati, on='id_cantitate')

comenzi_full = pd.merge(comenzi_data_quantities, sucursale, on='numar_comanda')

branch_filtered = comenzi_full[comenzi_full['sucursala'] == 'Bragadiru']

branch_filtered['data'] = pd.to_datetime(branch_filtered['data'], format='%m/%d/%Y')

january_2024_filtered = branch_filtered[
    (branch_filtered['data'].dt.month == 1) &
    (branch_filtered['data'].dt.year == 2024)
]

orders_with_returns = january_2024_filtered[
    january_2024_filtered['cantitate'] < 0
]

unique_orders_with_returns = orders_with_returns['numar_comanda'].unique()
total_orders_with_returns = len(unique_orders_with_returns)

orders_with_returns_all = comenzi_full[comenzi_full['cantitate'] < 0]

orders_per_branch = orders_with_returns_all.groupby('sucursala')['numar_comanda'].nunique().reset_index()

orders_per_branch.columns = ['Branch', 'Number of Orders with Returns']

print("\n" + "-"*50 + "\n")
print("\nNumarul de comenzi care au produse returnate pentru fiecare sucursala:")
print(orders_per_branch)
print("\n" + "-"*50 + "\n")
print(f'Numarul total de comenzi ce contin cel putin un produs returnat pentru sucursala "Bragadiru" in luna Ianuarie 2024: {total_orders_with_returns}')
print("\n" + "-"*50 + "\n")
