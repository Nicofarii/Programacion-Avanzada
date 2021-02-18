  
function iniciar(){
    document.getElementById("display").innerHTML = 0;
}

function actualizar(_elemento){
    valor_actual = document.getElementById("display").innerHTML;
    if(valor_actual == "0")
        document.getElementById("display").innerHTML = _elemento.innerText;
    else {
        document.getElementById("display").innerHTML = valor_actual + _elemento.innerText;
    }
}

function evaluar(){
    expresion = document.getElementById("display").innerHTML
    resultado = eval(expresion);
    document.getElementById("display").innerHTML = resultado;
}

function borrar(){
    expresion = document.getElementById("display").innerHTML;
    document.getElementById("display").innerHTML = expresion.substring(0, expresion.length-1)
    if(document.getElementById("display").innerHTML.length <= 0)
        iniciar();
}