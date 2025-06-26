import pandas as pd
import matplotlib.pyplot as plt

juegos = pd.read_csv('/Users/erickandrenaunay/Documents/Work/TripleTen/DS-DA Curso/Sprint #7/43_DS/games.csv')

juegos.info()

print(juegos.head())

juegos['total_ventas'] = juegos['NA_sales'] + juegos['EU_sales'] + juegos['JP_sales']

print()

ventas_x_anio = juegos.groupby('Year_of_Release')['total_ventas'].sum().sort_index()

ventas_x_anio.plot()
plt.show()


