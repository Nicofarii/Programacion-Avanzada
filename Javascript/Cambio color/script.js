function colorear(){
    color = parseInt(document.getElementById("color").value)

  if (color == 1){
    document.getElementById("elemento").style.color = "yellow";
  }
  else if(color == 2){
    document.getElementById("elemento").style.color = "blue";
  }
  else if(color == 3){
    document.getElementById("elemento").style.color = "red";
  }
  else if(color == 4){
    document.getElementById("elemento").style.color = "green";
  }
  else if(color == 5){
    document.getElementById("elemento").style.color = "orange";
  }
  else if(color == 6){
    document.getElementById("elemento").style.color = "purple";
  }
  else if(color == 7){
    document.getElementById("elemento").style.color = "cyan";
  }
  else if(color == 8){
    document.getElementById("elemento").style.color = "gray";
  }
  else if(color == 9){
    document.getElementById("elemento").style.color = "violet";
  }
  else{
    document.getElementById("elemento").style.color = "black";
  }
}
