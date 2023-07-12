from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


# Create your views here.
# Cargar Vistas
def cargarInicio(request):
    products = Product.objects.all()
    lastitems = Product.objects.filter(stock__gt=0).order_by('-insdate')[:4]
    lastitems2 = Product.objects.filter(stock__gt=0).order_by('-insdate')[4:8]
    lastitems3 = Product.objects.filter(stock__gt=0).order_by('-insdate')[8:12]
    return render(request, "index.html", {"Prod": products, "Last": lastitems, "Last2": lastitems2, "Last3": lastitems3})


def buscar_productos(request):
    query = request.GET.get('q') 
    result = []
    if query:
        result = Product.objects.filter(name__icontains=query, stock__gt=0)[:4]

    results = [{'id':product.prod_id,'name':product.name,'img':product.img.url if product.img else None} for product in result]

    return JsonResponse({'results': results})

@staff_member_required(login_url='login')
def cAddProd(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "AddProd.html",{"Prod":products, "Cate":categories})

@staff_member_required(login_url='login')
def cAddCate(request):
    return render(request, "addCate.html")

@staff_member_required(login_url='login')
def cEdProd(request, id):
    products = Product.objects.get(prod_id = id)
    categories = Category.objects.all()

    cateId = products.id_cate

    ProdcateId = Category.objects.get(cate_id = cateId.cate_id).cate_id

    return render(request, "EdProd.html",{"Prod": products, "Cate":categories, "CateId": ProdcateId})

@staff_member_required(login_url='login')
def cedUser(request, username):
    user = User.objects.get(username = username)
    return render(request, "edUser.html", {"User": user})

def cProdview(request, id):
    products = Product.objects.get(prod_id = id)
    categories = Category.objects.all()

    cateId = products.id_cate

    cateID = Category.objects.get(cate_id = cateId.cate_id)

    ProdcateId = Category.objects.get(cate_id = cateId.cate_id).cate_id

    return render(request, "Product.html",{"Prod": products, "Cate":categories, "CateId": ProdcateId, "CateID":cateID})

@staff_member_required(login_url='login')
def cUserlist(request):
    usuarios = User.objects.all()
    return render(request, "UserList.html", {"Users": usuarios})

@staff_member_required(login_url='login')
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

def cCategories(request):
    products = Product.objects.all()
    catego = Category.objects.all()
    return render(request, "Category.html", {"Prod": products, "Cate": catego})

def cCates(request, id):
    productos = Product.objects.all()
    producto = Product.objects.filter(id_cate = id, stock__gt=0)
    cate = Category.objects.get(cate_id = id)
    return render(request, "categoria.html", {"Prod": productos,"Prodc": producto, "Cate":cate})

def cContact(request):
    return render(request, "contact.html")

@login_required(login_url='login')
def cmyAcc(request):
    return render(request, "micuenta.html")

@login_required(login_url='login')
def cedAcc(request, username):
    user = User.objects.get(username = username)
    return render(request, "edcuenta.html", {"User": user})

@login_required(login_url='login')
def cEditPass(request, username):
    user = User.objects.get(username = username)
    return render(request, "cpass.html", {"User": user})

@staff_member_required(login_url='login')
def listProd(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "ProductList.html",{"Prod":products, "Cate":categories})

@staff_member_required(login_url='login')
def cCatelist(request):
    categories = Category.objects.all()
    return render(request, "catelist.html",{"Cate":categories})

@staff_member_required(login_url='login')
def cEdCate(request, id):
    categoria = Category.objects.get(cate_id = id)

    return render(request, "edCate.html",{"Cate":categoria})

@login_required(login_url='login')
def cdelAcc(request, username):
    user = User.objects.get(username=username)
    return render(request, 'delAcc.html', {'User': user})

@login_required(login_url='login')
def cCarrito(request):
    prod = Product.objects.all()
    cate = Category.objects.all()
    return render(request, 'carroc.html', {'Prod': prod, 'Cate': cate})
# Cargar Vistas

# Funciones Vista

@staff_member_required(login_url='login')
def addProd(request):   
    add_name = request.POST['txTitle']
    add_author = request.POST['txAuthor']
    add_price = request.POST ['txPrice']
    add_stock = int(request.POST['txStock'])
    add_desc = request.POST['txDesc']
    add_img = request.FILES['iptImg']
    add_cate = Category.objects.get(cate_id = request.POST['optCate'])

    idcate = request.POST.get('optCate')

    counte = 0
    add_id = int(idcate + "000" + str(counte))

    while Product.objects.filter(prod_id=add_id).exists():
        counte += 1
        add_id = int(idcate + "000" + str(counte))

    if (add_stock <= 0):
        messages.error(request, 'El Stock no puede ser menor a 1.')
        return redirect('/AddProduct')


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

    return redirect('/Prodlist')

@staff_member_required(login_url='login')
def editProd(request):
    ed_id = request.POST['txSku']
    BProduct = Product.objects.get(prod_id = ed_id)
    ed_name = request.POST['txTitle']
    ed_author = request.POST['txAuthor']
    ed_price = request.POST['txPrice']
    ed_stock = int(request.POST['txStock'])
    ed_desc = request.POST['txDesc']
    ed_cate = Category.objects.get(cate_id = request.POST['optCate'])

    try:
        ed_img = request.FILES['iptImg']
        img_rute  = os.path.join(settings.MEDIA_ROOT, str(BProduct.img))
        os.remove(img_rute)
    except:
        ed_img = BProduct.img

    if (ed_stock <= 0):
        messages.error(request, 'El Stock no puede ser menor a 1.')
        return redirect('/edProd/'+ed_id)
    
    BProduct.name = ed_name
    BProduct.author = ed_author
    BProduct.price = ed_price
    BProduct.stock = ed_stock
    BProduct.desc = ed_desc
    BProduct.id_cate = ed_cate
    BProduct.img = ed_img
    
    BProduct.save()

    messages.success(request, 'El Producto ha sido Editado Exitosamente.')

    return redirect('/Prodlist')

@staff_member_required(login_url='login')
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

@staff_member_required(login_url='login')
def editUser(request):
    usernamel = request.user.username
    username = request.POST['txUser2']
    usern = request.POST['txUser']
    pemail = request.POST['txEmail2']
    uemail = request.POST['txEmail']
    staffcb = request.POST.get('txStaff') == 'on'
    apass = request.POST['txPassA']
    upass = request.POST['txUPass']

    user = authenticate(request, username=usernamel, password=apass)
    
    if (usern != username):
        if User.objects.filter(username=usern).exists():
            messages.error(request, 'El Nombre de Usuario ya está en uso.')
            return redirect('/edUser/'+ username)
    if (uemail != pemail):
        if User.objects.filter(email=uemail).exists():
            messages.error(request, 'El Email ya está en Uso.')
            return redirect('/edUser/'+ username)

    if user is not None:
        user = User.objects.get(username = username)
        user.username = usern
        user.email = uemail
        user.is_staff = staffcb
        if(upass != ''):
            user.set_password(upass)
        user.save()

        messages.success(request, 'El Usuario ha sido Editado Exitosamente.')
        return redirect('/userlist')
    else:
        messages.error(request, 'La Contraseña Ingresada es Incorrecta')
        return redirect('/edUser/'+ username)


@staff_member_required(login_url='login')
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

def obInfCate(request):
    cat_id = request.GET.get('id')
    categoria = Category.objects.get(cate_id=cat_id)

    categoria_info = {
        'name': categoria.cate_name
    }
    return JsonResponse(categoria_info)

@staff_member_required(login_url='login')
def addCate(request):
    add_name = request.POST['txTitle']
    add_img = request.FILES['iptImg']

    counte = 1
    add_cid = int(counte)

    while Category.objects.filter(cate_id=add_cid).exists():
        counte += 1
        add_cid = int(counte)

    if Category.objects.filter(cate_name = add_name).exists():
        messages.error(request, 'La Categoria Ya Existe.')
        return redirect('/AddCateg')
    else:
        Category.objects.create(
            cate_id = add_cid,
            cate_name = add_name,
            cate_img = add_img)
        
        messages.success(request, 'La Categoria ha sido Agregada Exitosamente.')

        return redirect('/Catelist')

@staff_member_required(login_url='login')
def editCate(request):
    ec_id = request.POST['txID']
    BPCate = Category.objects.get(cate_id = ec_id)
    ec_name = request.POST['txName']

    try:
        ec_img = request.FILES['iptImg']
        img_rute  = os.path.join(settings.MEDIA_ROOT, str(BPCate.cate_img))
        os.remove(img_rute)
    except:
        ec_img = BPCate.cate_img

    BPCate.cate_name = ec_name
    BPCate.cate_img = ec_img
    
    BPCate.save()

    messages.success(request, 'La Categoria ha sido Editado Exitosamente.')

    return redirect('/Catelist')

@staff_member_required(login_url='login')
def delCate(request,id):
    
    if Category.objects.filter(cate_id=id).exists():
        categoria = Category.objects.get(cate_id=id)
        categoria.delete()
        messages.error(request, 'La Categoria ha sido Eliminada Exitosamente.')
    else:
        messages.error(request, 'Categoria no Existe.')

    return redirect('/Catelist')

@login_required(login_url='login')
def editData(request):
    usernamel = request.user.username
    username = request.POST['txUser2']
    usern = request.POST['txUser']
    pemail = request.POST['txEmail2']
    uemail = request.POST['txEmail']
    apass = request.POST['txPass']

    user = authenticate(request, username=usernamel, password=apass)
    
    if (usern != username):
        if User.objects.filter(username=usern).exists():
            messages.error(request, 'El Nombre de Usuario ya está en uso.')
            return redirect('/edAcc/'+ username)
    if (uemail != pemail):
        if User.objects.filter(email=uemail).exists():
            messages.error(request, 'El Email ya está en Uso.')
            return redirect('/edAcc/'+ username)

    if user is not None:
        user = User.objects.get(username = username)
        user.username = usern
        user.email = uemail
        user.save()
        messages.success(request, 'Los Datos han sido Editados Exitosamente.')
        return redirect('/cMyAcc')
    else:
        messages.error(request, 'La Contraseña Ingresada es Incorrecta')
        return redirect('/edAcc/'+ username)

@login_required(login_url='login')
def editPass(request):
    usernamel = request.user.username
    apass = request.POST['txPass2']
    npass = request.POST['txPass']

    user = authenticate(request, username=usernamel, password=apass)
    
    if user is not None:
        user = User.objects.get(username = usernamel)
        user.set_password(npass)
        user.save()

        messages.success(request, 'Cambio de Contraseña Exitoso.')
        return redirect('/cMyAcc')
    else:
        messages.error(request, 'La Contraseña Ingresada es Incorrecta')
        return redirect('/edCon/'+ usernamel)

@login_required(login_url='login')
def delAcc(request):
    username = request.user.username
    passw = request.POST['txPass2']

    user = authenticate(request, username=username, password=passw)

    if user is not None:
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.delete()
            messages.error(request, 'El Usuario ha sido Eliminado Exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Usuario no Existe.')
            return redirect('login')
    else:
        messages.error(request, 'La Contraseña Ingresada es Incorrecta')
        return redirect('/cdelAcc/'+ username)

def descuento_stock(request):
    id = request.GET.get('id')
    cantidad = request.GET.get('cantidad')
    stock_pr = Product.objects.get(prod_id = id)
    stock_pr.stock -= int(cantidad)
    stock_pr.save()
    messages.success(request, 'Compra Exitosa')
    return redirect('inicio')