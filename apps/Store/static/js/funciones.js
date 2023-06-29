function Apireloj(){
  fetch('http://worldtimeapi.org/api/timezone/America/Santiago')
      .then(response => response.json())
      .then(data =>{
          let h4hora = document.getElementById("reloj");
          
          var hora = data.datetime.substring(11, 19);

          h4hora.innerHTML = hora;
      })
}
function actualizaReloj(){
  Apireloj();
  setInterval(Apireloj, 1000);
}


$(document).ready(function() {
    $('#searchInput').on('keyup', function() {
        var searchTerm = $(this).val();
        $.ajax({
            url: 'search/',
            type: 'GET',
            data: { 'q': searchTerm },
            success: function(response) {
                $('#resultadosCollapse .card').empty();
                $.each(response.results, function(index, result) {
                    var content = "";
                    if (result.img) {
                        content = '<a href="/Prodview/'+result.id+'" style="text-decoration: none; color: var(--fourth-color);">'+
                        '<div class="col">'+
                        '<div class="row">'+
                        '<div class="col-4"><img src="' + result.img + '"></div>';
                        content += '<div class="col-8 d-flex align-items-center me-0"><h6>'+result.name+'</h6></div>'+
                        '</div>'+
                        '</div>'+
                        '</a>';
                    };
                    
                    $('#resultadosCollapse .card').append(content);
                 });
            }
        });
    });
});


$(function(){
    $("#listSearch").on("keyup", function(){
        let val = $(this).val().toLowerCase();
        $("table tbody tr").filter(function(){
            let text = $(this).text().toLowerCase();
            let match = text.indexOf(val) > -1;
            if (match) {
                $(this).stop().fadeIn(200);
            } else {
                $(this).stop().fadeOut(200);
            }
        })
    })
})


/*document.getElementById("agregarBtn").addEventListener("click", function() {
  location.reload();
});*/

var abrirModalBtn = document.querySelectorAll('.btn-abrir-modal');

abrirModalBtn.forEach(function(button) {
  button.addEventListener('click', function() {
    var productId = button.getAttribute('data-product-id');

    var modal = document.getElementById('pemodal');
    modal.setAttribute('data-product-id', productId);
    fetch("/obtainProd?id=" + productId)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        document.getElementById("modalbody").textContent = "¿Esta seguro que Desea Eliminar "+ data.name +"?";
      })
      .catch(function(error) {
        console.error("Error al obtener la información del producto:", error);
      });
      var delProd = document.getElementById('delBtn');
      delProd.href = '/delProd/' + productId;
  });
});

var abrirModalBtnul = document.querySelectorAll('.btn-abrir-modalul');

abrirModalBtnul.forEach(function(button) {
  button.addEventListener('click', function() {
    var userId = button.getAttribute('data-username');

    var modal = document.getElementById('uemodal');
    modal.setAttribute('data-username', userId);
    fetch("/obtainUser?id=" + userId)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        document.getElementById("modalbodyue").textContent = "¿Esta seguro que Desea Eliminar "+ data.name +"?";
      })
      .catch(function(error) {
        console.error("Error al obtener la información del Usuario:", error);
      });
      var delProdul = document.getElementById('delBtnul');
      delProdul.href = '/delUser/' + userId;
  });
});



$(document).ready(function() {
  if ($('.alert-success').length) {
      var successToast = document.getElementById('successToast');
      var toast = new bootstrap.Toast(successToast);
      toast.show();
  }
  setTimeout(function() {
      var successToast = document.getElementById('successToast');
      
      if (successToast) {
          var toast = new bootstrap.Toast(successToast);
          successToast.classList.add("d-none");
        }
  }, 1000);
});

  $(document).ready(function() {
    if ($('.alert-success').length) {
        var errorToast = document.getElementById('errorToast');
        var toast = new bootstrap.Toast(errorToast);
        toast.show();
    }
    setTimeout(function() {
        var errorToast = document.getElementById('errorToast');
        
        if (errorToast) {
            var toast = new bootstrap.Toast(errorToast);
            errorToast.classList.add("d-none");
          }
    }, 1000);
  });

  




const darkModeToggle = document.getElementById('dark-mode-toggle');
const section = document.getElementById('bgkc');
const card = document.getElementById('cards');

const savedMode = localStorage.getItem('darkMode');

if (savedMode === 'dark') {
  enableDarkMode();
}

function enableDarkMode() {
  section.classList.add('dark-mode');
  card.classList.add('dark-mode');
  localStorage.setItem('darkMode', 'dark');
}

function disableDarkMode() {
  section.classList.remove('dark-mode');
  card.classList.remove('dark-mode');
  localStorage.setItem('darkMode', 'light');
}

darkModeToggle.addEventListener('click', () => {
  const isDarkModeEnabled = section.classList.contains('dark-mode');


  if (isDarkModeEnabled) {
    disableDarkMode();
  } else {
    enableDarkMode();
  }
});
