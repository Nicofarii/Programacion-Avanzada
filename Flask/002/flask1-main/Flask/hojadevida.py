from flask import Flask, render_template
app = Flask(__name__)

@app.route('/mateo') 
def hoja_de_vida():
   return render_template('PagPrincipal.html')

@app.route('/mateo/PagPrincipal.html') 
def hoja_de_vida1():
   return render_template('PagPrincipal.html')

@app.route('/mateo/PagDatos.html')
def hoja_de_vida2():
   return render_template('PagDatos.html')

@app.route('/mateo/PagFormacion.html')
def hoja_de_vida3():
   return render_template('PagFormacion.html')

@app.route('/mateo/PagTecnologias.html')
def hoja_de_vida4():
   return render_template('PagTecnologias.html')




if __name__ == '__main__':
   app.run(debug = True)