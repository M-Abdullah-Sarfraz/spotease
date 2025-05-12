from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ads'


urlpatterns = [
    path('choose_category/', views.choose_category, name='choose_category'),
    path('post/<str:category>/', views.post_ad_and_payment, name='post_ad_and_payment'),
    # path('payment-details/', views.payment_details, name='payment-details'),
    path('post-success/', views.post_success, name='post_success'),
    # path('reserve/<int:ad_id>/', views.reserve_spot, name='reserve_spot'),        

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
