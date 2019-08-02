import stripe

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'home_payment.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        amount = self.request.GET.get('amount')
        amount = int(float(amount))
        print(type(amount))
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['amount'] = amount
        return context


def charge(request):
    if request.method == 'POST':
        # print("amount:", request.POST['amount'])
        amount = request.POST['amount']
        charge = stripe.Charge.create(
            amount=request.POST['amount'],
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html', {'amount': amount})