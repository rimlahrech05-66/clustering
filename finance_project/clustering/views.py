from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

import joblib
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")
kmeans = joblib.load(BASE_DIR / "models" / "kmeans_model.pkl")


def ajouter_client(request):

    if request.method == "POST":

        form = ClientForm(request.POST)

        if form.is_valid():

            client = form.save(commit=False)

            data = pd.DataFrame({
                "current_age":[client.current_age],
                "yearly_income":[client.yearly_income],
                "total_debt":[client.total_debt],
                "credit_score":[client.credit_score],
                "num_credit_cards":[client.num_credit_cards]
            })

            X = scaler.transform(data)

            client.cluster = int(kmeans.predict(X)[0])

            client.save()

            return redirect("liste_clients")

    else:

        form = ClientForm()

    return render(request,"ajouter_client.html",{"form":form})
def liste_clients(request):

    clients = Client.objects.all()

    return render(
        request,
        "liste_clients.html",
        {"clients":clients}
    )