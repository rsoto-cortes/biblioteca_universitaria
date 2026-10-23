from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title ="Home", message="Bienvenido a la pagina donde podras buscar todo tipo de informacion que necesites")

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', title ="Catalogo", message="Bienvenido al catalogo de libros")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', title ="Servicios", message="Bienvenido a la pagina de servicios")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', title ="Contacto", message="Bienvenido a la pagina de contacto")


if __name__ == '__main__':
    app.run(debug=True, port=5050)