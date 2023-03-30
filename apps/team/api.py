import json
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Team


@login_required
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    data = json.loads(request.body)
    plan = data['plan']

    if plan == 'basic':
        price_id = settings.STRIPE_BASIC_PRICE_ID
    else:
        price_id = settings.STRIPE_PRO_PRICE_ID

    try:
        checkout_session = stripe.checkout.Session.create(
            client_reference_id = request.user.userprofile.active_team_id,
            success_url = '%s%s?session_id={CHECKOUT_SESSION_ID}' % (settings.WEBSITE_URL, reverse('team:plans_thankyou')),
            cancel_url = '%s%s' % (settings.WEBSITE_URL, reverse('team:plans')),
            payment_method_types = ['card'],
            mode = 'subscription',
            line_items = [
                {
                    'price': price_id,
                    'quantity': 1
                }
            ]
        )
        return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
        return JsonResponse({'error': str(e)})
