from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdPaymentForm  # Import the new combined form
from .models import AdPayment, Spot  # Corrected import to use AdPayment

# Post ad and payment details on the same page
def post_ad_and_payment(request, category):
    if request.method == 'POST':
        form = AdPaymentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the combined form (ad and payment details)
            form.save()
            # Redirect to payment success page after form submission
            return redirect('ads:post_success')
    else:
        form = AdPaymentForm()

    return render(request, 'post_ad_and_payment.html', {'form': form, 'category': category})



# Post success page
def post_success(request):
    return render(request, 'ad_post_success.html')  


# Category selection page (unchanged)
def choose_category(request):
    return render(request, 'ads/choose_category.html')

# List all ads (no payment details needed here)
def ads_list(request):
    ads = AdPayment.objects.all()  # Use AdPayment model to fetch all ads
    return render(request, 'ads/ads_list.html', {'ads': ads})

# Payment details function (not needed as it was handled in the form)
# def payment_details(request):
#     return HttpResponse("This page is no longer needed since ad and payment details are submitted together.")


# # Reserve a spot for a specific ad
# def reserve_spot(request, ad_id):
#     ad = get_object_or_404(AdPayment, id=ad_id)  # Correct model to AdPayment
#     payment_details = ad.paymentdetails_set.first()  # Get payment details related to the ad

#     return render(
#         request,
#         'view_payment_details.html',
#         {'ad': ad, 'payment_details': payment_details}
#     )
