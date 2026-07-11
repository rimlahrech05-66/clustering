from django.db import models

class Client(models.Model):
    current_age = models.IntegerField()
    yearly_income = models.FloatField()
    total_debt = models.FloatField()
    credit_score = models.IntegerField()
    num_credit_cards = models.IntegerField()

    cluster = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client {self.id} - Cluster {self.cluster}"
