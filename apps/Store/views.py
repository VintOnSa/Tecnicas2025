from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


# Create your views here.
# Cargar Vistas
def cargarInicio(request):
    products = Product.objects.all()
    lastitems = Product.objects.order_by('-insdate')[:4]
    lastitems2 = Product.objects.order_by('-insdate')[4:8]
    lastitems3 = Product.objects.order_by('-insdate')[8:12]
    return render(request, "index.html", {"Prod": products, "Last": lastitems, "Last2": lastitems2, "Last3": lastitems3})


def buscar_productos(request):
    query = request.GET.get('q') 
    result = []
    if query:
        result = Product.objects.filter(name__icontains=query)[:4]

    results = [{'id':product.prod_id,'name':product.name,'img':product.img.url if product.img else None} for product in result]

    return JsonResponse({'results': results})

def cAddProd(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "AddProd.html",{"Prod":products, "Cate":categories})


def cEdProd(request, id):
    products = Product.objects.get(prod_id = id)
    categories = Category.objects.all()

    cateId = products.id_cate

    ProdcateId = Category.objects.get(cate_id = cateId.cate_id).cate_id

    return render(request, "EdProd.html",{"Prod": products, "Cate":categories, "CateId": ProdcateId})


def cProdview(request, id):
    products = Product.objects.get(prod_id = id)
    categories = Category.objects.all()

    cateId = products.id_cate

    ProdcateId = Category.objects.get(cate_id = cateId.cate_id).cate_id

    return render(request, "Product.html",{"Prod": products, "Cate":categories, "CateId": ProdcateId})

def cUserlist(request):
    usuarios = User.objects.all()
    return render(request, "UserList.html", {"Users": usuarios})

@login_required
def cadmStore(request):
    user = request.user
    user_type = user.is_staff
    return render(request, "admin.html")

def cLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            
            if user.is_staff:
                messages.success(request, 'Bienvenido Administrador.')
                return redirect('/adminView')
            else:
                messages.success(request, 'Bienvenido Usuario.')
                return redirect('inicio')
        else:
            messages.error(request, 'Los Datos Ingresados son Incorrectos.')
            
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('inicio')

def cRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El Nombre de Usuario ya está en uso.')
            return render(request, 'register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El Email ya está en Uso.')
            return render(request, 'register.html')
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=username, password=password, email=email)

            messages.success(request, 'Usuario creado con Exito.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, Ingrese los Datos Solicitados de Manera Correcta.')
    
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def obInfUser(request):
    use_id = request.GET.get('id')
    usuario = User.objects.get(username=use_id)

    user_info = {
        'name': usuario.username
    }
    return JsonResponse(user_info)


def delUser(request,username):
    
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        if user.is_staff:
            messages.error(request, 'No se puede eliminar a un Administrador')
            return redirect('/userlist')
        else:
            user.delete()
            messages.error(request, 'El Usuario ha sido Eliminado Exitosamente.')
    else:
        messages.error(request, 'Usuario no Existe.')

    return redirect('/userlist')

def cContact(request):
    return render(request, "contact.html")

def listProd(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "ProductList.html",{"Prod":products, "Cate":categories})
# Cargar Vistas

# Funciones Vista

def addProd(request):   
    add_name = request.POST['txTitle']
    add_author = request.POST['txAuthor']
    add_price = request.POST ['txPrice']
    add_stock = request.POST['txStock']
    add_desc = request.POST['txDesc']
    add_img = request.FILES['iptImg']
    add_cate = Category.objects.get(cate_id = request.POST['optCate'])

    idcate = request.POST.get('optCate')

    catego = Category.objects.get(cate_id = idcate)
    counte = Product.objects.filter(id_cate = catego).count()

    add_id = int(idcate + "000" + str(counte + 1))


    Product.objects.create(
        prod_id = add_id,
        name = add_name,
        author = add_author,
        price = add_price,
        id_cate = add_cate,
        desc = add_desc,
        stock = add_stock,
        img = add_img)
    
    messages.success(request, 'El Producto ha sido Agregado Exitosamente.')

    return redirect('/AddProduct')

def cCategories(request):
    products = Product.objects.all()
    catego = Category.objects.all()
    return render(request, "Category.html", {"Prod": products, "Cate": catego})

def editProd(request):
    ed_id = request.POST['txSku']
    BProduct = Product.objects.get(prod_id = ed_id)
    ed_name = request.POST['txTitle']
    ed_price = request.POST['txPrice']
    ed_stock = request.POST['txStock']
    ed_desc = request.POST['txDesc']
    ed_cate = Category.objects.get(cate_id = request.POST['optCate'])

    try:
        ed_img = request.FILES['iptImg']
        img_rute  = os.path.join(settings.MEDIA_ROOT, str(BProduct.img))
        os.remove(img_rute)
    except:
        ed_img = BProduct.img

    BProduct.name = ed_name
    BProduct.price = ed_price
    BProduct.stock = ed_stock
    BProduct.desc = ed_desc
    BProduct.id_cate = ed_cate
    BProduct.img = ed_img
    
    BProduct.save()

    messages.success(request, 'El Producto ha sido Editado Exitosamente.')

    return redirect('/Prodlist')

def delProduct(request,id):
    product = Product.objects.get(prod_id = id)
    product.delete()
    img_rute  = os.path.join(settings.MEDIA_ROOT, str(product.img))
    os.remove(img_rute)

    messages.error(request, 'El Producto ha sido Eliminado Exitosamente.')

    return redirect('/Prodlist')

def obInfProd(request):
    pro_id = request.GET.get('id')
    producto = Product.objects.get(prod_id=pro_id)

    producto_info = {
        'name': producto.name
    }
    return JsonResponse(producto_info)




def salesCart(request):
    #print("texto",request.body)

    data = json.loads(request.body)

    for i in data:
        print("Sku:",i['sku'])
        print("Name:",i['name'])
        print("Amount:",i['amount'])

    return HttpResponse("Texto")