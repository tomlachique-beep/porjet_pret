

```python
import pandas as pd
import statsmodels.api as sm

# Charger les données
df = pd.read_excel("../data/donnees_pret.xlsx")

# Sélection des variables explicatives
X = df[["revenu", "age", "taux_endettement", "situation_familiale"]]
y = df["pret_accorde"]

# Ajouter une constante
X = sm.add_constant(X)

# Modèle OLS
model = sm.OLS(y, X).fit()

# Résultats
print(model.summary())
