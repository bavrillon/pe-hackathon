# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
import common_boiarsky_
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('db_exoplanete.csv',on_bad_lines='skip', comment='#', index_col='rowid')
df

# +
# Nombre d'exoplanètes découvertes par année
df['disc_year'] = pd.to_numeric(df['disc_year'], errors='coerce')
discovery_years = df['disc_year'].dropna()

plt.figure(figsize=(12, 6))
plt.hist(discovery_years, bins=30, edgecolor='k', alpha=0.7)
plt.title("Distribution of Exoplanet Discoveries by Year")
plt.xlabel("Discovery Year")
plt.ylabel("Number of Discoveries")
plt.show()

# +
# Nombre d’exoplanètes découvertes par année
discoveries_per_year = df['disc_year'].value_counts().sort_index()

yearly_discoveries_df = pd.DataFrame({'Year': discoveries_per_year.index, 'Discoveries': discoveries_per_year.values})

plt.figure(figsize=(12, 6))
sns.regplot(x='Year', y='Discoveries', data=yearly_discoveries_df, scatter_kws={"s": 50, "alpha": 0.7}, line_kws={"color": "orange"})
plt.title("Number of Exoplanet Discoveries by Year with Linear Trend")
plt.xlabel("Discovery Year")
plt.ylabel("Number of Discoveries")
plt.show()
# -

# Répartition des exoplanètes par méthode de découverte
plt.figure(figsize=(10,6))
sns.countplot(y='discoverymethod', data=df, order=df['discoverymethod'].value_counts().index)
plt.title("Distribution of Exoplanet Discoveries by Discovery Method")
plt.xlabel("Number of Discoveries")
plt.ylabel("Discovery Method")
plt.show()

# +
#Comparaison de l’année de découverte avec la masse des exoplanètes
df['pl_masse'] = pd.to_numeric(df['pl_masse'], errors='coerce')
df_filtered_mass = df.dropna(subset=['disc_year', 'pl_masse'])

plt.figure(figsize=(12, 6))
sns.scatterplot(x='disc_year', y='pl_masse', data=df_filtered_mass, alpha=0.6, label='Planet Mass')

plt.title("Planet Mass by Discovery Year")
plt.xlabel("Discovery Year")
plt.ylabel("Planet Mass (Earth mass)")
plt.show()

# +
# Comparaison de l’année de découverte avec la distance de l’étoile hôte
df['sy_dist'] = pd.to_numeric(df['sy_dist'], errors='coerce')
df_filtered_dist = df.dropna(subset=['disc_year', 'sy_dist'])

plt.figure(figsize=(12, 6))
sns.scatterplot(x='disc_year', y='sy_dist', data=df_filtered_dist, alpha=0.7)
plt.title("Distance of Host Star by Discovery Year")
plt.xlabel("Discovery Year")
plt.ylabel("Distance to Host Star (pc)")
plt.show()

# +
# Vérification de la troisième loi de Kepler

df['pl_orbper'] = pd.to_numeric(df['pl_orbper'], errors='coerce')
df['pl_orbsmax'] = pd.to_numeric(df['pl_orbsmax'], errors='coerce')
df_kepler = df.dropna(subset=['pl_orbper', 'pl_orbsmax'])

df_kepler['log_orbper'] = np.log10(df_kepler['pl_orbper'])
df_kepler['log_orbsmax'] = np.log10(df_kepler['pl_orbsmax'])

plt.figure(figsize=(12, 6))
sns.regplot(x='log_orbsmax', y='log_orbper', data=df_kepler, line_kws={"color": "orange"})
plt.title("Verification of Kepler's third law")
plt.xlabel("Log of semi-Major axis (AU)")
plt.ylabel("Log of orbital period (days)")
plt.show()



# +
# relation entre l’excentricité des orbites des exoplanètes et la masse de leur étoile hôte
df['pl_orbeccen'] = pd.to_numeric(df['pl_orbeccen'], errors='coerce')
df['st_mass'] = pd.to_numeric(df['st_mass'], errors='coerce')
df_excentricity_mass = df.dropna(subset=['pl_orbeccen', 'st_mass'])

plt.figure(figsize=(12, 6))
sns.regplot(x='st_mass', y='pl_orbeccen', data=df_excentricity_mass, scatter_kws={'s': 20, 'alpha': 0.6}, line_kws={'color': 'orange'})
plt.title("Relationship between stellar mass and orbital eccentricity")
plt.xlabel("Stellar mass (Solar masses)")
plt.ylabel("Orbital eccentricity")
plt.show()

# +
# relation entre la masse des exoplanètes et de leur étoile hôte
df['pl_masse'] = pd.to_numeric(df['pl_masse'], errors='coerce')
df['st_mass'] = pd.to_numeric(df['st_mass'], errors='coerce')
df_mass_relation = df.dropna(subset=['pl_masse', 'st_mass'])

plt.figure(figsize=(12, 6))
sns.regplot(x='st_mass', y='pl_masse', data=df_mass_relation, scatter_kws={'s': 20, 'alpha': 0.6}, line_kws={'color': 'orange'})
plt.yscale('log')  
plt.title("Relationship between Stellar mass and Planetary mass")
plt.xlabel("Stellar Mass (Solar Masses)")
plt.ylabel("Planetary Mass (Earth Mass)")
plt.show()
# -


