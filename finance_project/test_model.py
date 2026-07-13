import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

kmeans = joblib.load(BASE_DIR / "finance_project" / "models" / "kmeans_model.pkl")

print("Nombre de clusters :", kmeans.n_clusters)
print("Labels uniques :", set(kmeans.labels_))