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
  