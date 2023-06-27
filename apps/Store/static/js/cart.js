

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