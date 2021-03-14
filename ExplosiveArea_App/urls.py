"""ExplosiveArea_App URL Configuration

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
from . import views, models
from django.urls import path, include


athletic_section = models.Excercise.ATHLETIC_FOR_ATHLETICS

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/basketball', views.basketball_view, name='basketball'),
    path('home/<section>', views.section_view, name='section'),
    path('home/<section>/delete/<id>', views.excercise_delete, name='excercise_delete'),
    path('home/<section>/<title>/<id>', views.excercise_view, name='excercise'),
    path('home/<section>/<title>/<id>/edit', views.excercise_edit_view, name='excercise_edit'),
    path('home/<section>/add-excercise', views.excercise_add_view, name='excercise_add'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]