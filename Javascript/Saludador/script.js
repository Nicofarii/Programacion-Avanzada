  
function saludar(){
    nombre = document.getElementById("nombre").value;
    document.getElementById("msn").innerHTML = "Hola " + nombre;
    return false;
}