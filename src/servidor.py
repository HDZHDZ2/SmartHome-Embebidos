from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/Simulador/casa.html')

@app.route('/focos')
def focos():
    return render_template('/Focos/Focos.html')

@app.route('/camaras')
def camaras():
    return render_template('/Camaras/Camaras.html')

@app.route('/timbre')
def timbre():
    return render_template('/Timbre_Garage/Timbre_Garage.html')

