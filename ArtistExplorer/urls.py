from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('' , views.index , name = 'home'),
    path('add' , views.add , name = 'add'),
    path('edit' , views.edit , name = 'edit'),
    path('update/<int:pk>' , views.update , name = 'update'),
    path('delete/<int:pk>' , views.delete , name = 'delete')
    
] 


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)