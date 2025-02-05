from django.contrib import admin
from django.urls import path
from webhooks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap1/v1/webhooks/order', views.WebhookOrderView.as_view() , name='webhoock-order'),
]
