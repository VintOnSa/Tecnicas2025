var array_productos = [];

if (localStorage.getItem('Productos')) {
    array_productos = JSON.parse(localStorage.getItem('Productos')) || [];
}else{
    localStorage.setItem('Productos', JSON.stringify(array_productos));
}

function comprar(id) {
    var producto = $('#producto-' + id);

    var p = {
        id: id,
        img: producto.data('img'),
        nombre: producto.data('nombre'),
        precio: producto.data('precio'),
        cantidad: producto.data('amount')
    };
// Verificar si el producto ya existe en el array de productos
    var index = array_productos.findIndex(function(producto) {
        return producto.id === id;
    });

    if (index !== -1) {
        // Si el producto ya existe, sumar la cantidad
        array_productos[index].cantidad += 1;
    } else {
        // Si el producto no existe, agregarlo al array
        p.cantidad = 1;
        array_productos.push(p);
    }

    // Realizar la suma de cantidades para los productos repetidos
    array_productos1 = sumarProductosRepetidos(array_productos);

    localStorage.setItem('Productos', JSON.stringify(array_productos));
    localStorage.setItem('Productos1', JSON.stringify(array_productos1));
    llenar_carro();
}

function sumarProductosRepetidos(arrayProductos) {
    var productosSumados = {};
    arrayProductos.forEach(function(producto) {
      var productId = producto.id;
      var cantidad = producto.cantidad || 1;
      if (productosSumados.hasOwnProperty(productId)) {
        productosSumados[productId] += cantidad;
      } else {
        productosSumados[productId] = cantidad;
      }
    });
  
    var arrayProductosSumados = [];
    for (var productId in productosSumados) {
      arrayProductosSumados.push({id: productId, cantidad: productosSumados[productId] });
    }
  
    return arrayProductosSumados;
  }

function llenar_carro() {
    var arrayData = JSON.parse(localStorage.getItem('Productos'));
    var arrayLength = arrayData.length;
    
    if (arrayLength == 0){
        $('#carrito-producto').html('');   
        var texto = '';
        texto += `
            <tr>
                <td></td>
                <td>Carro Vacio</td>
                <td></td>
            </tr>
            `;
        var total = 0;

        $('#carrito-producto').append(texto);         
        $('#carrito-precio').html(total);
        var spanElement = document.getElementById('carrospan');
        spanElement.textContent = 0;
    }else{
        $('#carrito-producto').html('');   
        var texto = '';
        var total = 0;
        array_productos.forEach((producto, index) => {
            texto += `
            <tr>
                <td><img src="${producto.img}" width="50px"></td>
                <td>${producto.nombre}</td>
                <td>$${producto.precio}</td>
                <td>${producto.cantidad}</td>
                <td>
                    <button class="btn delete-button" data-index="${index}"><img src="../static/img/delete.png" height="25px"></button>
                </td>
            </tr>
            `;
            total += producto.precio;
        });

        $('#carrito-producto').append(texto);         
        $('#carrito-precio').html(total);
        
        
        $('.delete-button').click(function() {
            var index = $(this).data('index');
            eliminar_producto(index);
        });

        var spanElement = document.getElementById('carrospan');
        spanElement.textContent = arrayLength;
    }
}

function eliminar_producto(index) {
    array_productos.splice(index, 1);
    localStorage.setItem('Productos', JSON.stringify(array_productos));
    llenar_carro();
}


function vaciarCarro(){
    localStorage.removeItem('Productos');
}

function onLoad(){
    llenar_carro()
}

window.addEventListener('load', function() {
    onLoad();
  });



// Agregar evento de escucha para cada input de cantidad


/*
let btnCart = document.getElementById("cart");

btnCart.addEventListener('click',function(){

    products_array = [
        {sku:1, name:"Jujutsu Vol.11", price:"9000", amount:20}
    ]

    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    fetch('/cart',{
    method:'POST', 
    headers:{
        'Content-type':'applications/json',
        'X-CSRFToken':token,

    },
    body:JSON.stringify(products_array)
    })

})
*/