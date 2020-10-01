from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from django.contrib import messages

from .models import new_york, beer_review
from .support.regression import nyse_reg, beer_reg


def home(request):
    return render(request, 'data_app/home.html')

def about(request):
    return render(request, 'data_app/about.html')

class NewYorkListView(LoginRequiredMixin, ListView):
    model = new_york
    template_name = 'data_app/nyse.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_time']

class BeerListView(LoginRequiredMixin, ListView):
    model = beer_review
    template_name = 'data_app/beer_review.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'beers'
    ordering = ['-date_time']

class NewYorkCreateView(LoginRequiredMixin, CreateView):
    model = new_york
    fields = ['company_symbol', 'open_val', 'high_val', 'low_val']

    def form_valid(self, form):
        form.instance.users = self.request.user

        vals = list([form.instance.company_symbol, form.instance.open_val, form.instance.high_val, form.instance.low_val])
        vals = nyse_reg(vals)
        form.instance.close_prediction = vals[-1]
        messages.success(self.request, f'Prediction Successful. Veiw it under NYSE!')
        return super().form_valid(form)

class BeerCreateView(LoginRequiredMixin, CreateView):
    model = beer_review
    fields = ['beer_name', 'review_aroma', 'review_pallete', 'review_taste', 'review_appearance', 'beer_abv']

    def form_valid(self, form):
        form.instance.users = self.request.user

        vals = list([form.instance.review_aroma, form.instance.review_pallete, form.instance.review_taste])
        vals = beer_reg(vals)
        form.instance.prediction_review = vals[-1]
        messages.success(self.request, f'Prediction Successful. Veiw it under Beer Review!')
        return super().form_valid(form)
