
from django.contrib import admin
from django.urls import path
from Weather_app import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header="ADMIN PANEL"
admin.site.site_title="ADMIN MODE "
admin.site.index_title="Welcome to Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
