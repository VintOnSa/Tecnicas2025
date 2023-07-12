var form = document.getElementById('formAddProduct');
if(form){
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        var txTitle = document.getElementById('txTitle').value;
        var txAuthor = document.getElementById('txAuthor').value;
        var txPrice = document.getElementById('txPrice').value;
        var optCate = document.getElementById('optCate').value;
        var txStock = document.getElementById('txStock').value;
        var txDesc = document.getElementById('txDesc').value;
        var iptImg = document.getElementById('iptImg').value;
      
        console.log(optCate)
      
        if (!txTitle || !txAuthor || !txPrice || !txStock || !txDesc || !iptImg) {
          $(function(){
            $("#formAddProduct").validate({
                rules:{
                    txTitle:{
                        required: true,
                        minlength: 3
                    },
                    txAuthor:{
                        required: true,
                        minlength: 2
                    },
                    txPrice:{
                        required: true,
                        minlength: 2
                    },
                    txStock:{
                        required:true,
                        minlength: 1
                    },
                    txDesc:{
                        required:true,
                        minlength: 10
                    },
                    optCate:{
                        required:true,
                    },
                    iptImg:{
                        required:true
                    }
                },
                messages:{
                    txTitle:{
                        required:"Debe Ingresar El Titulo",
                        minlength:"Minimo 3 caracteres"
                    },
                    txAuthor:{
                        required:"Debe Ingresar El Autor.",
                        minlength:"Minimo 2 caracteres"
                    },
                    txPrice:{
                        required:"Debe Ingresar El Precio",
                        minlength:"Minimo 2 caracteres"
                    },
                    txStock:{
                        required:"Debe Ingresar El Stock Disponible",
                        minlength:"Minimo 1 caracteres"
                    },
                    txDesc:{
                        required:"Debe Ingresar Una Descripcion",
                        minlength:"Minimo 10 caracteres"
                    },
                    optCate:{
                        required:"La Categoria es Obligatoria"
                    },
                    iptImg:{
                        required:"La Portada es Obligatoria"
                    }
                }
            })
          })
          return;
        }
        if (optCate === "null" || optCate.value === "null"){
          $(function(){
              $("#formAddProduct").validate({
                  rules:{
                      optCate:{
                          required:true,
                      }
                  },
                  messages:{
                      optCate:{
                          required:"La Categoria es Obligatoria"
                      } 
                  }
              })
            })
          return;
        }else {
          form.submit();
        }
      });
      
}

var forme = document.getElementById('formEdProduct');
if(forme){
    forme.addEventListener('submit', function(event) {
        event.preventDefault();
        var txTitle = document.getElementById('txTitle').value;
        var txAuthor = document.getElementById('txAuthor').value;
        var txPrice = document.getElementById('txPrice').value;
        var optCate = document.getElementById('optCate').value;
        var txStock = document.getElementById('txStock').value;
        var txDesc = document.getElementById('txDesc').value;
        
        
      
        if (!txTitle || !txAuthor || !txPrice || !txStock || !txDesc) {
          $(function(){
            $("#formEdProduct").validate({
                rules:{
                    txTitle:{
                        required: true,
                        minlength: 3
                    },
                    txAuthor:{
                        required: true,
                        minlength: 2
                    },
                    txPrice:{
                        required: true,
                        minlength: 2
                    },
                    txStock:{
                        required:true,
                        minlength: 1
                    },
                    txDesc:{
                        required:true,
                        minlength: 10
                    },
                    optCate:{
                        required:true,
                    }
                },
                messages:{
                    txTitle:{
                        required:"Debe Ingresar El Titulo",
                        minlength:"Minimo 3 caracteres"
                    },
                    txAuthor:{
                        required:"Debe Ingresar El Autor.",
                        minlength:"Minimo 2 caracteres"
                    },
                    txPrice:{
                        required:"Debe Ingresar El Precio",
                        minlength:"Minimo 2 caracteres"
                    },
                    txStock:{
                        required:"Debe Ingresar El Stock Disponible",
                        minlength:"Minimo 1 caracteres"
                    },
                    txDesc:{
                        required:"Debe Ingresar Una Descripcion",
                        minlength:"Minimo 10 caracteres"
                    },
                    optCate:{
                        required:"La Categoria es Obligatoria"
                    }  
                }
            })
          })
          return;
        }
        if (optCate === "null" || optCate.value === "null"){
          $(function(){
              $("#formEdProduct").validate({
                  rules:{
                      optCate:{
                          required:true,
                      }
                  },
                  messages:{
                      optCate:{
                          required:"La Categoria es Obligatoria"
                      } 
                  }
              })
            })
          return;
        }else {
          forme.submit();
        }
      });
      
}


var formc = document.getElementById('formAddCate');
if(formc){
    formc.addEventListener('submit', function(event) {
        event.preventDefault();
        var txTitle = document.getElementById('txTitle').value;
        var iptImg = document.getElementById('iptImg').value;
      
        if (!txTitle || !iptImg) {
          $(function(){
            $("#formAddCate").validate({
                rules:{
                    txTitle:{
                        required: true,
                        minlength: 3
                    },
                    iptImg:{
                        required:true
                    }
                },
                messages:{
                    txTitle:{
                        required:"Nombre de la Categoria es Obligatorio",
                        minlength:"Minimo 3 caracteres"
                    },
                    iptImg:{
                        required:"La Imagen es Obligatoria"
                    }
                    
                }
            })
          })
          return;
        }
        else{
          formc.submit();
        } 
      });  
}

var formce = document.getElementById('formEdCate');
if(formce){
    formce.addEventListener('submit', function(event) {
        event.preventDefault();
        var txTitle = document.getElementById('txName').value;
      
        if (!txTitle) {
          $(function(){
            $("#formEdCate").validate({
                rules:{
                    txName:{
                        required: true,
                        minlength: 3
                    }
                },
                messages:{
                    txName:{
                        required:"Nombre de la Categoria es Obligatorio",
                        minlength:"Minimo 3 caracteres"
                    }
                }
            })
          })
          return;
        }
        else{
          formce.submit();
        } 
      });  
}


$(document).ready(function() {
    var formRe = document.getElementById('formEdUser');
    if (formRe) {
      $("#formEdUser").validate({
        rules: {
          txUser: {
            required: true,
            minlength: 4
          },
          txPass: {
            required: true,
            minlength: 8,
            validarContrasena: true 
          },
          txPass2: {
            required: true,
            minlength: 8,
            validarContrasena: true 
          },
          txUPass:{
            required: false
          },
          txPassA: {
            required: true,
            minlength: 8,
          },
          txEmail: {
            required: true,
            email: true,
            validarCorreo: true
          }
        },
        messages: {
          txUser: {
            required: "Debe ingresar un Nombre de Usuario",
            minlength: "Mínimo 4 caracteres"
          },
          txPass: {
            required: "Debe ingresar una Contraseña",
            minlength: "Mínimo 8 caracteres",
            validarContrasena: "La Contraseña debe contener al menos una letra Mayúscula, una letra Minúscula y un Número."
          },
          txPass2: {
            required: "Debe ingresar una Contraseña",
            minlength: "Mínimo 8 caracteres"
          },
          txPassA: {
            required: "Debe ingresar una Contraseña",
            minlength: "Mínimo 8 caracteres"
          },
          txEmail: {
            required: "Debe ingresar un Email",
            email: "Por favor ingrese un Email válido",
            validarCorreo: "Ingrese un Dominio válido."
          }
        }
      });
    }
  });

$(document).ready(function() {
    var formReg = document.getElementById('registerform');
    if (formReg) {
      $("#registerform").validate({
        rules: {
          username: {
            required: true,
            minlength: 4
          },
          password: {
            required: true,
            minlength: 8,
            validarContrasena: true 
          },
          email: {
            required: true,
            email: true,
            validarCorreo: true
          }
        },
        messages: {
          username: {
            required: "Debe ingresar un Nombre de Usuario",
            minlength: "Mínimo 4 caracteres"
          },
          password: {
            required: "Debe ingresar una Contraseña",
            minlength: "Mínimo 8 caracteres",
            validarContrasena: "La Contraseña debe contener al menos una letra Mayúscula, una letra Minúscula y un Número."
          },
          email: {
            required: "Debe ingresar un Email",
            email: "Por favor ingrese un Email válido",
            validarCorreo: "Ingrese un Dominio válido."
          }
        }
      });
    }
  });
  

$(document).ready(function() {
  var formLog = document.getElementById('loginform');
  if (formLog) {
    $("#loginform").validate({
      rules: {
        username: {
          required: true
        },
        password: {
          required: true
        },
      },
      messages: {
        username: {
          required: "Debe ingresar un Nombre de Usuario"
        },
        password: {
          required: "Debe ingresar una Contraseña"
        }
      }
    });
  }
});


$.validator.addMethod("validarContrasena", function(value, element) {
  return /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d.*-_]{8,}$/.test(value);
}, "La Contraseña debe contener al menos una letra Mayúscula, una letra Minúscula y un Número.");

$.validator.addMethod("validarCorreo", function(value, element) {
  return /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value);
}, "Ingrese un Dominio válido.");