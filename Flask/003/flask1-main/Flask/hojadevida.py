from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Home.html')

@app.route('/PagPrincipal.html')
def hoja_de_vida():
   return render_template('PagPrincipal.html')

@app.route('/HomeF.html')
def home_f():
   return render_template('HomeF.html')


@app.route('/PagDatos.html')
def hoja_de_vida2():
   return render_template('PagDatos.html')

@app.route('/PagFormacion.html')
def hoja_de_vida3():
   return render_template('PagFormacion.html')

@app.route('/PagTecnologias.html')
def hoja_de_vida4():
   return render_template('PagTecnologias.html')

@app.route('/prog/hojadevida/Principal.html')
def hoja_de_vida5():
   return render_template('Principal.html') 

@app.route('/prog/hojadevida/Datosbasicos.html')
def hoja_de_vida6():
   return render_template('Datosbasicos.html') 

@app.route('/prog/hojadevida/Formacion.html')
def hoja_de_vida7():
   return render_template('Formacion.html') 

@app.route('/prog/hojadevida/Tecnologias.html')
def hoja_de_vida8():
   return render_template('Tecnologias.html')    

@app.route('/DatosF.html')
def hoja_de_vida9():
   return render_template('DatosF.html')

@app.route('/FormacionF.html')
def hoja_de_vida10():
   return render_template('FormacionF.html')

@app.route('/TecnologiasF.html')
def hoja_de_vida11():
   return render_template('TecnologiasF.html')


if __name__ == '__main__':
   app.run(debug = True)