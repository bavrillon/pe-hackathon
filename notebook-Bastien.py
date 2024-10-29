import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import common_Bastien_

df = pd.read_csv('db_exoplanete.csv',on_bad_lines='skip',comment='#',index_col='rowid')

df.head()

df_filtered = df[(df['pl_insol'] <= 4000) & (df['st_teff'] <= 7500)]
df_filtered.plot(x='pl_insol', y='st_teff', kind='scatter', s=1)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Flux d'insolation de la planète (en Flux Solaire)") 
plt.ylabel("Température de la planète (en K)")  
plt.title("Evolution de la température des planètes en fonction de leur insolation (échelles logarithmiques)")
plt.show()

Mt = 5.972*(10**24)
df_filtered_2 = df
df_filtered_2['pl_masse_kg'] = df_filtered['pl_masse']*Mt
df_filtered_2.plot(x='pl_masse_kg', y='pl_dens', kind='scatter', s=1)
plt.xlabel("Masse de la planète (en kg)") 
plt.ylabel("Densité de la planète (g/cm^3)")  
plt.title("Evolution de la densité des planètes en fonction de leur masse")
plt.show()

g = df.groupby('discoverymethod').size()
g.plot(kind='pie', autopct='%1.1f%%', figsize=(5, 8))
plt.title("Distribution des exoplanètes par méthode de découverte")
plt.show()


