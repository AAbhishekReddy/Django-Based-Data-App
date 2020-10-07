from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class new_york(models.Model):
    token = models.CharField(max_length = 100, default = "7936104b73f9f19b7c1095ca6d3cbf673a57fbe6")
    company_symbol = models.CharField(max_length = 100)
    open_val = models.IntegerField()
    high_val = models.IntegerField()
    low_val = models.IntegerField()
    close_prediction = models.IntegerField(default = 0)
    date_time = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Data_app_home')

    def __repr__(self):
        return f"new_york('{self.company_symbol}', '{self.open_val}', '{self.high_val}', '{self.low_val}', '{self.close_prediction}', '{self.date_time}', '{self.users}')"

class beer_review(models.Model):
    token = models.CharField(max_length = 100, default = "7936104b73f9f19b7c1095ca6d3cbf673a57fbe6")
    beer_name = models.CharField(max_length = 100)
    review_aroma = models.IntegerField()
    review_pallete = models.IntegerField()
    review_taste = models.IntegerField()
    review_appearance = models.IntegerField()
    beer_abv = models.IntegerField()
    prediction_review = models.IntegerField(default = 0)
    date_time = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Data_app_home')

    def __repr__(self):
        return f"new_york('{self.beer_name}', '{self.review_aroma}', '{self.user_id}')"