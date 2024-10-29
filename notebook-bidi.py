# +
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import IPython
import seaborn as sns

df = pd.read_csv("db_exoplanete.csv", comment = '#', index_col = 'rowid')


df



# Je m'occupe du rayon de la planète et de la durée d'orbite

# -

for col in df.columns:
    print(col)

# +
X = df['sy_dist']
Y = df['pl_masse']

plt.xlabel("Distance de l'exoplanète à la Terre (en pc)")
plt.ylabel("Masse de l'exoplanète (en équivalent Terre)")
plt.title("Evolution de la masse de l'exoplanète en fonction de sa distance par rapport à la Terre")
plt.grid()
plt.yscale("log")
plt.xscale("log")
plt.scatter(X,Y, s = 2)
plt.show()


# +
y = df.pl_rade

plt.xlabel("Distance de l'exoplanète à la Terre (en pc)")
plt.ylabel("Rayon de l'exoplanète (en équivalent Terre)")
plt.title("Evolution du rayon de l'exoplanète en fonction de sa distance par rapport à la Terre")
plt.grid()
plt.ylim(0,25)
# plt.yscale("log")
# plt.xscale("log")
plt.scatter(X,y, s = 2)
plt.show()

# +
plt.grid()
plt.xlabel("Rayon de l'exoplanète (en équivalent Terre)")
plt.ylabel("Masse de l'exoplanète (en équivalent Terre)")
plt.title("Evolution de la masse de l'exoplanète en fonction de son rayon")
plt.ylim(0,2000)
plt.xlim(0,25)
plt.scatter(y,Y,s=2)
plt.show()



# +
x2 = df["pl_orbsmax"]
y2 = df["pl_eqt"]
df_relation = df.dropna(subset=['pl_orbsmax', 'pl_eqt'])

sns.regplot(x='pl_orbsmax', y='pl_mass', data = df_relation, scatter_kws={'s': 20, 'alpha':0.6}, line_kws={'color':'orange'})
plt.xlabel("Distance de l'exoplanète à son étoile (en UA)")
plt.ylabel("Température d'équilibre de la planète (en K)")
plt.xlim(0,1.5)
plt.title("Evolution de la température d'équilibre de l'exoplanète en fonction de sa distance à son étoile")
plt.scatter(x2,y2, s=0.5)


# -




