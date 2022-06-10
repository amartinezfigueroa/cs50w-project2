document.addEventListener('DOMContentLoaded', () => {

    var socket = io(); //servidor
        socket.on('connect', function() {
            //socket.emit('my event',  'I\'m connected!');
            
            document.querySelector('#new-user').onsubmit = () => {
                let nombre = document.querySelector("#user").value;
                socket.emit('senduser', nombre);

                return false;
            };


        });

    //cliente
   // socket.on("my response", (data) => { 
       // console.log(data); 
   // });
    
    socket.on("Mensajes de alerta", (data) => { 
        alert(data); 
    });
    
    socket.on("Registrar usuario", (nombre) => { 
        localStorage.setItem("nombre", nombre);
        let usuario = localStorage.getItem("nombre")
        alert("Bienvenidos" + usuario)
    });    

});