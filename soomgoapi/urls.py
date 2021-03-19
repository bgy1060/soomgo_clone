"""soomgoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from IPython.core.release import url
from django.contrib import admin
from django.urls import path,include
from region import views as r
from users import views as u
from category import views as c
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('category/<str:cat_name>/<str:detail_name>', c.sub_category),
    path('category/<str:cat_name>', c.detail_category),
    path('category/', c.category_list),

    path('users/region/<str:region_name>', u.region_user),
    path('users/category/<str:cat_name>', u.cat_user),
    path('users/region/<str:region_name>/category/<str:cat_name>', u.region_cat_user),

    path('region/',r.region_list),
    path('region/<str:region_name>', r.detail_region),

    path('info/<int:uid>',u.info_list),

    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
