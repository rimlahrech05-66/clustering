from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

import joblib
import pandas as pd
from django.conf import settings

scaler = joblib.load(settings.BASE_DIR / "finance_project" / "models" / "scaler.pkl")
kmeans = joblib.load(settings.BASE_DIR / "finance_project" / "models" / "kmeans_model.pkl")

print("Nombre de clusters :", kmeans.n_clusters)


def ajouter_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)

            data = pd.DataFrame({
                "current_age": [client.current_age],
                "yearly_income": [client.yearly_income],
                "total_debt": [client.total_debt],
                "credit_score": [client.credit_score],
                "num_credit_cards": [client.num_credit_cards]
            })

            X = scaler.transform(data)

            prediction = kmeans.predict(X)
            print("Prédiction :", prediction)

            client.cluster = int(prediction[0])
            client.save()

            return redirect("liste_clients")

    else:
        form = ClientForm()

    return render(request, "ajouter_client.html", {"form": form})


def liste_clients(request):
    clients = Client.objects.all()
    return render(request, "liste_clients.html", {"clients": clients})