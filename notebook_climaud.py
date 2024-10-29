import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('db_exoplanete.csv',on_bad_lines='skip', comment = "#", index_col = 'rowid')

df.head(10)

plt.figure()
plt.hist(df['sy_dist'], bins = 1000)
plt.title('Distance des objets au système solaire')
plt.xlabel('Planètes')
plt.ylabel('Distance (en parsecs)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

for col in df.columns:
    print (col)

distance= df['sy_dist'].dropna()
radius = df['pl_rade'].dropna()

# +
plt.figure()
plt.hist(df['sy_snum'], bins = 6)
plt.title("Nombre d'étoiles")
plt.xlabel('Planètes')
plt.ylabel("Nombre d'étoiles par planète")

plt.show()

# +

plt.figure()
plt.scatter(df['disc_year'], df['sy_dist'], s = 2)
plt.plot([2000, 2025], [0, 6000], color = 'red')
plt.title('Distance de la planète en fonction de lannée de découverte')
plt.xlabel('Année de découverte')
plt.ylabel('Distance ( en parsecs = 3,26 année lumière)')
plt.ylim(0, 10000)
plt.show()
# -





plt.figure()
plt.scatter(df['pl_orbsmax'], df['pl_orbeccen'], s = 2)
plt.xlim(0, 60)
plt.xlabel('Demi-grand-axe (en u.a)')
plt.ylabel('Excentricité')
plt.title(' Excentricité en fonction du demi-grand-axe')
plt.show()


