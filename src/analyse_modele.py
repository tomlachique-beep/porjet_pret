import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


DATA_PATH = "data/donnees_pret.xlsx"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    # Chargement du fichier de données Excel
    df = pd.read_excel(path)
    return df


def build_ols_model(df: pd.DataFrame,
                    target_col: str,
                    feature_cols: list):
    # Séparation entre la variable cible et les variables explicatives
    X = df[feature_cols].copy()
    y = df[target_col].copy()

    # Ajout de la constante pour estimer l'intercept
    X = sm.add_constant(X)

    # Construction du modèle OLS
    model = sm.OLS(y, X)
    results = model.fit()
    return results


def main():
    # 1. Charger les données
    df = load_data()
    print("Aperçu des données :")
    print(df.head())
    print("\nInfos sur le DataFrame :")
    print(df.info())

    # On garde seulement les lignes où PRET n'est pas manquant
    df = df[df["PRET"].notna()].copy()

    # Définition de la variable à expliquer et des variables explicatives
    target_col = "PRET"
    feature_cols = [
        "TX_ENDET (X1)",
        "ANTEC (X2)",
        "PRIX(X3)",
        "REVENU(X4)",
        "MARIAGE (X5)",
        "EMP (X6)",
        "TAUX (X7)",
    ]

    # Vérification rapide que les colonnes existent
    missing = [col for col in [target_col] + feature_cols if col not in df.columns]
    if missing:
        print("\nColonnes introuvables dans les données :")
        print(missing)
        print("Merci d'adapter target_col et feature_cols dans analyse_modele.py.")
        return

    # 3. Construire le modèle
    results = build_ols_model(df, target_col, feature_cols)

    # 4. Afficher le résumé du modèle
    print("\nRésumé du modèle OLS :")
    print(results.summary())

    # 5. Exemple de visualisation simple
    plt.figure()
    plt.scatter(df["REVENU(X4)"], df[target_col])
    plt.xlabel("Revenu (REVENU(X4))")
    plt.ylabel("Montant du prêt (PRET)")
    plt.title("Relation entre revenu et montant de prêt accordé")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()




