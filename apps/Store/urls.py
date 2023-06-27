from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio, name='inicio'),
    path('AddProduct', views.cAddProd),
    path('search/', views.buscar_productos, name='buscar_productos'),
    path('cart', views.salesCart),
    path('edProd/<id>', views.cEdProd),
    path('Prodview/<id>', views.cProdview ),
    path('addPro', views.addProd),
    path('adminView', views.cadmStore),
    path('Prodlist', views.listProd),
    path('delProd/<id>', views.delProduct),
    path('eddProd', views.editProd),
    path('obtainProd', views.obInfProd),
    path('login', views.cLogin, name='login'),
    path('register', views.cRegister),
    path('contact', views.cContact),
    path('logout', views.logout_view),
]
