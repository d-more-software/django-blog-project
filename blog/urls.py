from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ArticlesList.as_view(), name= 'articles_view'),
    path('<slug:slug>', views.ArticleDetails.as_view(), name= 'article_Details_View'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)